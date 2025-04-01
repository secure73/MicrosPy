import json
import importlib
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from typing import Any, Optional

"""
Note: This class is not suitable for production.

It is designed solely for educational purposes to demonstrate how HTTP requests work. 
There are several areas that could be cleaner, more optimized, and more secure for a production-level application.

This class is intended for beginners to understand the HTTP request lifecycle and gain insights into 
how robust frameworks like Flask and Django handle requests efficiently.
"""

class HttpHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self._handle_request("GET")
    
    def do_POST(self):
        self._handle_request("POST")
    
    def do_PUT(self):
        self._handle_request("PUT")
    
    def do_DELETE(self):
        self._handle_request("DELETE")
    
    def do_OPTIONS(self):
        self._handle_request("OPTIONS")

    def _handle_request(self, method_HTTP):
        validation_result = self._validateRequestParts(method_HTTP)

        if isinstance(validation_result, dict):  # Error case
            return self._send_response(400, validation_result)

        controller_name, query_params = validation_result  # Unpack

        try:
            controller_instance = self._createInstance(controller_name)
            if not controller_instance:
                return self._send_response(404, {"error": f"Controller '{controller_name}' not found."})

            method_map = {
                "POST": "post",
                "PUT": "put",
                "DELETE": "destroy",
                "GET": "get",
                "OPTIONS": "options"
            }

            method_name = method_map.get(method_HTTP, "get")
            method_to_call = self._createMethod(controller_instance, method_name)

            if not method_to_call:
                return self._send_response(404, {"error": f"Method '{method_name}' not found in '{controller_name}'."})
            data = None
            if method_HTTP == "GET":
                data = query_params
            else:
                data = self._load_data(method_HTTP)
            
            response_data = method_to_call(data)
            status_code = response_data.get("status_code", 200)
            return self._send_response(status_code, response_data)
        
        except Exception as e:
            return self._send_response(500, {"error": str(e)})

    def _validateRequestParts(self, method_HTTP):
        path_parts = self.path.strip('/').split('/')
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if len(path_parts) < 1:
            return {"error": "Invalid request. Use /Controller or /Controller?id=value"}

        controller_name = path_parts[0].capitalize() + "Controller"

        # Handle GET requests with optional ID
        if method_HTTP == "GET" and len(path_parts) > 1 and path_parts[1].isdigit():
            query_params["id"] = path_parts[1]

        return controller_name, query_params

    def _createInstance(self, controller_name):
        try:
            module = importlib.import_module(f'controller.{controller_name}')
            controller_class = getattr(module, controller_name, None)
            if controller_class is None:
                return None
            return controller_class()
        except ImportError:
            return None

    def _createMethod(self, controller_instance, method_name) -> Optional[Any]:
        return getattr(controller_instance, method_name, None)

    def _send_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def _load_data(self, HTTP_method):
        if HTTP_method in ["POST", "PUT"]:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            try:
                return json.loads(post_data)
            except json.JSONDecodeError:
                return {"error": "Invalid JSON format"}
        return None


def run(port=8001):
    server_class = HTTPServer
    handler_class = HttpHandler
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()
