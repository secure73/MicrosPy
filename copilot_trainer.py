#!/usr/bin/env python
"""
Copilot Trainer for micro_py_framework

This script helps train GitHub Copilot to understand the micro_py_framework patterns
by generating reference examples and opening them in VS Code.

To use:
1. Run this script from the command line: python copilot_trainer.py
2. The script will generate example files in a reference directory
3. VS Code will open with these examples (if VS Code is installed)
4. Work alongside these examples when creating new components

This helps Copilot learn the correct patterns for this framework instead of
suggesting patterns from Flask, Django, or other frameworks.
"""

import os
import sys
import subprocess
from pathlib import Path
import shutil
from helper.CodeAssistant import CodeAssistant

REFERENCE_DIR = "copilot_reference"
VSCODE_COMMAND = "code"  # VS Code command-line command

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        from helper.CodeAssistant import CodeAssistant
        return True
    except ImportError:
        print("Error: helper.CodeAssistant not found. Make sure you're running this script from the project root.")
        return False

def create_reference_directories():
    """Create directories for reference examples"""
    reference_path = Path(REFERENCE_DIR)
    
    # Create main directory if it doesn't exist
    if reference_path.exists():
        shutil.rmtree(reference_path)
    
    # Create subdirectories
    (reference_path / "controller").mkdir(parents=True)
    (reference_path / "model").mkdir(parents=True)
    (reference_path / "table").mkdir(parents=True)
    
    # Create README file
    with open(reference_path / "README.md", "w") as f:
        f.write("""# Copilot Reference Examples

These files are examples to help train GitHub Copilot with the correct micro_py_framework patterns.
Keep these files open while working to help Copilot suggest appropriate code.

**Important:** DO NOT import or use patterns from Flask, Django, or other frameworks!

## Best Practices

1. Controller methods should be `get`, `post`, `put`, and `destroy` (not delete)
2. Controllers should implement `IController` or extend `AuthController`
3. All models should implement `IModel`
4. Tables should extend `Base` from `table.DBConnection`
5. Use the framework's own `Response` class for API responses
""")
    
    return reference_path

def generate_example_resources(assistant, output_dir):
    """Generate example resources using CodeAssistant"""
    # List of resources to generate
    resources = [
        "Product", "Order", "Customer", "Category", "Inventory"
    ]
    
    # Create both regular and authenticated controllers
    for resource in resources:
        # Basic controllers
        basic_code = assistant.generate_crud_endpoints(resource)
        
        # Write controller
        with open(output_dir / "controller" / f"{resource}Controller.py", "w") as f:
            f.write(f"# Example {resource}Controller for micro_py_framework\n")
            f.write(f"# Use this pattern when creating new controllers\n")
            f.write(f"# DO NOT mix with Flask, Django, or other frameworks\n\n")
            f.write(basic_code["controller"])
        
        # Write model
        with open(output_dir / "model" / f"{resource}Model.py", "w") as f:
            f.write(f"# Example {resource}Model for micro_py_framework\n")
            f.write(f"# Use this pattern when creating new models\n")
            f.write(f"# DO NOT mix with Flask, Django, or other frameworks\n\n")
            f.write(basic_code["model"])
        
        # Write table
        with open(output_dir / "table" / f"{resource}Table.py", "w") as f:
            f.write(f"# Example {resource}Table for micro_py_framework\n")
            f.write(f"# Use this pattern when creating new tables\n")
            f.write(f"# DO NOT mix with Flask, Django, or other frameworks\n\n")
            f.write(basic_code["table"])
    
    # Create authenticated controller examples
    for i, resource in enumerate(resources[:3]):  # Just use the first 3 resources
        auth_resource = f"Auth{resource}"
        auth_code = assistant.generate_crud_endpoints_with_auth(auth_resource)
        
        # Write authenticated controller
        with open(output_dir / "controller" / f"{auth_resource}Controller.py", "w") as f:
            f.write(f"# Example Authenticated Controller for micro_py_framework\n")
            f.write(f"# Use this pattern when creating secured endpoints\n")
            f.write(f"# DO NOT mix with Flask, Django, or other frameworks\n\n")
            f.write(auth_code["controller"])

def generate_anti_patterns(output_dir):
    """Generate examples of what NOT to do (with comments explaining why)"""
    # Create an "anti-patterns" directory
    anti_dir = output_dir / "anti_patterns"
    anti_dir.mkdir(exist_ok=True)
    
    # Flask-style anti-pattern
    with open(anti_dir / "flask_style_DONT_USE.py", "w") as f:
        f.write("""# DON'T USE THIS PATTERN - This is a Flask pattern, not micro_py_framework!
# -------------------------------------------------------------------
# This file demonstrates patterns that should NOT be used with micro_py_framework
# Copilot might suggest these patterns but they should be rejected.

from flask import Flask, request, jsonify  # WRONG - Don't import Flask!

app = Flask(__name__)  # WRONG - micro_py_framework doesn't use Flask app

@app.route('/product', methods=['GET'])  # WRONG - Don't use decorators
def get_products():                      # WRONG - Don't use function-based views
    # Flask pattern - DON'T USE THIS
    products = get_all_products()
    return jsonify(products)

# CORRECT PATTERN:
'''
from interface.IController import IController
from helper.Response import Response
from model.ProductModel import ProductModel

class ProductController(IController):
    def __init__(self):
        self.model = ProductModel()
        
    def get(self, data):
        result = self.model.list()
        if not result:
            return Response.bad_request("Failed to get products")
        return Response.success(result)
'''
""")

    # Django-style anti-pattern
    with open(anti_dir / "django_style_DONT_USE.py", "w") as f:
        f.write("""# DON'T USE THIS PATTERN - This is a Django pattern, not micro_py_framework!
# -------------------------------------------------------------------
# This file demonstrates patterns that should NOT be used with micro_py_framework
# Copilot might suggest these patterns but they should be rejected.

from django.db import models  # WRONG - Don't import Django!

# WRONG - Don't use Django models
class Product(models.Model):  # WRONG - Don't extend Django's Model class
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

# CORRECT PATTERN:
'''
from sqlalchemy import Column, Integer, String, Float
from table.DBConnection import Base
from datetime import datetime

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
'''
""")

def create_comment_examples(output_dir):
    """Create a file with comments that help guide Copilot"""
    with open(output_dir / "copilot_comments.py", "w") as f:
        f.write("""# Effective Comments for Guiding GitHub Copilot with micro_py_framework
# --------------------------------------------------------------------
# Use comments like these to help Copilot generate appropriate code.

# GOOD COMMENT: Specific to the framework
# Create a new controller for Products following micro_py_framework patterns

# GOOD COMMENT: Reminds Copilot which framework we're using
# Using micro_py_framework, implement a User model with email and password fields

# GOOD COMMENT: Reminding about inheritance
# Create a controller that extends AuthController for secure endpoints

# GOOD COMMENT: Reminding about method names
# Implement the get, post, put, destroy methods (not delete)

# LESS EFFECTIVE:
# Create a new controller for products
# (Too generic, might lead Copilot to use Flask or other patterns)

# LESS EFFECTIVE:
# Create a REST API
# (Too vague, will likely lead to Flask suggestions)
""")

def open_vscode(directory):
    """Attempt to open VS Code with the reference files"""
    try:
        # Check if VS Code is available
        subprocess.run([VSCODE_COMMAND, "--version"], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL, 
                      check=True)
        
        # Open VS Code with the reference directory
        subprocess.run([VSCODE_COMMAND, directory])
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        print(f"Could not open VS Code automatically. Please open {directory} manually.")
        return False

def create_training_document(output_dir):
    """Create a training document with patterns to follow"""
    with open(output_dir / "TRAINING_GUIDE.md", "w") as f:
        f.write("""# micro_py_framework Training Guide for GitHub Copilot

## Framework Pattern Summary

### Controllers
- Must implement `IController` or extend `AuthController`
- Must provide `get`, `post`, `put`, `destroy` methods (NOT `delete`)
- Use `Response` class for formatted responses
- When using authentication:
  - Extend `AuthController`
  - Accept `headers` parameter and call `self.authenticate(headers)`
  - Check authentication result before proceeding

### Models
- Must implement `IModel`
- Provide `create`, `single` (NOT `get`), `list`, `update`, `remove` (NOT `delete`) methods
- Handle error reporting through `self.error` attribute
- Use `DBConnection.Session` for database access

### Tables
- Must extend `Base` from `table.DBConnection`
- Define columns using SQLAlchemy's `Column` 
- Include standard columns like `id`, `created_at`, `updated_at`
- Implement `to_dict()` method for serialization

## Anti-Patterns to Avoid

- Don't use Flask's `@app.route` decorators
- Don't use Django's `models.Model` base class
- Don't import from Flask, Django, or FastAPI
- Don't use function-based route handlers
- Don't use Django's `views.py`/`urls.py` pattern
- Don't use FastAPI's `@app.get`/`@app.post` decorators

## Recommended Workflow

1. Keep these reference files open when working with Copilot
2. Start with a clear comment describing what you want to implement
3. Explicitly mention "micro_py_framework" in your comments
4. If Copilot suggests Flask/Django patterns, reject and add clarifying comments
5. Use code from the reference examples to guide Copilot

## VS Code Tips for Copilot

- Press Tab to accept suggestions
- Press Esc to reject suggestions
- Press Alt+] to see the next suggestion
- Press Alt+[ to see the previous suggestion
""")

def main():
    """Main function to train GitHub Copilot with micro_py_framework patterns"""
    print("🚀 Starting GitHub Copilot Trainer for micro_py_framework...")
    
    if not check_dependencies():
        sys.exit(1)
    
    print("✅ Dependencies found.")
    
    # Create directory structure
    print(f"📁 Creating reference directories in {REFERENCE_DIR}...")
    output_dir = create_reference_directories()
    print(f"✅ Created directories.")
    
    # Initialize CodeAssistant
    print("🤖 Initializing CodeAssistant...")
    assistant = CodeAssistant()
    
    # Analyze codebase if available
    try:
        print("🔍 Analyzing codebase...")
        assistant.analyze_codebase(str(Path('.')))
        print("✅ Codebase analysis complete.")
    except Exception as e:
        print(f"⚠️  Warning: Could not analyze codebase: {e}")
    
    # Generate examples
    print("📝 Generating example resources...")
    generate_example_resources(assistant, output_dir)
    print("✅ Generated example resources.")
    
    # Create anti-pattern examples
    print("⛔ Creating anti-pattern examples...")
    generate_anti_patterns(output_dir)
    print("✅ Created anti-pattern examples.")
    
    # Create comment examples
    print("💬 Creating comment examples...")
    create_comment_examples(output_dir)
    print("✅ Created comment examples.")
    
    # Create training document
    print("📜 Creating training guide...")
    create_training_document(output_dir)
    print("✅ Created training guide.")
    
    # Try to open VS Code
    print("🔍 Attempting to open VS Code...")
    vs_open = open_vscode(REFERENCE_DIR)
    
    # Final instructions
    print("\n✨ GitHub Copilot training materials generated! ✨")
    print(f"\nReference files have been created in: {REFERENCE_DIR}")
    if not vs_open:
        print("\nTo use these files:")
        print(f"1. Open VS Code manually: code {REFERENCE_DIR}")
        print("2. Keep these files open in a separate VS Code window while working")
        print("3. Follow the recommendations in TRAINING_GUIDE.md")
    print("\n🔎 These files will help train Copilot to suggest micro_py_framework patterns")
    print("   instead of Flask, Django, or other frameworks.")
    print("\n🚫 Remember: DO NOT mix with Flask, Django, or other frameworks!\n")

if __name__ == "__main__":
    main() 