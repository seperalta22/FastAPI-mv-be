from jwt import encode, decode


def create_token(data: dict, secret: str):
    token:str = encode(payload=data, key="secret", algorithm="HS256")
    return token
