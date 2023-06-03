from jwt import encode, decode
from jwt.exceptions import InvalidTokenError


def create_token(data: dict):
    token:str = encode(payload=data, key="secret", algorithm="HS256")
    return token



def validate_token(token: str) -> dict:
    try:
        data: dict = decode(token, key="secret", algorithms=["HS256"])
        return data if data["username"] else None
    except InvalidTokenError:
        return {}
