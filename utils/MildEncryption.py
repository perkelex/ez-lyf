from cryptography.fernet import Fernet, InvalidToken

key = b'GOjd51gSWjfBNpu415vqFgTHLEzIoefRwQfxfk3ZX68='
f = Fernet(key)

def hide(secret: str) -> str:
    return f.encrypt(secret.encode("utf-8")).decode("utf-8")

def reveal(hidden_secret: str) -> str:
    return f.decrypt(hidden_secret.encode("utf-8"), None).decode("utf-8")

def isValidToken(token: str) -> bool:
    try:
        reveal(token)
    except InvalidToken:
        return False
    return True