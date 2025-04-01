# Micro Python Framework Documentation

## Overview
This is a minimal micro-framework designed for learning the fundamentals of Python and RESTful API development. It implements a simple MVC (Model-View-Controller) architecture and provides basic RESTful API functionality.

## Prerequisites
- Python 3.13.2 or higher
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd micro_py_framework
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure
```
micro_py_framework/
├── app.py                 # Main application entry point
├── controller/            # Controllers directory
│   └── UserController.py  # User-related operations
├── model/                # Models directory
│   └── UserModel.py      # User data operations
├── table/                # Database tables
│   ├── DBConnection.py   # Database connection management
│   ├── DBMigrate.py      # Database migration and schema
│   └── UserTable.py      # User table schema
├── interface/            # Interfaces directory
│   └── IController.py    # Controller interface
└── helper/              # Helper utilities
    ├── HttpHandler.py    # HTTP request handler
    ├── Response.py       # Response formatting
    ├── JWTManager.py     # JWT authentication
    └── FormatCheck.py    # Input validation
```

## Running the Application
```bash
python app.py
```
The server will start on port 8001 by default.

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

## Data Validation

### User Data Validation Rules
- Email: Must follow standard email format
- Password: Minimum 6 characters
- Name: Minimum 2 characters

## Database

### SQLite Database
- The application uses SQLite as the default database
- Database file: `db.db`
- Tables are automatically created on first run

### Database Migration (DBMigrate.py)
The `DBMigrate.py` file is responsible for database initialization and table creation. It handles:

1. **Database Connection**
   - Creates a connection to SQLite database (`db.db`)
   - Manages database cursor for executing SQL commands

2. **Table Creation**
   - Automatically creates required tables if they don't exist
   - Currently manages two tables:
     - `users` table:
       ```sql
       CREATE TABLE users(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           email TEXT NOT NULL UNIQUE,
           password TEXT NOT NULL,
           name TEXT NOT NULL
       )
       ```
     - `products` table:
       ```sql
       CREATE TABLE products(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL UNIQUE,
           category TEXT NOT NULL,
           price FLOAT NOT NULL
       )
       ```

3. **Usage**
   - The migration runs automatically when the application starts
   - Ensures database schema is up-to-date
   - Prevents errors from missing tables

4. **Features**
   - Uses `CREATE TABLE IF NOT EXISTS` to prevent duplicate table creation
   - Handles primary keys with auto-increment
   - Enforces unique constraints on email and product names
   - Manages required fields with NOT NULL constraints

### Database Connection Management (DBConnection.py)
The `DBConnection.py` file manages database connections using SQLAlchemy ORM. It provides:

1. **SQLAlchemy Integration**
   - Uses SQLAlchemy for Object-Relational Mapping (ORM)
   - Provides a declarative base for model definitions
   - Manages database sessions efficiently

2. **Connection Configuration**
   ```python
   engine = create_engine("sqlite:///db.db", echo=False)
   ```
   - Default configuration uses SQLite database
   - Supports MySQL/MariaDB through connection string modification
   - `echo=False` disables SQL query logging for better performance

3. **Session Management**
   ```python
   Session = sessionmaker(bind=engine)
   ```
   - Creates a session factory for database operations
   - Manages database connections and transactions
   - Provides thread-safe database access

4. **Utility Methods**
   - `create_all()`: Creates all database tables defined in models
   - `get_session()`: Returns a new database session for operations

5. **Database Support**
   - **SQLite** (Default):
     ```python
     engine = create_engine("sqlite:///db.db")
     ```
   - **MySQL/MariaDB**:
     ```python
     engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
     ```

6. **Error Handling**
   - Catches and reports database connection failures
   - Provides clear error messages for troubleshooting

7. **Usage in Models**
   ```python
   from table.DBConnection import DBConnection
   
   class YourModel:
       def __init__(self):
           self.Session = DBConnection.Session
   ```

8. **Best Practices**
   - Uses connection pooling for better performance
   - Implements proper session management
   - Supports multiple database backends
   - Follows SQLAlchemy best practices

### MySQL Support
- The framework also supports MySQL databases
- To use MySQL, modify the connection string in `table/DBConnection.py`:
  ```python
  engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
  ```

## Error Handling
The framework includes basic error handling for:
- Invalid input data
- Database operations
- HTTP request validation
- Resource not found

## Security Notes
1. This is an educational framework and is not recommended for production use
2. Password hashing is implemented using bcrypt
3. Basic input validation is provided through FormatCheck.py
4. JWT authentication support is available through JWTManager.py
5. No built-in authentication/authorization system

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

### Creating a New User
```bash
curl -X POST http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123", "name": "John Doe"}'
```

### Getting All Users
```bash
curl http://localhost:8001/user
```

### Getting a Specific User
```bash
curl http://localhost:8001/user/1
```

### Updating a User
```bash
curl -X PUT http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Updated Name"}'
```

### Deleting a User
```bash
curl -X DELETE http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"id": 1}'
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

## HTTP Request Lifecycle

### General Request Flow
```mermaid
graph TD
    A[Client Request] --> B[HttpHandler]
    B --> C{Request Validation}
    C -->|Valid| D[Route to Controller]
    C -->|Invalid| E[Return 400 Error]
    D --> F[Execute Controller Method]
    F --> G[Process Model Operations]
    G --> H[Database Operations]
    H --> I[Format Response]
    I --> J[Send Response to Client]
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
    Note over HttpHandler: Validate Request
    HttpHandler->>UserController: Route to Controller
    UserController->>UserModel: create()
    UserModel->>UserModel: Validate Email
    UserModel->>UserModel: Hash Password
    UserModel->>Database: INSERT Query
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
    A[HttpHandler] -->|Routes| B[Controllers]
    B -->|Uses| C[Models]
    C -->|Interacts| D[Database]
    B -->|Implements| E[IController Interface]
    C -->|Implements| F[IModel Interface]
    D -->|Managed by| G[DBConnection]
    D -->|Schema by| H[DBMigrate]
```

## Response Handling

### Response Class (helper/Response.py)
The `Response` class provides a standardized way to format API responses. It ensures consistent response structure across all endpoints.

#### Response Structure
```json
{
    "status_code": 200,      // HTTP status code
    "status": "success",     // "success" or "error"
    "message": {}            // Response data or error message
}
```

#### Available Methods

1. **Base Response Method**
   ```python
   @staticmethod
   def response(status_code, data)
   ```
   - Creates a standardized response object
   - Automatically determines status based on status code
   - Status codes >= 400 are marked as "error"
   - Status codes < 400 are marked as "success"

2. **Success Response**
   ```python
   @staticmethod
   def success(data)
   ```
   - Returns a 200 OK response
   - Used for successful operations
   - Example:
     ```python
     Response.success({"user": "created"})
     # Returns:
     # {
     #     "status_code": 200,
     #     "status": "success",
     #     "message": {"user": "created"}
     # }
     ```

3. **Bad Request Response**
   ```python
   @staticmethod
   def bad_request(message)
   ```
   - Returns a 400 Bad Request response
   - Used for validation errors or invalid input
   - Example:
     ```python
     Response.bad_request("Invalid email format")
     # Returns:
     # {
     #     "status_code": 400,
     #     "status": "error",
     #     "message": "Invalid email format"
     # }
     ```

4. **Unauthorized Response**
   ```python
   @staticmethod
   def unauthorized(message)
   ```
   - Returns a 401 Unauthorized response
   - Used for authentication failures
   - Example:
     ```python
     Response.unauthorized("Invalid credentials")
     # Returns:
     # {
     #     "status_code": 401,
     #     "status": "error",
     #     "message": "Invalid credentials"
     # }
     ```

5. **Internal Error Response**
   ```python
   @staticmethod
   def internal_error(message)
   ```
   - Returns a 500 Internal Server Error response
   - Used for server-side errors
   - Example:
     ```python
     Response.internal_error("Database connection failed")
     # Returns:
     # {
     #     "status_code": 500,
     #     "status": "error",
     #     "message": "Database connection failed"
     # }
     ```

#### Usage Examples

1. **In Controllers**
   ```python
   def post(self, data):
       try:
           # Process data
           return Response.success({"message": "Created successfully"})
       except ValidationError:
           return Response.bad_request("Invalid input")
       except Exception:
           return Response.internal_error("Server error")
   ```

2. **Error Handling**
   ```python
   if not user_data:
       return Response.bad_request("User not found")
   ```

3. **Success Response**
   ```python
   return Response.success({
       "user": {
           "id": 1,
           "name": "John Doe",
           "email": "john@example.com"
       }
   })
   ```

#### Best Practices
1. Always use the Response class for consistent API responses
2. Use appropriate status codes for different scenarios
3. Provide clear and descriptive error messages
4. Keep response data structure consistent
5. Use success() for successful operations
6. Use specific error methods (bad_request, unauthorized, internal_error) for different error types 

## Authentication

### JWT Authentication (helper/JWTManager.py)
The framework includes JWT (JSON Web Token) support for authentication:

1. **Token Creation**
   ```python
   jwt_manager = JWTManager()
   token = jwt_manager.create({"user_id": 123, "role": "admin"})
   ```
   - Creates JWT tokens with expiration
   - Default expiration: 60 minutes
   - Uses HS256 algorithm
   - Automatically adds expiration timestamp

2. **Token Verification**
   ```python
   decoded = jwt_manager.verify(token)
   if decoded:
       # Token is valid
       user_data = decoded
   else:
       # Token is invalid or expired
   ```
   - Verifies token validity
   - Checks expiration
   - Returns decoded payload or False

3. **Configuration**
   ```python
   self.__secret_key = "your-secret-key"
   self.__algorithm = "HS256"
   self.__expiration_minutes = 60
   ```
   - Configurable secret key
   - Configurable algorithm
   - Configurable expiration time

4. **Usage Example**
   ```python
   # Creating a token
   jwt_manager = JWTManager()
   user_data = {"user_id": 123, "role": "admin"}
   token = jwt_manager.create(user_data)

   # Verifying a token
   decoded = jwt_manager.verify(token)
   if decoded:
       print("Decoded Data:", decoded)
   ```

5. **Security Notes**
   - Secret key should be stored in environment variables
   - Tokens expire after 60 minutes by default
   - Uses industry-standard HS256 algorithm
   - Handles token expiration gracefully 