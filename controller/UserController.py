from interface.IController import IController
from model.UserModel import UserModel
from helper.Response import Response

class UserController(IController):
    def __init__(self):
        pass
    
    def get(self,data):
        return Response.success(data)
    
    def post(self, data):
        
        #return Response.success(data)
        userModel = UserModel()
        
        created = userModel.create(data["email"], data["password"], data["name"])
        if not created: 
            return Response.bad_request(f"Failed to create user {userModel.error}")
        return Response.success({"success": "User created successfully"})
    
    def destroy(self, data):
        model = UserModel()
        result = model.remove(data.get("id"))  # Fixed: `id` was missing from input
        if not result:
            return Response.bad_request("Failed to destroy user")
        return Response.success({"success": "User destroyed successfully"})
    
    def put(self, data):
        return Response.bad_request(data)
