
crossword = [
    list("mfroslmdemonsandlunaydeyteicms"),
    list("tsocubasromuhriticatalgclthien"),
    list("ekieprecexperimentinsoapndedta"),
    list("vdicecahitedtoposvgslsmiteivht"),
    list("ieuerchaasngesktiecoeapywwiboa"),
    list("tvqcnodzcvypmritrihssvgbfoncdd"),
    list("aighacxzvyihpoaoecsktkloxhmwso"),
    list("ttklttledpaopeunytjncathoughts"),
    list("iaqrumiulprarstsunwptnostoahav"),
    list("trburftoawgcvipdzzsneahspgrcha"),
    list("nrsyasxunhgvfayklyeqzicwrnslwr"),
    list("aawjllojcynirocfcmzjpiogzhrxai"),
    list("unekbuiidpcaigahlldorstzcugzha"),
    list("qsseuidtcmpxisoxwukrambmwwjcgb"),
    list("lnnoxbzsalqvqlgjkbvlcnimjxrxyl"),
    list("kjrvnaxvbtfpoisrcilwtloxlabbfe"),
    list("agurqozbeligszefmtmjidjieybhms"),
    list("mcptlfwheyyvppefoqvychnssduton"),
    list("eqztvxlmvpzrepgjfpheemeiyabbnu"),
    list("tnviupdlhusrsduktpniarbwmnffgz"),
    list("hjtxneuropsychologyziakcacivql"),
    list("oiwatutauvccuztsjfivgachhndpvz"),
    list("dxcqwmkfxhnoxgonabviamosejtdjg"),
    list("toyewhydohrkulwqptgjkxhukkpqdc"),
    list("dugntleljhpziftphogiianrqpooxz"),
    list("npzpgvoqppzhizysjpseudovmqoxec"),
    list("uoazfgmcdjpaqfqdksegaexeavuzba"),
    list("wswsyonxpdamtfyflghaursynnzsxo"),
    list("tuktgdmfiotibrpfgywpxpasvuzazg"),
    list("yuoijpyxcxvzldukxdhggohkkhuixu"),
]

#vars
words_to_find = [
    "apa",
    "case",
    "data",
    "experiment",
    "method",
    "mixed",
    "parapsychology",
    "practice",
    "psychology",
    "research",
    "scientific",
    "supernatural",
    "variables",
    "behavior",
    "creativity",
    "education",
    "humors",
    "narrative",
    "philosophy",
    "pseudo",
    "qualitative",
    "sample",
    "study",
    "survey",
    "wundt",
    "brain",
    "dangerous",
    "exorcism",
    "mental",
    "mind",
    "neuropsychology",
    "physical",
    "quantitative",
    "science",
    "thoughts"
]
output_image_path = "crossword_output.png"



def _find_word_positions(grid: list[list[str]], word: str) -> list[list[tuple[int, int]]]:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    directions = [
        ("E", 0, 1),
        ("W", 0, -1),
        ("S", 1, 0),
        ("N", -1, 0),
        ("SE", 1, 1),
        ("NE", -1, 1),
        ("SW", 1, -1),
        ("NW", -1, -1),
    ]
    matches: list[list[tuple[int, int]]] = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != word[0]:
                continue
            for _, dr, dc in directions:
                end_r = r + dr * (len(word) - 1)
                end_c = c + dc * (len(word) - 1)
                # Bounds check to prevent row/column wrap
                if end_r < 0 or end_r >= rows or end_c < 0 or end_c >= cols:
                    continue
                if all(grid[r + dr * i][c + dc * i] == word[i] for i in range(len(word))):
                    matches.append([(r + dr * i, c + dc * i) for i in range(len(word))])
    return matches


def _print_highlighted(
    grid: list[list[str]],
    highlights: dict[tuple[int, int], str],
    color_map: dict[str, str],
) -> None:
    # ANSI color for highlight; works in modern Windows terminals
    reset = "\x1b[0m"
    for r, row in enumerate(grid):
        line = []
        for c, ch in enumerate(row):
            key = (r, c)
            if key in highlights:
                color = color_map[highlights[key]]
                line.append(f"{color}{ch.upper()}{reset}")
            else:
                line.append(ch)
        print(" ".join(line))


def _render_to_image(
    grid: list[list[str]],
    highlights: dict[tuple[int, int], str],
    rgb_map: dict[str, tuple[int, int, int]],
    output_path: str,
) -> None:
    from PIL import Image, ImageDraw, ImageFont

    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    cell = 28
    pad = 20
    width = cols * cell + pad * 2
    height = rows * cell + pad * 2

    img = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except Exception:
        font = ImageFont.load_default()

    for r in range(rows):
        for c in range(cols):
            x = pad + c * cell + cell // 2
            y = pad + r * cell + cell // 2
            ch = grid[r][c].upper()
            bbox = draw.textbbox((0, 0), ch, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
            draw.text((x - w // 2, y - h // 2), ch, fill=(0, 0, 0), font=font)

    radius = cell // 2 - 2
    for (r, c), word in highlights.items():
        x = pad + c * cell + cell // 2
        y = pad + r * cell + cell // 2
        color = rgb_map[word]
        draw.ellipse(
            (x - radius, y - radius, x + radius, y + radius),
            outline=color,
            width=2,
        )

    img.save(output_path)


def Crossword() -> None:
    # ANSI colors: cycle through distinct colors for different words
    ansi_palette = [
        "\x1b[1;33m",  # yellow
        "\x1b[1;36m",  # cyan
        "\x1b[1;35m",  # magenta
        "\x1b[1;32m",  # green
        "\x1b[1;31m",  # red
        "\x1b[1;34m",  # blue
    ]
    rgb_palette = [
        (255, 193, 7),   # yellow
        (0, 188, 212),   # cyan
        (156, 39, 176),  # magenta
        (76, 175, 80),   # green
        (244, 67, 54),   # red
        (63, 81, 181),   # blue
    ]
    color_map = {
        word: ansi_palette[i % len(ansi_palette)]
        for i, word in enumerate(words_to_find)
    }
    rgb_map = {
        word: rgb_palette[i % len(rgb_palette)]
        for i, word in enumerate(words_to_find)
    }

    positions_by_word: dict[str, list[tuple[int, int]]] = {}
    highlight_cells: dict[tuple[int, int], str] = {}
    for word in words_to_find:
        matches = _find_word_positions(crossword, word)
        if matches:
            # Use the first match for that word
            positions_by_word[word] = matches[0]
            for pos in matches[0]:
                highlight_cells[pos] = word

    _print_highlighted(crossword, highlight_cells, color_map)
    _render_to_image(crossword, highlight_cells, rgb_map, output_image_path)
    for word in words_to_find:
        if word not in positions_by_word:
            print(f"'{word}' not found.")
    
if __name__ == "__main__":
    Crossword()




