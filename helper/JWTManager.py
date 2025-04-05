import jwt
import os
import datetime
from typing import Union


class JWTManager:
    def __init__(self):
        self.__secret_key = os.getenv("TOKEN_SECRET")
        self.__algorithm = os.getenv("ACCESS_TOKEN_VALIDITY", "HS256") #Default HS256
        self.__access_token_validity = int(os.getenv("ACCESS_TOKEN_VALIDITY", 300))  # Default to 5 minutes
        self.__refresh_token_validity = int(os.getenv("REFRESH_TOKEN_VALIDITY", 43200))  # Default to 12 hours

    def create_access_token(self, payload: dict) -> str:
        payload = payload.copy()
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.__access_token_validity)
        payload["exp"] = expiration_time
        return jwt.encode(payload, self.__secret_key, algorithm=self.__algorithm)

    def create_refresh_token(self, payload: dict) -> str:
        payload = payload.copy()
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.__refresh_token_validity)
        payload["exp"] = expiration_time
        return jwt.encode(payload, self.__secret_key, algorithm=self.__algorithm)

    def verify(self, token: str) -> Union[dict, str, bool]:
        """
        veriy token if success return object or return false
        """
        try:
            return jwt.decode(token, self.__secret_key, algorithms=[self.__algorithm])
        except jwt.ExpiredSignatureError:
            return False


# how to use this class
if __name__ == "__main__":
    jwt_manager = JWTManager()

    user_data = {"user_id": 123, "role": "admin"}
    access_token = jwt_manager.create_access_token(user_data)
    refresh_token = jwt_manager.create_refresh_token(user_data)
    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)

    decoded = jwt_manager.verify(access_token)
    if decoded:
        print("Decoded Data:", decoded)