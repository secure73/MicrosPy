from interface.IController import IController
from model.AutoModel import AutoModel
from helper.Response import Response

class AutoController(IController):
    def __init__(self):
        pass
    
    def get(self,data):
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
    
    def post(self, data):  
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
    

