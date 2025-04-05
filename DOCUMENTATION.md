# Micro Python Framework Documentation

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
2. go to your cloned local folder for example micro_py_framework is your local target directory where repository is cloned:
   ```bash
   cd micro_py_framework
   ```

4.  ⚠️ **Important** Create and activate virtual environment inside project directory(IMPORTANT - do this immediately after cloning):
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

5. Install dependencies to set up the application:
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   ```

6. Configure the environment variables:
   ```bash
   # Rename .env.example to .env
   # Windows
   copy .env.example .env
   
   # Linux/Mac
   cp .env.example .env
   
   # Then edit the .env file with your configuration
   # At minimum, set TOKEN_SECRET for JWT authentication
   ```
   
   > ⚠️ **Important**: The project includes an `.env.example` file that you should rename to `.env`. This file contains template environment variables that you should customize for your setup.
   
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

7. Migrate Database for sample Database:
   ```bash
   # Run database migration
   python migrate.py
   ```
8. Run App:
   ```bash
   # Start the application
   python app.py   # Server will start on port 8001
   ```

### Database Migration And Create New Table in Your Database(migrate.py)
   - easily and anytime after Creating any Table Class Example AutoController.py , open migrate.py on the root and run it , or write python migrate.py on terminal in project root!
1. **Migration Features**
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
     
2. **Key Benefits**
   - No manual SQL writing required
   - Consistent database schema across installations
   - Automatic schema updates when models change
   - Clear feedback during migration process
   - Error detection and reporting

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

## API Endpoints

### User Controller Endpoints

1. **Create User**
   - Method: POST
   - URL: `/user`
   - Request Body:
     ```json
     {
         "email": "user@example.com",
         "password": "password123",
         "name": "John Doe"
     }
     ```
   - Response: Success message or error details

2. **Get User(s)**
   - Method: GET
   - URL: `/user` (list all users)
   - URL: `/user/{id}` (get specific user)
   - Response: User data or error message

3. **Update User**
   - Method: PUT
   - URL: `/user`
   - Request Body:
     ```json
     {
         "id": 1,
         "name": "Updated Name",
         "password": "newpassword"  // optional
     }
     ```
   - Response: Updated user data or error message

4. **Delete User**
   - Method: DELETE
   - URL: `/user`
   - Request Body:
     ```json
     {
         "id": 1
     }
     ```
   - Response: Success message or error details

### Auto Controller Endpoints

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

2. **Get Auto(s)**
   - Method: GET
   - URL: `/auto` (list all autos)
   - URL: `/auto/{id}` (get specific auto)
   - Response: Auto data or error message

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

## Data Validation

### User Data Validation Rules
- Email: Must follow standard email format
- Password: Minimum 6 characters
- Name: Minimum 2 characters

### Auto Data Validation Rules
- Name: Minimum 2 characters
- PS (horsepower): Must be a positive integer

## Database

### Configuration with Environment Variables
- The application uses environment variables for database configuration
- Database connection settings are defined in the `.env` file
- Example configuration for different database types:
  ```
  # SQLite (Default)
  DB_HOST=sqlite:///db.db
  
  # MySQL/MariaDB
  DB_HOST=mysql+pymysql://username:password@localhost:3306/database_name
  ```

### SQLite Database
- The application uses SQLite as the default database
- Database file: `db.db`
- Tables are automatically created on first run

### Database Connection Management (DBConnection.py)
The `DBConnection.py` file manages database connections using SQLAlchemy ORM. It provides:

1. **SQLAlchemy Integration**
   - Uses SQLAlchemy for Object-Relational Mapping (ORM)
   - Provides a declarative base for model definitions
   - Manages database sessions efficiently

2. **Connection Configuration**
   ```python
   # Uses the DB_HOST environment variable from .env file
   engine = create_engine(os.getenv("DB_HOST", "sqlite:///db.db"), echo=False)
   ```
   - Default configuration uses SQLite database
   - Supports MySQL/MariaDB through connection string modification in .env
   - `echo=False` disables SQL query logging for better performance

3. **Session Management**
   ```python
   Session = sessionmaker(bind=engine)
   ```
   - Creates a session factory for database operations
   - Manages database connections and transactions
   - Provides thread-safe database access

4. **Database Support**
   - **SQLite** (Default):
     ```
     DB_HOST=sqlite:///db.db
     ```
   - **MySQL/MariaDB**:
     ```
     DB_HOST=mysql+pymysql://username:password@localhost:3306/database_name
     ```
   - To change database type, simply update the DB_HOST variable in your .env file

5. **Error Handling**
   - Catches and reports database connection failures
   - Provides clear error messages for troubleshooting

6. **Usage in Models**
   ```python
   from table.DBConnection import DBConnection
   
   class YourModel:
       def __init__(self):
           self.Session = DBConnection.Session
   ```

7. **Best Practices**
   - Implements proper session management
   - Follows SQLAlchemy best practices

### MySQL Support
- The framework also supports MySQL databases
- To use MySQL, modify the connection string in `table/DBConnection.py`:
  ```python
  engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
  ```

## Error Handling
The framework includes comprehensive error handling for:
- Invalid input data
- Database operations
- HTTP request validation
- Resource not found
- Data type validation
- Missing required fields

## Security Notes
1. This is an educational framework and is not recommended for production use
2. Password hashing is implemented using bcrypt
3. Basic input validation is provided through FormatCheck.py
4. JWT authentication support is available through JWTManager.py
5. Authentication and authorization can be implemented using AuthController which provides a role-based access control system

## Authentication and Authorization

The framework now includes a robust authentication and authorization system using JWT (JSON Web Tokens) for securing API endpoints.

### JWT Authentication

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

2. **JWTManager Class**
   ```python
   from helper.JWTManager import JWTManager

   jwt_manager = JWTManager()
   
   # Create tokens
   user_data = {"user_id": 123, "role": "admin"}
   access_token = jwt_manager.create_access_token(user_data)
   refresh_token = jwt_manager.create_refresh_token(user_data)
   
   # Verify token
   decoded = jwt_manager.verify(token)
   if decoded:
       # Token is valid
       user_id = decoded.get("user_id")
       role = decoded.get("role")
   ```

### AuthController

The `AuthController` class provides a simple way to add authentication and authorization to your controllers:

1. **Setting up AuthController**
   ```python
   from helper.AuthController import AuthController
   from helper.Response import Response

   class YourController(AuthController):
       def __init__(self):
           super().__init__()
           
       def get(self, data, headers):
           # Authenticate the request
           decoded = self.authenticate(headers)
           if isinstance(decoded, dict) and "status_code" in decoded:
               return decoded  # Return error response if authentication fails
               
           # Continue with your logic
           return Response.success({"data": "Your data"})
   ```

2. **Role-Based Access Control**
   ```python
   def post(self, data, headers):
       # Authenticate the user
       decoded = self.authenticate(headers)
       if isinstance(decoded, dict) and "status_code" in decoded:
           return decoded
       
       # Authorize for specific role
       auth_result = self.authorize(decoded, required_role="admin")
       if isinstance(auth_result, dict) and "status_code" in auth_result:
           return auth_result
       
       # Continue with authorized operation
       return Response.success({"message": "Operation successful"})
   ```

3. **Accessing User Information**
   After successful authentication, user information is available in the controller:
   ```python
   # User ID from the token
   user_id = self.user_id
   
   # User role from the token
   role = self.role
   ```

### Making Authenticated Requests

1. **Using Authorization Header**
   ```bash
   curl -X GET http://localhost:8001/resource \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
   ```

2. **Example in Postman**
   - Add a header with key `Authorization` and value `Bearer YOUR_TOKEN`
   - This should be included in all requests that require authentication

## Environment Variables

The framework now supports environment variables using `python-dotenv`:

1. **Setting up environment variables**
   - Create a `.env` file in the root directory
   - Define your variables:
     ```
     TOKEN_SECRET=your_secret_key_here
     ACCESS_TOKEN_VALIDITY=300
     REFRESH_TOKEN_VALIDITY=43200
     ```
   
2. **Accessing environment variables**
   ```python
   import os
   
   # After load_dotenv() has been called in app.py
   secret_key = os.getenv("TOKEN_SECRET")
   ```

3. **Loading .env file**
   The framework automatically loads the `.env` file in `app.py`:
   ```python
   from dotenv import load_dotenv
   
   # Load environment variables from .env file
   load_dotenv()
   ```

## Input Validation
The framework includes a FormatCheck utility for validating input data:

1. **Email Validation**
   ```python
   FormatCheck.email("user@example.com")
   ```
   - Uses regex pattern: `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+$`
   - Validates:
     - Username part: letters, numbers, dots, underscores, plus signs, hyphens
     - Domain part: letters, numbers, hyphens
     - TLD: letters only
   - Returns: True if valid, False otherwise

2. **Length Validation**
   ```python
   FormatCheck.minimumLength("password", 6)
   ```
   - Checks if string meets minimum length requirement
   - Parameters:
     - input_string: string to validate
     - min_length: minimum required length
   - Returns: True if length >= min_length, False otherwise

3. **Usage Examples**
   ```python
   # Email validation
   if not FormatCheck.email(user_email):
       return Response.bad_request("Invalid email format")

   # Password length check
   if not FormatCheck.minimumLength(password, 6):
       return Response.bad_request("Password must be at least 6 characters")

   # Name length check
   if not FormatCheck.minimumLength(name, 2):
       return Response.bad_request("Name must be at least 2 characters")
   ```

4. **Validation Rules**
   - Email: Must follow standard email format with valid characters
   - Password: Minimum 6 characters
   - Name: Minimum 2 characters

## Example Usage

### Creating a New Auto
```bash
curl -X POST http://localhost:8001/auto \
  -H "Content-Type: application/json" \
  -d '{"name": "Mercedes Benz", "ps": 750}'
```

### Getting All Autos
```bash
curl http://localhost:8001/auto
```

### Getting a Specific Auto
```bash
curl http://localhost:8001/auto/1
```

### Updating an Auto
```bash
curl -X PUT http://localhost:8001/auto \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Updated Name", "ps": 800}'
```

### Deleting an Auto
```bash
curl -X DELETE http://localhost:8001/auto \
  -H "Content-Type: application/json" \
  -d '{"id": 1}'
```

## Postman Collection
The framework includes a Postman collection (`Micro Python.postman_collection.json`) that contains pre-configured requests for example API endpoints. This makes it easy to test the API without writing curl commands.

### Importing the Collection
1. Open Postman
2. Click the "Import" button in the top-left corner
3. Select the "File" tab
4. Click "Upload Files" and select `Micro Python.postman_collection.json`
5. Click "Import"

### Using the Collection
The collection includes the following pre-configured requests:

#### Auto Endpoints
- **GET /auto**: List all autos
- **POST /auto**: Create a new auto
  - Body: JSON with `name` and `ps` fields
- **PUT /auto**: Update an existing auto
  - Body: JSON with `id`, `name`, and `ps` fields
- **DELETE /auto**: Delete an auto
  - Body: JSON with `id` field

### Collection Features
- Pre-configured headers (Content-Type: application/json)
- Example request bodies
- Organized folder structure
- Environment variables support
- Documentation for each endpoint

### Tips for Using Postman
1. **Environment Setup**
   - Create a new environment
   - Add a variable `base_url` with value `http://localhost:8001`
   - Use `{{base_url}}` in request URLs

2. **Testing Workflow**
   - Start with GET requests to view data
   - Use POST to create new entries
   - Use PUT to modify existing entries
   - Use DELETE to remove entries

3. **Response Handling**
   - Check status codes
   - View formatted JSON responses
   - Use Postman's test scripts for automation

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

## Limitations
1. No built-in authentication system
2. Limited error handling
3. Basic input validation
4. No request rate limiting
5. No built-in logging system
6. No built-in caching mechanism

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

## HTTP Request Lifecycle

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

### User Creation Flow
```mermaid
sequenceDiagram
    participant Client
    participant HttpHandler
    participant UserController
    participant UserModel
    participant Database

    Client->>HttpHandler: POST /user
    Note over HttpHandler: Validate request
    HttpHandler->>UserController: Route to Controller
    UserController->>UserModel: create()
    UserModel->>UserModel: Validate email
    UserModel->>UserModel: Hash password
    UserModel->>Database: INSERT query
    Database-->>UserModel: Success
    UserModel-->>UserController: Success
    UserController-->>HttpHandler: 200 OK
    HttpHandler-->>Client: Response
```

### Error Handling Flow
```mermaid
graph TD
    A[Error Occurs] --> B{Error Type}
    B -->|Validation| C[Format Validation Error]
    B -->|Database| D[Format Database Error]
    B -->|Not Found| E[Format 404 Error]
    C --> F[Set Error Status Code]
    D --> F
    E --> F
    F --> G[Send Error Response]
```

### Component Interaction
```mermaid
graph LR
    A[HttpHandler] -->|Routes| B[Controller]
    B -->|Uses| C[Models]
    C -->|Interacts| D[Database]
    B -->|Implements| E[IController Interface]
    B -->|May extend| F[AuthController]
    F -->|Uses| G[JWTManager]
    C -->|Implements| H[IModel Interface]
    D -->|Managed by| I[DBConnection]
    D -->|Schema by| J[DBMigrate]
```

## Response Format
All API responses follow a consistent format:

### Success Response
```json
{
    "status_code": 200,
    "status": "success",
    "message": {
        // Response data
    }
}
```

### Error Response
```json
{
    "status_code": 400,
    "status": "error",
    "message": "Error description"
}
```

## VS Code Integration
The framework includes VS Code integration features:
1. Custom snippets for quick code generation
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

## AI Assistant Features

The framework includes an intelligent code assistant that can help you with:
- Generating CRUD endpoints
- Providing code suggestions
- Generating documentation
- Analyzing your codebase
- Creating authenticated controllers with role-based access control

> ⚠️ **Framework Purity Warning**: When using AI assistants like GitHub Copilot, ChatGPT, or similar tools, they may suggest Flask, Django, or other framework patterns which are NOT compatible with this framework. Always ensure generated code follows the micro_py_framework patterns as shown in the examples.

### Getting Started with the AI Assistant

1. **Run the AI Assistant Demo**
   Simply run the `ai.py` file in your terminal:
   ```bash
   python ai.py
   ```
   This will show you examples of what the assistant can do:
   - Generate CRUD endpoints for a "Product" resource
   - Generate authenticated controllers with JWT validation
   - Show code suggestions for UserController
   - Generate documentation for controllers
   
   > **Note**: The script now includes error handling to handle any issues encountered when analyzing existing code. You may see notes about method parameters not matching interfaces exactly, which is normal and won't affect code generation.

2. **Understanding the Demo Output**
   When you run `ai.py`, you'll see:
   - The codebase analysis results (with notes about any pattern deviations)
   - Generated CRUD endpoints for a sample resource
   - Authentication-enabled controller examples
   - Code suggestions for common tasks
   - Generated documentation examples

3. **Using the Generated Code**
   The demo generates complete code examples that you can:
   - Copy and use in your own controllers
   - Use as templates for new resources
   - Study to understand the framework patterns

4. **Generating Secure Authenticated Controllers**
   You can generate controllers that automatically include JWT authentication:
   ```python
   # Example: Generate an authenticated controller
   authenticated_code = assistant.generate_crud_endpoints_with_auth("Resource")
   print(authenticated_code['controller'])
   ```
   
   This will generate a controller that extends `AuthController` with proper authentication checks in all methods.

5. **Generating Documentation**
   You can also generate documentation for specific components:
   ```python
   # Example: Generate documentation for controllers
   docs = assistant.generate_documentation("controller")
   print(docs)
   ```

### Understanding Controller Patterns

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

   Note that authenticated controllers:
   - Extend `AuthController` and implement `IController`
   - Have an additional `headers` parameter in each method
   - Call `self.authenticate(headers)` to validate tokens
   - Can access `self.user_id` and `self.role` after authentication

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

### Important Notes
- The assistant analyzes your codebase to provide context-aware suggestions
- Generated code should be reviewed and customized for your specific needs
- Authentication controllers automatically integrate with the JWT system
- The assistant is designed for educational purposes and may not cover all edge cases
- Always test generated code before using it in production
- You may see notes about method parameters not matching interfaces exactly during analysis, which is normal and won't affect code generation

### Example Authentication Workflow
1. Generate an authenticated controller with the assistant
2. Configure your `.env` file with JWT settings
3. Create JWTs for your users (e.g., upon login)
4. Make API requests with the JWT in the Authorization header
5. The controller will automatically validate JWTs and check role permissions

## A Note from the Developer

Thank you for taking the time to explore this educational framework! I created this project to help beginners understand the fundamental concepts of web development and Python programming.

I hope this framework serves as a helpful stepping stone in your learning journey. Remember that every expert was once a beginner, and the key to mastering programming is consistent practice and curiosity.

Best wishes for your learning journey!

Ali Khorsandfard
Developer & Educator