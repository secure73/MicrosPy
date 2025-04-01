from helper.CodeAssistant import CodeAssistant
from pathlib import Path

def main():
    # Initialize the AI Assistant
    assistant = CodeAssistant()
    
    # Analyze the codebase to understand patterns and relationships
    root_dir = Path(__file__).parent.parent
    assistant.analyze_codebase(str(root_dir))
    
    # Example 1: Generate CRUD endpoints for a new resource
    print("Generating CRUD endpoints for 'Product' resource...")
    product_endpoints = assistant.generate_crud_endpoints("Product")
    
    # Save the generated code to files
    for file_type, code in product_endpoints.items():
        file_path = root_dir / file_type / f"Product{file_type.capitalize()}.py"
        with open(file_path, 'w') as f:
            f.write(code)
        print(f"Generated {file_type} code at {file_path}")
    
    # Example 2: Get code suggestions for a specific context
    print("\nGetting code suggestions for a controller method...")
    context = """
    class UserController(IController):
        def get(self, data):
            # Get suggestions for this method
    """
    suggestions = assistant.suggest_code(context, "UserController.py")
    print("Suggestions:", suggestions)
    
    # Example 3: Generate documentation based on patterns
    print("\nGenerating documentation for controllers...")
    controller_docs = assistant.generate_documentation("controller")
    print(controller_docs)

if __name__ == "__main__":
    main() 