"""
Crossword OCR utility.

Goal: Extract only text from a crossword image with robust preprocessing.
Requires: easyocr, Pillow. Optional: opencv-python for best results.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps

try:
    import cv2  # type: ignore

    HAS_CV2 = True
except Exception:
    cv2 = None
    HAS_CV2 = False

try:
    import easyocr  # type: ignore
except Exception as exc:  # pragma: no cover - import-time error handling
    raise SystemExit(
        "easyocr is required. Install with: pip install easyocr"
    ) from exc


def _ensure_easyocr_model(reader: "easyocr.Reader") -> None:
    try:
        _ = reader.recognize  # smoke-check reader is ready
    except Exception as exc:  # pragma: no cover - runtime environment issue
        raise SystemExit(
            "EasyOCR failed to initialize. Check torch/CPU install."
        ) from exc


def _downscale_gray(gray, max_dim: int | None):
    if not max_dim:
        return gray
    h, w = gray.shape[:2]
    max_side = max(h, w)
    if max_side <= max_dim:
        return gray
    scale = max_dim / max_side
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    return cv2.resize(gray, (new_w, new_h), interpolation=cv2.INTER_AREA)


def _cv2_preprocess(image_path: Path, max_dim: int | None) -> "cv2.Mat":
    img = cv2.imread(str(image_path))
    if img is None:
        raise SystemExit(f"Unable to read image: {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return _downscale_gray(gray, max_dim)


def _pil_preprocess(image_path: Path, max_dim: int | None) -> Image.Image:
    img = Image.open(image_path)
    img = ImageOps.grayscale(img)
    if not max_dim:
        return img
    w, h = img.size
    max_side = max(w, h)
    if max_side <= max_dim:
        return img
    scale = max_dim / max_side
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    return img.resize((new_w, new_h), resample=Image.Resampling.LANCZOS)


def _normalize_lang(lang: str) -> str:
    # EasyOCR uses ISO 639-1 codes (e.g., "en"), not Tesseract's "eng".
    lang = lang.strip().lower()
    return "en" if lang in {"eng", "english"} else lang


def _order_points(pts: "cv2.Mat") -> "cv2.Mat":
    rect = pts.astype("float32")
    s = rect.sum(axis=1)
    diff = (rect[:, 0] - rect[:, 1]).reshape(-1)
    ordered = [
        rect[s.argmin()],  # top-left
        rect[diff.argmin()],  # top-right
        rect[s.argmax()],  # bottom-right
        rect[diff.argmax()],  # bottom-left
    ]
    return np.array(ordered, dtype="float32")


def _find_largest_quad(bin_img: "cv2.Mat") -> "cv2.Mat | None":
    contours, _ = cv2.findContours(
        bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    if not contours:
        return None
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    for cnt in contours[:8]:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        if len(approx) == 4:
            return approx.reshape(4, 2)
    return None


def _warp_to_square(gray: "cv2.Mat", *, scale: float = 1.08) -> "cv2.Mat":
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 5
    )
    inv = 255 - thresh
    quad = _find_largest_quad(inv)
    h_img, w_img = gray.shape[:2]
    if quad is None:
        return gray
    # If detected quad is too small, fall back to full image
    quad_area = cv2.contourArea(quad.reshape(-1, 1, 2))
    if quad_area < 0.4 * (w_img * h_img):
        return gray
    # Expand quad slightly to avoid cropping grid edges
    rect = _order_points(quad)
    center = rect.mean(axis=0)
    rect = (rect - center) * scale + center
    rect[:, 0] = np.clip(rect[:, 0], 0, w_img - 1)
    rect[:, 1] = np.clip(rect[:, 1], 0, h_img - 1)
    (tl, tr, br, bl) = rect
    widthA = int(((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2) ** 0.5)
    widthB = int(((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2) ** 0.5)
    heightA = int(((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2) ** 0.5)
    heightB = int(((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2) ** 0.5)
    max_w = max(widthA, widthB)
    max_h = max(heightA, heightB)
    side = max(max_w, max_h)
    dst = np.array(
        [[0, 0], [side - 1, 0], [side - 1, side - 1], [0, side - 1]],
        dtype="float32",
    )
    matrix = cv2.getPerspectiveTransform(rect, dst)
    return cv2.warpPerspective(gray, matrix, (side, side))


def _prepare_cell_variants(cell: "cv2.Mat") -> list["cv2.Mat"]:
    # Generate per-cell variants: raw, Otsu, and adaptive threshold
    variants = [cell]
    _, otsu = cv2.threshold(cell, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    variants.append(otsu)
    adaptive = cv2.adaptiveThreshold(
        cell, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 5
    )
    variants.append(adaptive)
    return variants


def _disambiguate_char(cell: "cv2.Mat", ch: str) -> str:
    # Heuristics for common confusions: O/Q/D and I/L/T
    if ch in {"O", "Q", "D"}:
        h, w = cell.shape[:2]
        cx1 = int(w * 0.35)
        cx2 = int(w * 0.65)
        cy1 = int(h * 0.35)
        cy2 = int(h * 0.65)
        center = cell[cy1:cy2, cx1:cx2]
        # Estimate if center has a hole (Q/D/O); lower mean indicates a hole
        center_mean = float(center.mean())
        if center_mean < 120:
            # Could be O/Q/D, look for Q tail: dark pixels in bottom-right
            br = cell[int(h * 0.65) : int(h * 0.9), int(w * 0.65) : int(w * 0.9)]
            if float(br.mean()) < 140:
                return "Q"
            # D tends to be more vertical-right heavy; check right stripe
            right = cell[int(h * 0.2) : int(h * 0.8), int(w * 0.7) : int(w * 0.9)]
            left = cell[int(h * 0.2) : int(h * 0.8), int(w * 0.1) : int(w * 0.3)]
            if float(right.mean()) < float(left.mean()) - 5:
                return "D"
            return "O"
    if ch in {"I", "L", "T"}:
        h, w = cell.shape[:2]
        top = cell[int(h * 0.1) : int(h * 0.25), int(w * 0.2) : int(w * 0.8)]
        mid = cell[int(h * 0.45) : int(h * 0.55), int(w * 0.2) : int(w * 0.8)]
        bottom = cell[int(h * 0.75) : int(h * 0.9), int(w * 0.2) : int(w * 0.8)]
        top_mean = float(top.mean())
        mid_mean = float(mid.mean())
        bottom_mean = float(bottom.mean())
        # Darker = more ink
        if top_mean < 140 and mid_mean < 140:
            return "T"
        if bottom_mean < 140 and top_mean > 150:
            return "L"
        return "I"
    return ch


def _ocr_cell(
    reader: "easyocr.Reader",
    cell: "cv2.Mat",
    whitelist: str | None,
    *,
    text_threshold: float,
    low_text: float,
    link_threshold: float,
    mag_ratio: float,
    contrast_ths: float,
    adjust_contrast: float,
) -> tuple[str, float]:
    base_kwargs = {
        "detail": 1,
        "paragraph": False,
        "text_threshold": text_threshold,
        "low_text": low_text,
        "link_threshold": link_threshold,
        "mag_ratio": mag_ratio,
        "contrast_ths": contrast_ths,
        "adjust_contrast": adjust_contrast,
    }
    if whitelist:
        base_kwargs["allowlist"] = whitelist

    # Second pass: more permissive thresholds to catch faint letters
    relaxed_kwargs = dict(base_kwargs)
    relaxed_kwargs["text_threshold"] = max(0.2, text_threshold - 0.1)
    relaxed_kwargs["low_text"] = max(0.1, low_text - 0.1)
    relaxed_kwargs["contrast_ths"] = max(0.03, contrast_ths - 0.03)
    relaxed_kwargs["adjust_contrast"] = min(0.9, adjust_contrast + 0.1)
    best_char = " "
    best_conf = 0.0
    for variant in _prepare_cell_variants(cell):
        for kwargs in (base_kwargs, relaxed_kwargs):
            results = reader.readtext(variant, **kwargs)
            for item in results:
                if not isinstance(item, (list, tuple)) or len(item) < 3:
                    continue
                text = str(item[1])
                conf = float(item[2]) if item[2] is not None else 0.0
                for ch in text:
                    if ch.isalpha():
                        ch = ch.upper()
                        if conf >= best_conf:
                            best_conf = conf
                            best_char = _disambiguate_char(variant, ch)
                        break
    return best_char, best_conf


def _grid_ocr_cv2(
    image_path: Path,
    reader: "easyocr.Reader",
    whitelist: str | None,
    *,
    cols: int,
    rows: int,
    cell_inset: float,
    jitter: int,
    warp_tries: int,
    warp_scale_step: float,
    text_threshold: float,
    low_text: float,
    link_threshold: float,
    mag_ratio: float,
    contrast_ths: float,
    adjust_contrast: float,
    max_dim: int | None,
) -> str:
    img = cv2.imread(str(image_path))
    if img is None:
        raise SystemExit(f"Unable to read image: {image_path}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = _downscale_gray(gray, max_dim)
    # Build warp scale candidates around 1.0
    scales = [1.0]
    if warp_tries > 0:
        for k in range(1, warp_tries + 1):
            scales.append(1.0 + k * warp_scale_step)
            scales.append(max(0.9, 1.0 - k * warp_scale_step))

    # Build jitter offsets (pixels)
    if jitter <= 0:
        offsets = [(0, 0)]
    else:
        step = max(1, jitter)
        offsets = [(dy, dx) for dy in (-step, 0, step) for dx in (-step, 0, step)]

    best_grid: list[list[str]] = [[" " for _ in range(cols)] for _ in range(rows)]
    best_conf: list[list[float]] = [[0.0 for _ in range(cols)] for _ in range(rows)]

    for scale in scales:
        warped = _warp_to_square(gray, scale=scale)
        h, w = warped.shape[:2]
        cell_h = max(h // rows, 1)
        cell_w = max(w // cols, 1)
        inset = int(min(cell_h, cell_w) * cell_inset)

        for r in range(rows):
            y1 = r * cell_h
            y2 = (r + 1) * cell_h
            for c in range(cols):
                x1 = c * cell_w
                x2 = (c + 1) * cell_w

                best_char = best_grid[r][c]
                best_c = best_conf[r][c]

                for dy, dx in offsets:
                    yy1 = max(0, y1 + dy)
                    yy2 = min(h, y2 + dy)
                    xx1 = max(0, x1 + dx)
                    xx2 = min(w, x2 + dx)
                    if yy2 <= yy1 or xx2 <= xx1:
                        continue
                    cell = warped[yy1:yy2, xx1:xx2]
                    if (
                        inset > 0
                        and cell.shape[0] > inset * 2
                        and cell.shape[1] > inset * 2
                    ):
                        cell = cell[inset:-inset, inset:-inset]
                    cell = cv2.resize(cell, (64, 64), interpolation=cv2.INTER_AREA)
                    # Light per-cell sharpen to improve single-character clarity
                    blur = cv2.GaussianBlur(cell, (0, 0), 0.8)
                    cell = cv2.addWeighted(cell, 1.5, blur, -0.5, 0)
                    ch, conf = _ocr_cell(
                        reader,
                        cell,
                        whitelist,
                        text_threshold=text_threshold,
                        low_text=low_text,
                        link_threshold=link_threshold,
                        mag_ratio=mag_ratio,
                        contrast_ths=contrast_ths,
                        adjust_contrast=adjust_contrast,
                    )
                    if conf >= best_c and ch != " ":
                        best_char = ch
                        best_c = conf

                best_grid[r][c] = best_char
                best_conf[r][c] = best_c

    return "\n".join("".join(row) for row in best_grid)


def extract_text(
    image_path: Path,
    lang: str,
    whitelist: str | None,
    no_preprocess: bool,
    gpu: bool,
    cell_inset: float,
    jitter: int,
    warp_tries: int,
    warp_scale_step: float,
    text_threshold: float,
    low_text: float,
    link_threshold: float,
    mag_ratio: float,
    contrast_ths: float,
    adjust_contrast: float,
    *,
    grid_ocr: bool,
    max_dim: int | None,
    rows: int,
    cols: int,
) -> str:
    lang = _normalize_lang(lang)
    reader = easyocr.Reader([lang], gpu=gpu)
    _ensure_easyocr_model(reader)

    if grid_ocr and HAS_CV2:
        try:
            return _grid_ocr_cv2(
                image_path,
                reader,
                whitelist,
                rows=rows,
                cols=cols,
                cell_inset=cell_inset,
                jitter=jitter,
                warp_tries=warp_tries,
                warp_scale_step=warp_scale_step,
                text_threshold=text_threshold,
                low_text=low_text,
                link_threshold=link_threshold,
                mag_ratio=mag_ratio,
                contrast_ths=contrast_ths,
                adjust_contrast=adjust_contrast,
                max_dim=max_dim,
            )
        except Exception:
            pass
    if no_preprocess:
        pil_img = Image.open(image_path)
        pil_img = ImageOps.grayscale(pil_img)
        if max_dim:
            w, h = pil_img.size
            max_side = max(w, h)
            if max_side > max_dim:
                scale = max_dim / max_side
                new_w = max(1, int(w * scale))
                new_h = max(1, int(h * scale))
                pil_img = pil_img.resize(
                    (new_w, new_h), resample=Image.Resampling.LANCZOS
                )
        return _run_easyocr(
            reader,
            pil_img,
            whitelist,
            text_threshold=text_threshold,
            low_text=low_text,
            link_threshold=link_threshold,
            mag_ratio=mag_ratio,
            contrast_ths=contrast_ths,
            adjust_contrast=adjust_contrast,
        )

    if HAS_CV2:
        processed = _cv2_preprocess(image_path, max_dim)
        text = _run_easyocr(
            reader,
            processed,
            whitelist,
            text_threshold=text_threshold,
            low_text=low_text,
            link_threshold=link_threshold,
            mag_ratio=mag_ratio,
            contrast_ths=contrast_ths,
            adjust_contrast=adjust_contrast,
        )
        if text.strip():
            return text
        # Fallback: try raw grayscale without allowlist
        raw = _pil_preprocess(image_path, max_dim)
        return _run_easyocr(
            reader,
            raw,
            None,
            text_threshold=text_threshold,
            low_text=low_text,
            link_threshold=link_threshold,
            mag_ratio=mag_ratio,
            contrast_ths=contrast_ths,
            adjust_contrast=adjust_contrast,
        )

    processed = _pil_preprocess(image_path, max_dim)
    text = _run_easyocr(
        reader,
        processed,
        whitelist,
        text_threshold=text_threshold,
        low_text=low_text,
        link_threshold=link_threshold,
        mag_ratio=mag_ratio,
        contrast_ths=contrast_ths,
        adjust_contrast=adjust_contrast,
    )
    if text.strip():
        return text
    raw = _pil_preprocess(image_path, max_dim)
    return _run_easyocr(
        reader,
        raw,
        None,
        text_threshold=text_threshold,
        low_text=low_text,
        link_threshold=link_threshold,
        mag_ratio=mag_ratio,
        contrast_ths=contrast_ths,
        adjust_contrast=adjust_contrast,
    )


def _run_easyocr(
    reader: "easyocr.Reader",
    image,
    whitelist: str | None,
    *,
    text_threshold: float,
    low_text: float,
    link_threshold: float,
    mag_ratio: float,
    contrast_ths: float,
    adjust_contrast: float,
) -> str:

    # allowlist limits to crossword-friendly characters
    read_kwargs = {"detail": 0, "paragraph": False}
    if whitelist:
        read_kwargs["allowlist"] = whitelist

    results = reader.readtext(
        image,
        **read_kwargs,
        text_threshold=text_threshold,
        low_text=low_text,
        link_threshold=link_threshold,
        mag_ratio=mag_ratio,
        contrast_ths=contrast_ths,
        adjust_contrast=adjust_contrast,
    )
    # Join tokens with newlines to preserve separations
    return "\n".join(r.strip() for r in results if r.strip())


def _format_grid(text: str, cols: int = 30, rows: int = 30) -> str:
    letters_only = "".join(ch for ch in text if ch.isalpha()).upper()
    total = cols * rows
    if len(letters_only) < total:
        letters_only = letters_only.ljust(total)
    else:
        letters_only = letters_only[:total]
    return "\n".join(
        letters_only[i : i + cols] for i in range(0, total, cols)
    )


def _is_grid(text: str, cols: int = 30, rows: int = 30) -> bool:
    lines = text.splitlines()
    if len(lines) != rows:
        return False
    return all(len(line) == cols for line in lines)


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract text from a crossword image."
    )
    default_image = Path(__file__).resolve().parent / "crosseditold1.png"
    parser.add_argument(
        "image",
        type=Path,
        nargs="?",
        default=default_image,
        help="Path to crossword image (default: ocr/crosseditold1.png)",
    )
    parser.add_argument(
        "--lang",
        default="en",
        help="EasyOCR language code (default: en). 'eng' is accepted and maps to 'en'.",
    )
    parser.add_argument(
        "--rows",
        type=int,
        default=24,
        help="Number of crossword rows (default: 24).",
    )
    parser.add_argument(
        "--cols",
        type=int,
        default=24,
        help="Number of crossword columns (default: 24).",
    )
    parser.add_argument(
        "--whitelist",
        default="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        help="Allowed characters for OCR (default: A-Z)",
    )
    parser.add_argument(
        "--no-preprocess",
        action="store_true",
        help="Skip preprocessing and use raw grayscale image",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Write output text to file instead of stdout",
    )
    parser.add_argument(
        "--no-grid-ocr",
        action="store_true",
        help="Disable per-cell grid OCR and use full-image OCR (faster, lower CPU)",
    )
    parser.add_argument(
        "--max-dim",
        type=int,
        default=0,
        help="Downscale longest image side to this many pixels (default: 0 = disabled).",
    )
    parser.add_argument(
        "--cell-inset",
        type=float,
        default=0.12,
        help="Fraction to trim from cell borders (default: 0.12)",
    )
    parser.add_argument(
        "--jitter",
        type=int,
        default=3,
        help="Pixel jitter per cell (default: 3)",
    )
    parser.add_argument(
        "--warp-tries",
        type=int,
        default=2,
        help="Extra warp scales to try in each direction (default: 2)",
    )
    parser.add_argument(
        "--warp-scale-step",
        type=float,
        default=0.03,
        help="Scale step for warp tries (default: 0.03)",
    )
    parser.add_argument(
        "--gpu",
        action="store_true",
        help="Enable GPU for EasyOCR (default: CPU)",
    )
    parser.add_argument(
        "--text-threshold",
        type=float,
        default=0.35,
        help="EasyOCR text threshold (default: 0.35)",
    )
    parser.add_argument(
        "--low-text",
        type=float,
        default=0.2,
        help="EasyOCR low text threshold (default: 0.2)",
    )
    parser.add_argument(
        "--link-threshold",
        type=float,
        default=0.1,
        help="EasyOCR link threshold (default: 0.1)",
    )
    parser.add_argument(
        "--mag-ratio",
        type=float,
        default=2.0,
        help="EasyOCR magnification ratio (default: 2.0)",
    )
    parser.add_argument(
        "--contrast-ths",
        type=float,
        default=0.05,
        help="EasyOCR contrast threshold (default: 0.05)",
    )
    parser.add_argument(
        "--adjust-contrast",
        type=float,
        default=0.7,
        help="EasyOCR adjust contrast (default: 0.7)",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = _parse_args(argv)
    if not args.image.exists():
        raise SystemExit(f"Image not found: {args.image}")

    text = extract_text(
        args.image,
        lang=args.lang,
        whitelist=args.whitelist,
        no_preprocess=args.no_preprocess,
        gpu=args.gpu,
        cell_inset=args.cell_inset,
        jitter=args.jitter,
        warp_tries=args.warp_tries,
        warp_scale_step=args.warp_scale_step,
        text_threshold=args.text_threshold,
        low_text=args.low_text,
        link_threshold=args.link_threshold,
        mag_ratio=args.mag_ratio,
        contrast_ths=args.contrast_ths,
        adjust_contrast=args.adjust_contrast,
        grid_ocr=not args.no_grid_ocr,
        max_dim=None if args.max_dim == 0 else args.max_dim,
        rows=args.rows,
        cols=args.cols,
    )

    if not _is_grid(text, cols=args.cols, rows=args.rows):
        text = _format_grid(text, cols=args.cols, rows=args.rows)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
