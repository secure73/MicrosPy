from helper.JWTManager import JWTManager
from helper.Response import Response

class AuthController:
    """
    This class is used to authenticate and authorize users
    """
    role = None
    user_id = None
    def __init__(self):
        self.jwt_manager = JWTManager()

    def authenticate(self, headers):
        auth_header = headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response.forbidden("Authorization header missing or malformed")

        # Extract the token from the header
        token = auth_header.split(' ')[1]
        decoded = self.jwt_manager.verify(token)
        if not decoded:
            return Response.forbidden("Invalid or expired token")
        self.role = decoded.get("role")
        self.user_id = decoded.get("user_id")
        return decoded

    def authorize(self, decoded_token, required_role=None):
        user_role = decoded_token.get("role")
        if required_role and user_role != required_role:
            return Response.forbidden("Insufficient permissions")

        self.user_id = decoded_token.get("user_id")
        self.role = decoded_token.get("role")
        return True
