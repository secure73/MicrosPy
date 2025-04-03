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

6. Migrate Database for sample Database:
   ```bash
   # Run database migration
   python migrate.py

   # Start the application
   python app.py   # Server will start on port 8001
   ```
7. Run App:
   ```bash
   # Start the application
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
└── helper/              # Helper utilities
    ├── HttpHandler.py    # HTTP request handler
    ├── Response.py       # Response formatting
    ├── JWTManager.py     # JWT authentication
    ├── FormatCheck.py    # Input validation
    ├── CodeAssistant.py  # AI-powered code generation
    └── DatabaseMigration.py  # Database migration helper
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

### SQLite Database
- The application uses SQLite as the default database
- Database file: `db.db`
- Tables are automatically created on first run

### Database Migration (DatabaseMigration.py)
The `DatabaseMigration.py` file is responsible for automatic database initialization and table creation. It handles:

1. **Database Connection**
   - Creates a connection to SQLite database (`db.db`)
   - Manages database cursor for executing SQL commands
   - Uses SQLAlchemy for database operations

2. **Automatic Table Creation**
   - Automatically discovers and creates all tables defined in the `table` directory
   - Uses SQLAlchemy models to define table structure
   - Currently manages tables like:
     - `users`: Stores user information with email, password, and name
     - `autos`: Stores auto information with name and horsepower (ps)
   - No manual SQL creation needed - tables are created from model definitions

3. **Migration Features**
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

4. **Migration Script (migrate.py)**
   easily open migrate.py on the root and run it , or write python migrate.py on terminal in project root!
   
   Features:
   - Automatic table creation from model definitions
   - Schema version tracking
   - Column modification detection
   - Clear progress indicators
   - Migration summary generation
   - Error handling with descriptive messages

5. **Key Benefits**
   - No manual SQL writing required
   - Consistent database schema across installations
   - Automatic schema updates when models change
   - Clear feedback during migration process
   - Error detection and reporting
   - Safe migration process with rollback support

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


4. **Database Support**
   - **SQLite** (Default):
     ```python
     engine = create_engine("sqlite:///db.db")
     ```
   - **MySQL/MariaDB**:
     ```python
     engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
     ```

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
    C -->|Implements| F[IModel Interface]
    D -->|Managed by| G[DBConnection]
    D -->|Schema by| H[DBMigrate]
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
2. IntelliSense support for framework components
3. Recommended extensions for Python development
4. Automatic code formatting with Black
5. Linting with Pylint
6. Import organization
7. Documentation generation support

## AI Assistant Features

The framework includes an intelligent code assistant that can help you with:
- Generating CRUD endpoints
- Providing code suggestions
- Generating documentation
- Analyzing your codebase

### Getting Started with the AI Assistant

1. **Run the AI Assistant Demo**
   Simply run the `ai.py` file in your terminal:
   ```bash
   python ai.py
   ```
   This will show you examples of what the assistant can do:
   - Generate CRUD endpoints for a "Product" resource
   - Show code suggestions for UserController
   - Generate documentation for controllers

2. **Understanding the Demo Output**
   When you run `ai.py`, you'll see:
   - The codebase analysis results
   - Generated CRUD endpoints for a sample resource
   - Code suggestions for common tasks
   - Generated documentation examples

3. **Using the Generated Code**
   The demo generates complete code examples that you can:
   - Copy and use in your own controllers
   - Use as templates for new resources
   - Study to understand the framework patterns

4. **Generating Documentation**
   You can also generate documentation for specific components:
   ```python
   # Example: Generate documentation for controllers
   docs = assistant.generate_documentation("controller")
   print(docs)
   ```

### Important Notes
- The assistant analyzes your codebase to provide context-aware suggestions
- Generated code should be reviewed and customized for your specific needs
- The assistant is designed for educational purposes and may not cover all edge cases
- Always test generated code before using it in production

### Example Workflow
1. Run `python ai.py` to see examples
2. Review the generated code and documentation
3. Use the patterns shown to create your own resources
4. Get code suggestions when needed
5. Generate documentation for your code
6. Review and customize the generated code
7. Test your implementation

Remember: This is an educational framework. Always review generated code and understand what it does before using it in your project.

## A Note from the Developer

Thank you for taking the time to explore this educational framework! I created this project to help beginners understand the fundamental concepts of web development and Python programming.

I hope this framework serves as a helpful stepping stone in your learning journey. Remember that every expert was once a beginner, and the key to mastering programming is consistent practice and curiosity.

Best wishes for your learning journey!

Ali Khorsandfard
Developer & Educator