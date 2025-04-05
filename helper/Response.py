class Response:
    @staticmethod
    def response(status_code, data):
        return {
            "status_code": status_code,
            "status": "error" if status_code >= 400 else "success",
            "message": data
        }


    @staticmethod
    def success(data):
        return Response.response(200, data)
    
    @staticmethod
    def created(data):
        return Response.response(201, data)

    @staticmethod
    def no_content():
        return Response.response(204, None)

    @staticmethod
    def not_found(message):
        return Response.response(404, message)

    @staticmethod
    def conflict(message):
        return Response.response(409, message)
    
    @staticmethod
    def bad_request(message):
        return Response.response(400, message)
    
    @staticmethod
    def deleted(message):
        return Response.response(202, message)
    
    @staticmethod
    def forbidden(message):
        return Response.response(403, message)

    @staticmethod
    def unauthorized(message):
        return Response.response(401, message)

    @staticmethod
    def internal_error(message):
        return Response.response(500, message)
