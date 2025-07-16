import hashlib
def generate_password_hash(password: str) -> str:
    """Generate a SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()
def verify_password_hash(password: str, password_hash: str) -> bool:
    """Verify the given password against the stored hash."""
    return generate_password_hash(password) == password_hash