import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha1(password.encode("utf-8")).hexdigest()

def verify_password(password: str, stored_hash: str) -> bool:
    return hash_password(password) == stored_hash

# Example usage:
# stored = hash_password("secret123")
# verify_password("secret123", stored)

