import argon2

def verify_password(hash: str, password: str) -> bool:
    ph = argon2.PasswordHasher()
    try:
        return ph.verify(hash, password)
    except argon2.exceptions.VerifyMismatchError:
        return False

def hash_password(password: str) -> str:
    ph = argon2.PasswordHasher()
    return ph.hash(password)
