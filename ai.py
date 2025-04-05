from helper.CodeAssistant import CodeAssistant
from pathlib import Path

def main():
    """
    AI Assistant Demo for micro_py_framework
    
    This script demonstrates how to use the AI assistant to:
    1. Generate CRUD endpoints
    2. Generate authenticated controllers with JWT validation
    3. Get code suggestions
    4. Generate documentation
    
    When using with GitHub Copilot or other AI tools:
    - Always ensure generated code uses micro_py_framework patterns
    - Do NOT accept suggestions that import Flask, Django, or other frameworks
    - Run this file to see proper examples of framework-compliant code
    """
    
    # Create an AI assistant
    assistant = CodeAssistant()
    
    # Get the project root directory
    # Since this file is in the root directory, we don't need to go up any levels
    root_dir = Path(__file__).parent
    
    # Analyze the codebase
    print("Analyzing codebase...")
    try:
        assistant.analyze_codebase(str(root_dir))
        print("Codebase analysis complete!")
    except Exception as e:
        print(f"Warning: Codebase analysis encountered an issue: {e}")
        print("This is normal for existing code that doesn't follow the exact interface pattern.")
        print("The examples will still be generated correctly.")
    
    # Example 1: Generate CRUD endpoints for a new resource
    print("\n============ EXAMPLE 1: Basic CRUD Endpoints ============")
    print("Generating CRUD endpoints for 'Product'...")
    try:
        product_endpoints = assistant.generate_crud_endpoints("Product")
        print("Generated endpoints:")
        for endpoint_type, code in product_endpoints.items():
            print(f"\n--- {endpoint_type} ---\n{code}")
    except Exception as e:
        print(f"Error generating basic CRUD endpoints: {e}")
    
    # Example 2: Generate authenticated CRUD endpoints
    print("\n============ EXAMPLE 2: Authenticated CRUD Endpoints ============")
    print("Generating authenticated CRUD endpoints for 'Order'...")
    try:
        auth_endpoints = assistant.generate_crud_endpoints_with_auth("Order")
        print("Generated authenticated endpoints:")
        for endpoint_type, code in auth_endpoints.items():
            print(f"\n--- {endpoint_type} ---\n{code}")
    except Exception as e:
        print(f"Error generating authenticated CRUD endpoints: {e}")
    
    # Example 3: Get code suggestions
    print("\n============ EXAMPLE 3: Code Suggestions ============")
    print("Getting code suggestions for UserController...")
    try:
        context = "How to implement user authentication in the controller"
        suggestions = assistant.suggest_code(context, "UserController.py")
        print(f"Suggestions:\n{suggestions}")
    except Exception as e:
        print(f"Error generating code suggestions: {e}")
    
    # Example 4: Generate documentation
    print("\n============ EXAMPLE 4: Documentation Generation ============")
    print("Generating documentation for controllers...")
    try:
        docs = assistant.generate_documentation("controller")
        print(f"Documentation:\n{docs}")
    except Exception as e:
        print(f"Error generating documentation: {e}")
    
    print("\n============ Using with VS Code & Copilot ============")
    print("When using VS Code with Copilot or other AI tools:")
    print("1. Run this script first to see proper code examples")
    print("2. Use these examples as reference when working with Copilot")
    print("3. Reject any suggestions that import or use patterns from Flask, Django, etc.")
    print("4. All controllers should implement IController or extend AuthController")
    print("5. All models should implement IModel")
    print("6. All tables should extend Base from table.DBConnection")
    
    print("\n============ About Method Warnings ============")
    print("You may see warnings about method parameters not matching the interface exactly.")
    print("This is normal for existing code and doesn't affect code generation.")
    print("For new code, consider using the patterns shown in the generated examples.")

if __name__ == "__main__":
    main() 