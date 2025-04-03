from helper.CodeAssistant import CodeAssistant
from pathlib import Path

def main():
    # Create an AI assistant
    assistant = CodeAssistant()
    
    # Get the project root directory
    # Since this file is in the root directory, we don't need to go up any levels
    root_dir = Path(__file__).parent
    
    # Analyze the codebase
    print("Analyzing codebase...")
    assistant.analyze_codebase(str(root_dir))
    print("Codebase analysis complete!")
    
    # Example 1: Generate CRUD endpoints for a new resource
    print("\nGenerating CRUD endpoints for 'Product'...")
    product_endpoints = assistant.generate_crud_endpoints("Product")
    print("Generated endpoints:")
    for endpoint_type, code in product_endpoints.items():
        print(f"\n{endpoint_type}:\n{code}")
    
    # Example 2: Get code suggestions
    print("\nGetting code suggestions for UserController...")
    context = "How to implement user authentication in the controller"
    suggestions = assistant.suggest_code(context, "UserController.py")
    print(f"Suggestions:\n{suggestions}")
    
    # Example 3: Generate documentation
    print("\nGenerating documentation for controllers...")
    docs = assistant.generate_documentation("controller")
    print(f"Documentation:\n{docs}")

if __name__ == "__main__":
    main() 