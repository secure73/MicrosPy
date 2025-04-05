from interface.IController import IController
from model.AutoModel import AutoModel
from helper.Response import Response
from helper.AuthController import AuthController

class AutoController(AuthController, IController):
    def __init__(self):
        super().__init__()
    
    def get(self, data, headers):
        decoded = self.authenticate(headers)
        if isinstance(decoded, dict) and "status_code" in decoded:
            return decoded  # Return error response if authentication fails

        autoModel = AutoModel()
        if data.get("id"):
            result = autoModel.single(data["id"])
            if not result:
                return Response.bad_request(f"Failed to get auto {autoModel.error}")
            return Response.success(result)
        result = autoModel.list()
        if not result:
            return Response.bad_request(f"Failed to get autos {autoModel.error}")
        return Response.success(result)
    
    def post(self, data, headers):
        # Authenticate the user
        decoded = self.authenticate(headers)
        if isinstance(decoded, dict) and "status_code" in decoded:
            return decoded  # Return error response if authentication fails

        # Authorize the user for admin role
        auth_result = self.authorize(decoded, required_role="admin")
        if isinstance(auth_result, dict) and "status_code" in auth_result:
            return auth_result  # Return error response if authorization fails

        autoModel = AutoModel()
        created = autoModel.create(data["name"], data["ps"])
        if not created:
            return Response.bad_request(f"Failed to create auto {autoModel.error}")
        return Response.success({"success": "Auto created successfully"})
    
    def destroy(self, data):
        model = AutoModel()
        # Handle both string and dict data types
        auto_id = data.get("id") if isinstance(data, dict) else data
        
        if auto_id is None:
            return Response.bad_request("Missing auto ID")
            
        try:
            auto_id = int(auto_id)
        except (ValueError, TypeError):
            return Response.bad_request("Invalid auto ID format")
            
        result = model.remove(auto_id)
        if not result:
            return Response.bad_request(model.error or "Failed to destroy auto")
        return Response.success({"success": f"Auto with ID {auto_id} destroyed successfully"})
    
    def put(self, data):
        autoModel = AutoModel() 
        updated = autoModel.update(data["id"], data["name"], data["ps"])
        if not updated:
            return Response.bad_request(f"Failed to update auto {autoModel.error}")
        return Response.success({"success": "Auto updated successfully"})
    

