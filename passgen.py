import hashlib
def generate_password_hash(password: str) -> str:
    """Generate a SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()
def verify_password_hash(password: str, password_hash: str) -> bool:
    """Verify the given password against the stored hash."""
    return generate_password_hash(password) == password_hash
def main():
    password = input("Enter a password to hash: ")
    password_hash = generate_password_hash(password)
    print(f"Generated password hash: {password_hash}")
    
    verify = input("Enter the password again to verify: ")
    if verify_password_hash(verify, password_hash):
        print("Password verification successful.")
    else:
        print("Password verification failed.")
if __name__ == "__main__":
    main()
# This script provides functions to generate and verify password hashes using SHA-256.
# It includes a main function to demonstrate usage.
# The `generate_password_hash` function takes a password string and returns its SHA-256 hash.
# The `verify_password_hash` function checks if a given password matches the stored hash.
# The script prompts the user to enter a password, generates its hash, and then verifies it by asking for the password again.
# The main function is executed when the script is run directly.
