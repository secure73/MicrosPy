# Micro Python Framework Documentation

## Overview
This is a minimal micro-framework designed for learning the fundamentals of Python and RESTful API development. It implements a simple MVC (Model-View-Controller) architecture and provides basic RESTful API functionality.

## Prerequisites
- Python 3.13.2 or higher
- Virtual environment (recommended)

## Virtual Environment
Using a virtual environment is **crucial** for Python development. Here's why and how to use it:

### Why Use Virtual Environment?
1. **Isolation**: Each project gets its own isolated Python environment
   - Prevents conflicts between project dependencies
   - Avoids system-wide Python package pollution
   - Makes projects reproducible across different machines

2. **Dependency Management**:
   - Clear separation of project dependencies
   - Easy to track and install required packages
   - Simple to export requirements with exact versions

3. **Project Portability**:
   - Projects can be easily shared with others
   - No interference with system Python installation
   - Consistent environment across development team

### Setting Up Virtual Environment

1. **Windows**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   .\venv\Scripts\activate

   # Verify activation (should show virtual environment path)
   where python
   ```

2. **Linux/Mac**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   source venv/bin/activate

   # Verify activation (should show virtual environment path)
   which python
   ```

3. **Deactivation** (All Platforms)
   ```bash
   deactivate
   ```

### Best Practices
1. **Always activate** the virtual environment before:
   - Installing packages
   - Running the application
   - Running migrations
   - Executing tests

2. **Never commit** virtual environment directory:
   - Add `venv/` to your `.gitignore`
   - Only commit `requirements.txt`

3. **Maintain requirements**:
   ```bash
   # After installing new packages, update requirements.txt
   pip freeze > requirements.txt
   ```

4. **Project Setup**:
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows

   # Install dependencies
   pip install -r requirements.txt

   # Run database migration
   python migrate.py

   # Start the application
   python app.py
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

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd micro_py_framework
   ```

2. Follow the virtual environment setup and activation steps from the Virtual Environment section above.

3. Install dependencies and set up the application:
   ```bash
   # Install dependencies
   pip install -r requirements.txt

   # Run database migration
   python migrate.py

   # Start the application
   python app.py   # Server will start on port 8001
   ```

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
The `DatabaseMigration.py` file is responsible for database initialization and table creation. It handles:

1. **Database Connection**
   - Creates a connection to SQLite database (`db.db`)
   - Manages database cursor for executing SQL commands

2. **Table Creation**
   - Automatically creates required tables if they don't exist
   - Currently manages three tables:
     - `users` table:
       ```sql
       CREATE TABLE users(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           email TEXT NOT NULL UNIQUE,
           password TEXT NOT NULL,
           name TEXT NOT NULL
       )
       ```
     - `autos` table:
       ```sql
       CREATE TABLE autos(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL,
           ps INTEGER NOT NULL
       )
       ```

3. **Usage**
   - The migration runs automatically when the application starts
   - Can also be run manually using the migration script:
     ```bash
     python migrate.py
     ```
   - The migration script provides clear status updates:
     ```
     🚀 Starting database migration...
     ✓ No new tables needed to be created.
     ✨ Migration process completed!
     ```
   - Ensures database schema is up-to-date
   - Prevents errors from missing tables

4. **Features**
   - Uses `CREATE TABLE IF NOT EXISTS` to prevent duplicate table creation
   - Handles primary keys with auto-increment
   - Enforces NOT NULL constraints on required fields
   - Provides clear migration status messages with emojis
   - Supports column change detection

5. **Migration Script (migrate.py)**
   The framework includes a dedicated migration script that can be run independently:
   ```python
   from helper.DatabaseMigration import DatabaseMigration

   def main():
       print("Starting database migration...")
       migrator = DatabaseMigration()
       migrator.migrate()

   if __name__ == "__main__":
       main()
   ```
   This script:
   - Can be run at any time to ensure database schema is up to date
   - Shows clear progress with emoji indicators
   - Creates missing tables if needed
   - Checks for column changes in existing tables
   - Provides a summary of all migration actions

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