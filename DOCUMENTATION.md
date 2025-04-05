# Micro Python Framework Documentation

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Project Structure](#project-structure)
- [Simple CRUD Example](#simple-crud-example)
- [Authentication and Authorization](#authentication-and-authorization)
- [VS Code Integration and Copilot Configuration](#vs-code-integration-and-copilot-configuration)
- [Database](#database)
- [Error Handling](#error-handling)
- [Development Guidelines](#development-guidelines)
- [Request Lifecycle and Flow](#request-lifecycle-and-flow)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Additional Information](#additional-information)

## Overview
This is a minimal micro-framework designed **exclusively for educational purposes** to help beginners understand the fundamentals of Python and RESTful API development. It implements a simple MVC (Model-View-Controller) architecture and provides basic RESTful API functionality.

> ⚠️ **Important Note**: This framework is **NOT suitable for production use**. It is designed solely as a learning tool to help you understand:
> - How frameworks like Django and FastAPI work under the hood
> - Python OOP principles and design patterns
> - Layered architecture and separation of concerns
> - Basic REST API principles and HTTP request handling
> - Database operations and ORM concepts
> - Basic MVC architecture implementation

> ⚠️ **Framework Independence Warning**: This is a custom framework with its own patterns and architecture. Do NOT mix it with Flask, Django, FastAPI or other web frameworks as this will cause conflicts and errors. All code should use only the classes and patterns defined within this framework.

> ⚠️ **Security Warning**: This framework has **minimal security implementations** and should never be used in production environments. It lacks:
> - Proper authentication and authorization
> - Input sanitization
> - CSRF protection
> - Rate limiting
> - Production-grade error handling
> - Security headers
> - And many other essential security features

This framework serves as an excellent first step for learning REST API principles and understanding how web frameworks are structured, but it should be treated as a learning tool rather than a production-ready solution.

## Prerequisites
- Python 3.13.2 or higher
- Virtual environment (recommended)

## Installation and Setup

> ⚠️ **Important**: Always create and activate the virtual environment immediately after cloning the repository and before installing any dependencies. This ensures a clean, isolated environment for your project.

1. Clone the repository:
   ```bash
   git clone https://github.com/secure73/micro_py_framework.git
   ```

2. Go to your cloned local folder:
   ```bash
   cd micro_py_framework
   ```

3. Create and activate virtual environment inside project directory:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python -m venv venv
   source venv/bin/activate

   # Verify activation (should show virtual environment path)
   # Windows: where python
   # Linux/Mac: which python
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure the environment variables:
   ```bash
   # Windows
   copy .env.example .env
   
   # Linux/Mac
   cp .env.example .env
   ```
   
   Here's what your `.env` file should contain:
   ```
   # JWT Configuration
   TOKEN_SECRET=your_secret_key_here
   ACCESS_TOKEN_VALIDITY=300
   REFRESH_TOKEN_VALIDITY=43200
   JWT_ALGORITHM=HS256
   
   # Database Configuration
   DB_HOST=sqlite:///db.db
   DB_USER=
   DB_PASSWORD=
   DB_NAME=
   DB_PORT=
   ```

6. Run database migration:
   ```bash
   python migrate.py
   ```

7. Start the application:
   ```bash
   python app.py   # Server will start on port 8001
   ```

### Troubleshooting Virtual Environment
1. **Virtual environment not activating**:
   - Check Python installation
   - Ensure execution policy allows scripts (Windows)
   - Try creating a new virtual environment

2. **Package installation fails**:
   - Verify virtual environment is activated
   - Check internet connection
   - Update pip: `python -m pip install --upgrade pip`

3. **Wrong Python version**:
   - Delete the virtual environment
   - Create new one with correct Python version
   - Reinstall dependencies

## Project Structure
```
micro_py_framework/
├── app.py                 # Main application entry point
├── controller/            # Controllers directory
│   ├── UserController.py  # User-related operations
│   └── AutoController.py  # Auto-related operations
├── model/                # Models directory
│   ├── UserModel.py      # User data operations
│   └── AutoModel.py      # Auto data operations
├── table/                # Database tables
│   ├── DBConnection.py   # Database connection management
│   ├── DBMigrate.py      # Database migration and schema
│   ├── UserTable.py      # User table schema
│   └── AutoTable.py      # Auto table schema
├── interface/            # Interfaces directory
│   └── IController.py    # Controller interface
├── helper/              # Helper utilities
│   ├── HttpHandler.py    # HTTP request handler
│   ├── Response.py       # Response formatting
│   ├── JWTManager.py     # JWT authentication
│   ├── AuthController.py # Authentication & authorization controller
│   ├── FormatCheck.py    # Input validation
│   ├── CodeAssistant.py  # AI-powered code generation
│   └── DatabaseMigration.py  # Database migration helper
└── .env                 # Environment variables configuration file
```

## Simple CRUD Example

### Creating a Simple CRUD Controller

The framework provides a simple way to create CRUD (Create, Read, Update, Delete) operations. Here's a walkthrough of using the Auto controller as an example.

#### Auto Controller Endpoints

1. **Create Auto**
   - Method: POST
   - URL: `/auto`
   - Request Body:
     ```json
     {
         "name": "Mercedes Benz",
         "ps": 750
     }
     ```
   - Response: Success message or error details
   - Example:
     ```bash
     curl -X POST http://localhost:8001/auto \
       -H "Content-Type: application/json" \
       -d '{"name": "Mercedes Benz", "ps": 750}'
     ```

2. **Get Auto(s)**
   - Method: GET
   - URL: `/auto` (list all autos)
   - URL: `/auto/{id}` (get specific auto)
   - Response: Auto data or error message
   - Example:
     ```bash
     # Get all autos
     curl http://localhost:8001/auto
     
     # Get specific auto
     curl http://localhost:8001/auto/1
     ```

3. **Update Auto**
   - Method: PUT
   - URL: `/auto`
   - Request Body:
     ```json
     {
         "id": 1,
         "name": "Updated Name",
         "ps": 800
     }
     ```
   - Response: Updated auto data or error message
   - Example:
     ```bash
     curl -X PUT http://localhost:8001/auto \
       -H "Content-Type: application/json" \
       -d '{"id": 1, "name": "Updated Name", "ps": 800}'
     ```

4. **Delete Auto**
   - Method: DELETE
   - URL: `/auto`
   - Request Body:
     ```json
     {
         "id": 1
     }
     ```
   - Response: Success message or error details
   - Example:
     ```bash
     curl -X DELETE http://localhost:8001/auto \
       -H "Content-Type: application/json" \
       -d '{"id": 1}'
     ```

### Data Validation for Auto Model

- Name: Minimum 2 characters
- PS (horsepower): Must be a positive integer

### Response Format
All API responses follow a consistent format:

#### Success Response
```json
{
    "status_code": 200,
    "status": "success",
    "message": {
        // Response data
    }
}
```

#### Error Response
```json
{
    "status_code": 400,
    "status": "error",
    "message": "Error description"
}
```

## Authentication and Authorization

### JWT Authentication Setup

1. **Setting up JWT Environment Variables**
   - The framework uses environment variables for JWT configuration
   - Required variables in `.env` file:
     ```
     TOKEN_SECRET=your_secret_key_here
     ACCESS_TOKEN_VALIDITY=300
     REFRESH_TOKEN_VALIDITY=43200
     ```
   - `TOKEN_SECRET`: Your secret key for signing tokens
   - `ACCESS_TOKEN_VALIDITY`: Validity period in seconds for access tokens (default: 300 seconds / 5 minutes)
   - `REFRESH_TOKEN_VALIDITY`: Validity period in seconds for refresh tokens (default: 43200 seconds / 12 hours)

2. **Creating User Authentication Tokens**
   The following example shows how to generate authentication tokens after user login:

   ```python
   from helper.JWTManager import JWTManager
   from helper.Response import Response
   from model.UserModel import UserModel

   class AuthLoginController(IController):
       def __init__(self):
           self.model = UserModel()
           self.jwt_manager = JWTManager()
       
       def post(self, data):
           # Extract login credentials
           email = data.get('email')
           password = data.get('password')
           
           if not email or not password:
               return Response.bad_request("Email and password are required")
           
           # Validate user credentials
           user = self.model.get_by_email(email)
           
           if not user:
               return Response.not_found("User not found")
           
           # Verify password
           if not self.model.verify_password(password, user.password):
               return Response.unauthorized("Invalid credentials")
           
           # Create user data for token
           user_data = {
               "user_id": user.id,
               "role": user.role  # Assuming user has a role field
           }
           
           # Generate tokens
           access_token = self.jwt_manager.create_access_token(user_data)
           refresh_token = self.jwt_manager.create_refresh_token(user_data)
           
           # Return tokens to client
           return Response.success({
               "access_token": access_token,
               "refresh_token": refresh_token,
               "user": {
                   "id": user.id,
                   "name": user.name,
                   "email": user.email,
                   "role": user.role
               }
           })
   ```

3. **Using Tokens for Authentication**
   To use the generated token in requests, include it in the Authorization header:
   ```bash
   curl -X GET http://localhost:8001/resource \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
   ```

### Creating an Authenticated Controller

The `AuthController` class provides a simple way to add authentication and authorization to your controllers:

1. **Create an Authenticated Controller**
   ```python
   from helper.AuthController import AuthController
   from interface.IController import IController
   from helper.Response import Response
   from model.ProductModel import ProductModel

   class ProductController(AuthController, IController):
       def __init__(self):
           super().__init__()
           self.model = ProductModel()
           
       def get(self, data, headers):
           # Authenticate the request
           decoded = self.authenticate(headers)
           if isinstance(decoded, dict) and "status_code" in decoded:
               return decoded  # Return error response if authentication fails
               
           # Get all products or specific product by ID
           if "id" in data:
               product = self.model.get_by_id(data["id"])
               if product:
                   return Response.success(product)
               return Response.not_found("Product not found")
           
           products = self.model.get_all()
           return Response.success(products)
           
       def post(self, data, headers):
           # Authenticate the user
           decoded = self.authenticate(headers)
           if isinstance(decoded, dict) and "status_code" in decoded:
               return decoded
           
           # Authorize for admin role only
           auth_result = self.authorize(decoded, required_role="admin")
           if isinstance(auth_result, dict) and "status_code" in auth_result:
               return auth_result
           
           # Create new product
           name = data.get("name")
           price = data.get("price")
           
           if not name or not price:
               return Response.bad_request("Name and price are required")
           
           result = self.model.create(name=name, price=price)
           return Response.success(result)
           
       # Similar implementation for put and destroy methods
   ```

2. **Accessing User Information**
   After successful authentication, user information is available in the controller:
   ```python
   # User ID from the token
   user_id = self.user_id
   
   # User role from the token
   role = self.role
   ```

3. **Role-Based Access Control**
   ```python
   # Authorize for specific role
   auth_result = self.authorize(decoded, required_role="admin")
   if isinstance(auth_result, dict) and "status_code" in auth_result:
       return auth_result
   ```

## VS Code Integration and Copilot Configuration

### VS Code Integration

The framework includes VS Code integration features:
1. Custom snippets for quick code generation:
   - Controller snippets (`micro_py_controller_basic`)
   - Authenticated controller snippets (`micro_py_authenticated_controller_basic`)
   - Model snippets (`micro_py_model_basic`)
   - Table snippets (`micro_py_table_basic`)
2. IntelliSense support for framework components
3. Recommended extensions for Python development
4. Automatic code formatting with Black
5. Linting with Pylint
6. Import organization
7. Documentation generation support

When installed, these snippets will be available in your VS Code environment, making it easier to create new components that follow the framework's patterns. VS Code will save these snippets to your home directory under `.vscode/snippets/`.

### Training GitHub Copilot

The framework includes a special tool to help train GitHub Copilot to generate code that follows the correct micro_py_framework patterns instead of suggesting Flask, Django, or other frameworks.

1. **Run the Copilot Trainer**
   ```bash
   python copilot_trainer.py
   ```
   This script will:
   - Generate multiple example files following the correct framework patterns
   - Create anti-pattern examples showing what NOT to do
   - Provide effective comments to guide Copilot
   - Open these files in VS Code (if available)

2. **Working with Generated Reference Files**
   - Keep the generated reference files open in a separate VS Code window
   - When working on your project, Copilot will use these as context
   - Example resources include Product, Order, Customer, Category, and Inventory
   - Both standard and authenticated controller versions are provided

3. **Using Comments to Guide Copilot**
   Use specific comments to help Copilot generate the correct code:
   ```python
   # Create a new controller for Products following micro_py_framework patterns
   ```
   Instead of vague comments like:
   ```python
   # Create a new controller for products
   ```

4. **Anti-Patterns to Reject**
   The trainer includes examples of Flask and Django patterns that should be rejected:
   - Flask's `@app.route` decorators
   - Django's `models.Model` base class
   - Function-based API routes
   - Any imports from external web frameworks

5. **VS Code Integration**
   - The tool attempts to open VS Code with the reference files
   - Follow the TRAINING_GUIDE.md document for best practices
   - Keep these files open when working with Copilot

> ⚠️ **Framework Purity Warning**: When using AI assistants like GitHub Copilot, ChatGPT, or similar tools, they may suggest Flask, Django, or other framework patterns which are NOT compatible with this framework. Always ensure generated code follows the micro_py_framework patterns as shown in the examples.

## Database

### Database Migration and Table Creation

1. **Migration Process**
   The framework provides a simple migration system to create and update database tables:
   ```bash
   python migrate.py
   ```

2. **Migration Features**
   - Automatic table discovery and creation
   - Column change detection
   - Migration status tracking
   - Clear progress indicators with emojis
   - Detailed migration summary
   - Example output:
     ```
     🚀 Starting database migration...
     📝 Creating table: users
     📝 Creating table: autos
     
     ✅ Tables created successfully:
       - users
       - autos
     
     === Migration Summary ===
     📦 Created Tables:
       ✓ users
       ✓ autos
     
     ✨ Migration process completed!
     ```

3. **Creating New Tables**
   After creating any new Table Class (e.g., ProductTable.py), simply run migrate.py again to update the database schema.

### Database Configuration with Environment Variables

1. **Configuration in .env File**
   - The application uses environment variables for database configuration
   - Database connection settings are defined in the `.env` file
   - Example configuration for different database types:
     ```
     # SQLite (Default)
     DB_HOST=sqlite:///db.db
     
     # MySQL/MariaDB
     DB_HOST=mysql+pymysql://username:password@localhost:3306/database_name
     ```

2. **Database Connection Management (DBConnection.py)**
   The `DBConnection.py` file manages database connections using SQLAlchemy ORM. It provides:
   - SQLAlchemy Integration for Object-Relational Mapping (ORM)
   - Connection Configuration through environment variables
   - Session Management for database operations
   - Support for SQLite and MySQL/MariaDB
   - Error Handling for database connection failures

3. **Usage in Models**
   ```python
   from table.DBConnection import DBConnection
   
   class YourModel:
       def __init__(self):
           self.Session = DBConnection.Session
   ```

## Error Handling

The framework includes comprehensive error handling for:
- Invalid input data
- Database operations
- HTTP request validation
- Resource not found
- Data type validation
- Missing required fields

### Input Validation
The framework includes a FormatCheck utility for validating input data:

1. **Email Validation**
   ```python
   FormatCheck.email("user@example.com")
   ```

2. **Length Validation**
   ```python
   FormatCheck.minimumLength("password", 6)
   ```

3. **Usage Examples**
   ```python
   # Email validation
   if not FormatCheck.email(user_email):
       return Response.bad_request("Invalid email format")

   # Password length check
   if not FormatCheck.minimumLength(password, 6):
       return Response.bad_request("Password must be at least 6 characters")
   ```

## Development Guidelines

### Creating New Controllers
1. Create a new file in the `controller` directory
2. Implement the `IController` interface
3. Add your controller methods (get, post, put, destroy)

### Creating New Models
1. Create a new file in the `model` directory
2. Implement the `IModel` interface
3. Create corresponding table in `table` directory
4. Implement database operations

### Controller Patterns
The framework supports two main controller patterns:

1. **Standard Controller Pattern**
   ```python
   from interface.IController import IController
   from helper.Response import Response
   from model.ProductModel import ProductModel

   class ProductController(IController):
       def __init__(self):
           self.model = ProductModel()

       def get(self, data):
           # Implementation...
       
       def post(self, data):
           # Implementation...
       
       def put(self, data):
           # Implementation...
       
       def destroy(self, data):
           # Implementation...
   ```

2. **Authenticated Controller Pattern**
   ```python
   from helper.AuthController import AuthController
   from interface.IController import IController
   from helper.Response import Response
   from model.OrderModel import OrderModel

   class OrderController(AuthController, IController):
       def __init__(self):
           super().__init__()
           self.model = OrderModel()

       def get(self, data, headers):
           # Authenticate the user
           decoded = self.authenticate(headers)
           if isinstance(decoded, dict) and "status_code" in decoded:
               return decoded  # Return error response if authentication fails
           
           # Implementation...
       
       # Other methods with authentication...
   ```

## Request Lifecycle and Flow

### General Request Flow
```mermaid
graph TD
    A[Client Request] --> B[HttpHandler]
    B --> C{Request Validation}
    C -->|Valid| D[Route to Controller]
    C -->|Invalid| E[Return 400 Error]
    D --> F1{Authentication Required?}
    F1 -->|Yes| F2[Check Authorization Header]
    F2 -->|Valid Token| F3[Decode & Extract User Info]
    F2 -->|Invalid/Missing Token| F4[Return 403 Forbidden]
    F3 -->|Required Role Check| F5{Has Required Role?}
    F5 -->|Yes| F[Execute Controller Method]
    F5 -->|No| F6[Return 403 Forbidden]
    F1 -->|No| F[Execute Controller Method]
    F --> G[Process Model Operations]
    G --> H[Database Operations]
    H --> I[Format Response]
    I --> J[Send Response to Client]
```

### Authenticated Request Flow
```mermaid
sequenceDiagram
    participant Client
    participant HttpHandler
    participant AuthController
    participant JWTManager
    participant Controller
    participant Model
    participant Database

    Client->>HttpHandler: Request with Authorization header
    HttpHandler->>Controller: Route with headers
    Controller->>AuthController: authenticate(headers)
    AuthController->>AuthController: Extract token from Bearer
    AuthController->>JWTManager: verify(token)
    JWTManager-->>AuthController: decoded token or false
    
    alt Invalid Token
        AuthController-->>Controller: Forbidden response
        Controller-->>HttpHandler: 403 Response
        HttpHandler-->>Client: Forbidden
    else Valid Token
        AuthController-->>Controller: decoded token data
        
        opt Role-Based Check
            Controller->>AuthController: authorize(token, required_role)
            alt Insufficient Permissions
                AuthController-->>Controller: Forbidden response
                Controller-->>HttpHandler: 403 Response
                HttpHandler-->>Client: Forbidden
            else Authorization OK
                AuthController-->>Controller: true
                Controller->>Model: Database operation
                Model->>Database: Execute query
                Database-->>Model: Result
                Model-->>Controller: Processed data
                Controller-->>HttpHandler: 200 OK
                HttpHandler-->>Client: Success Response
            end
        end
    end
```

## Best Practices
1. Always use virtual environment
2. Keep controllers thin, move business logic to models
3. Validate input data before processing
4. Handle database errors appropriately
5. Use proper HTTP status codes in responses
6. Follow consistent error handling patterns
7. Use type hints for better code clarity
8. Document API endpoints and their requirements
9. **DO NOT mix with Flask, Django or other frameworks** - this framework uses its own patterns

## Troubleshooting
1. If database connection fails:
   - Check if database file exists
   - Verify database credentials (if using MySQL)
   - Check database permissions

2. If server fails to start:
   - Check if port 8001 is available
   - Verify all dependencies are installed
   - Check Python version compatibility

3. If requests fail:
   - Verify request format
   - Check input validation rules
   - Ensure proper HTTP method is used
   - Verify content-type header is set correctly
   - Check if required fields are provided

## Additional Information

### AI Assistant Features

The framework includes an intelligent code assistant that can help you with:
- Generating CRUD endpoints
- Providing code suggestions
- Generating documentation
- Analyzing your codebase
- Creating authenticated controllers with role-based access control

To use the AI Assistant:

1. **Run the AI Assistant Demo**
   ```bash
   python ai.py
   ```
   This will show you examples of what the assistant can do.

2. **Using the Generated Code**
   The demo generates complete code examples that you can:
   - Copy and use in your own controllers
   - Use as templates for new resources
   - Study to understand the framework patterns

3. **Generating Secure Authenticated Controllers**
   ```python
   # Example: Generate an authenticated controller
   authenticated_code = assistant.generate_crud_endpoints_with_auth("Resource")
   print(authenticated_code['controller'])
   ```

### Postman Collection
The framework includes a Postman collection that contains pre-configured requests for example API endpoints.

1. **Importing the Collection**
   - Open Postman
   - Click "Import" in the top-left corner
   - Select "File" tab
   - Click "Upload Files" and select `Micro Python.postman_collection.json`
   - Click "Import"

2. **Using the Collection**
   The collection includes pre-configured requests for all auto endpoints (GET, POST, PUT, DELETE)

### Environment Variables

The framework automatically loads the `.env` file in `app.py`:
```python
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
```

To access environment variables in your code:
```python
import os

# After load_dotenv() has been called in app.py
secret_key = os.getenv("TOKEN_SECRET")
```

### A Note from the Developer

Thank you for taking the time to explore this educational framework! I created this project to help beginners understand the fundamental concepts of web development and Python programming.

I hope this framework serves as a helpful stepping stone in your learning journey. Remember that every expert was once a beginner, and the key to mastering programming is consistent practice and curiosity.

Best wishes for your learning journey!

Ali Khorsandfard
Developer & Educator