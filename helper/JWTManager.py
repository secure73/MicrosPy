import jwt
import datetime
from typing import Union

class JWTManager:
    def __init__(self):

        self.__secret_key = "some secret key like $edfukh6D6&fsidksjBxxcdksTaQ"
        self.__algorithm = "HS256"
        self.__expiration_minutes = 60 #in future you can use .env data to manage this more dynamically

    def create(self, payload: dict) -> str:
        payload = payload.copy()  # Avoid modifying the original payload
        expiration_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(self.__expiration_minutes)
        payload["exp"] = expiration_time
        return jwt.encode(payload, self.__secret_key, algorithm=self.__algorithm)

    def verify(self, token: str) -> Union[dict, str]|False:
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
    token = jwt_manager.create(user_data)
    print("Generated Token:", token)

    decoded = jwt_manager.verify(token)
    if decoded:
        print("Decoded Data:", decoded)