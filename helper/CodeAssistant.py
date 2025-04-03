from typing import Dict, List, Optional, Tuple
import inspect
import ast
from pathlib import Path
import re
from .VSCodeIntegration import VSCodeIntegration
from .PatternRecognition import PatternRecognition

class CodeAssistant:
    def __init__(self):
        self.project_structure = {
            'controllers': {},
            'models': {},
            'tables': {},
            'helpers': {},
            'interfaces': {}
        }
        self.patterns = {
            'controller': {
                'basic': '''from interface.IController import IController
from helper.Response import Response
from model.{model_name} import {model_name}

class {controller_name}(IController):
    def __init__(self):
        self.model = {model_name}

    def get(self, data):
        model = self.model()
        if "id" in data:
            result = model.single(int(data["id"]))
            if not result:
                return Response.bad_request("Item not found")
            return Response.success(result)
        return Response.success(model.list())

    def post(self, data):
        model = self.model()
        created = model.create(**data)
        if not created:
            return Response.bad_request(f"Failed to create: {model.error}")
        return Response.success({"success": "Created successfully"})

    def put(self, data):
        if "id" not in data:
            return Response.bad_request("ID is required")
        model = self.model()
        updated = model.update(data["id"], **data)
        if not updated:
            return Response.bad_request(f"Failed to update: {model.error}")
        return Response.success({"success": "Updated successfully"})

    def destroy(self, data):
        if "id" not in data:
            return Response.bad_request("ID is required")
        model = self.model()
        result = model.remove(data["id"])
        if not result:
            return Response.bad_request(f"Failed to destroy: {model.error}")
        return Response.success({"success": "Destroyed successfully"})'''
            },
            'model': {
                'basic': '''from table.{table_name} import {table_name}
from table.DBConnection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
from helper.FormatCheck import FormatCheck
from interface.IModel import IModel
from typing import Optional, List, Dict

class {model_name}(IModel):
    def __init__(self):
        self.Session = DBConnection.Session
        self.error = None

    def create(self, **data) -> bool:
        validation_result = self.__validateData(**data)
        if not validation_result:
            return False
        return self.__insert(**data)

    def single(self, id: int) -> Optional[{table_name}]:
        with self.Session() as session:
            try:
                return session.query({table_name}).filter_by(id=id).first()
            except SQLAlchemyError as e:
                self.error = f"Database failure: {str(e)}"
                return None

    def list(self) -> List[Dict]:
        with self.Session() as session:
            try:
                items = session.query({table_name}).all()
                return [item.to_dict() for item in items]
            except SQLAlchemyError as e:
                self.error = f"Database failure: {str(e)}"
                return None

    def update(self, id: int, **data) -> bool:
        with self.Session() as session:
            try:
                item = session.query({table_name}).filter_by(id=id).first()
                if not item:
                    self.error = "Item not found"
                    return False
                
                validation_result = self.__validateData(**data)
                if not validation_result:
                    return False
                
                for key, value in data.items():
                    setattr(item, key, value)
                session.commit()
                return True
            except SQLAlchemyError as e:
                session.rollback()
                self.error = f"Database Error: {str(e)}"
                return False

    def remove(self, id: int) -> bool:
        with self.Session() as session:
            try:
                item = session.query({table_name}).filter_by(id=id).first()
                if not item:
                    self.error = "Item not found"
                    return False
                
                session.delete(item)
                session.commit()
                return True
            except SQLAlchemyError as e:
                session.rollback()
                self.error = f"Database Error: {str(e)}"
                return False

    def __validateData(self, **data) -> bool:
        # Implement validation logic here
        return True

    def __insert(self, **data) -> bool:
        with self.Session() as session:
            try:
                new_item = {table_name}(**data)
                session.add(new_item)
                session.commit()
                return True
            except SQLAlchemyError as e:
                session.rollback()
                self.error = f"Database failure: {str(e)}"
                return False'''
            },
            'table': {
                'basic': '''from sqlalchemy import Column, Integer, String, Float, DateTime
from table.DBConnection import Base
from datetime import datetime

class {table_name}(Base):
    __tablename__ = '{table_name_lower}'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }'''
            }
        }
        self.vscode = VSCodeIntegration()
        self.pattern_recognition = PatternRecognition()
        
    def analyze_codebase(self, root_dir: str):
        """Analyzes the project codebase to understand patterns and relationships."""
        for pattern in ['controller/*.py', 'model/*.py', 'table/*.py', 'helper/*.py', 'interface/*.py']:
            files = Path(root_dir).glob(pattern)
            for file in files:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self._analyze_file(content, file.name, pattern.split('/')[0])
                    # Analyze patterns
                    self.pattern_recognition.analyze_patterns(content, pattern.split('/')[0])
        
        # Generate VS Code snippets
        self.vscode.generate_snippets(self.patterns)

    def _analyze_file(self, content: str, filename: str, category: str):
        """Analyzes a single file to extract patterns and relationships."""
        # Convert category to plural form if needed
        category = category + 's' if not category.endswith('s') else category
        
        if category not in self.project_structure:
            self.project_structure[category] = {}
            
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                self.project_structure[category][node.name] = {
                    'methods': self._get_class_methods(node),
                    'parent_class': self._get_parent_class(node),
                    'imports': self._get_imports(tree)
                }
                
                # Add completions for VS Code
                self.vscode.add_completion(
                    node.name,
                    self.patterns.get(category, {}).get('basic', ''),
                    f"Create new {category} {node.name}"
                )

    def suggest_code(self, context: str, current_file: str) -> str:
        """Suggests code based on the current context and file."""
        file_type = self._get_file_type(current_file)
        
        # Get suggestions from pattern recognition
        try:
            suggestions = self.pattern_recognition.suggest_improvements(context, file_type)
        except SyntaxError:
            # If context is not valid Python code, return a basic suggestion
            if 'controller' in file_type.lower():
                return self.patterns['controller']['basic']
            elif 'model' in file_type.lower():
                return self.patterns['model']['basic']
            elif 'table' in file_type.lower():
                return self.patterns['table']['basic']
            return "# No suggestions available for this context"
        
        # Add VS Code diagnostics for suggestions
        for suggestion in suggestions:
            self.vscode.add_diagnostic(
                current_file,
                1,  # Line number (you might want to make this more specific)
                suggestion['message'],
                suggestion['severity']
            )
        
        if 'Controller.py' in current_file:
            return self._suggest_controller_code(context)
        elif 'Model.py' in current_file:
            return self._suggest_model_code(context)
        elif 'Table.py' in current_file:
            return self._suggest_table_code(context)
        return "# No suggestions available for this context"

    def _get_file_type(self, filename: str) -> str:
        """Determines the file type based on filename."""
        if 'Controller' in filename:
            return 'controller'
        elif 'Model' in filename:
            return 'model'
        elif 'Table' in filename:
            return 'table'
        return 'unknown'

    def generate_crud_endpoints(self, resource_name: str) -> Dict[str, str]:
        """Generates complete CRUD endpoints for a resource."""
        model_name = f"{resource_name.capitalize()}"
        controller_name = f"{resource_name.capitalize()}Controller"
        table_name = f"{resource_name.capitalize()}"
        
        try:
            # Debug: Print the structure of patterns
            print("Patterns structure:", {k: list(v.keys()) for k, v in self.patterns.items()})
            
            # Get the basic patterns
            controller_pattern = self.patterns['controller']['basic']
            model_pattern = self.patterns['model']['basic']
            table_pattern = self.patterns['table']['basic']
            
            # Format each pattern with the correct variables
            generated_code = {
                'controller': controller_pattern.replace('{model_name}', model_name).replace('{controller_name}', controller_name),
                'model': model_pattern.replace('{model_name}', model_name).replace('{table_name}', table_name),
                'table': table_pattern.replace('{table_name}', table_name).replace('{table_name_lower}', resource_name.lower())
            }
            return generated_code
        except KeyError as e:
            print(f"Error: Missing pattern key - {e}")
            print("Available patterns:", list(self.patterns.keys()))
            return {
                'controller': '',
                'model': '',
                'table': ''
            }
        except Exception as e:
            print(f"Error formatting patterns: {e}")
            print("Pattern content:", {k: v['basic'] for k, v in self.patterns.items()})
            return {
                'controller': '',
                'model': '',
                'table': ''
            }

    def generate_documentation(self, file_type: str) -> str:
        """Generates documentation based on recognized patterns."""
        return self.pattern_recognition.generate_documentation(file_type)

    def _suggest_controller_code(self, context: str) -> str:
        """Suggests controller-specific code."""
        if 'def get' in context.lower():
            return self._suggest_get_method()
        elif 'def post' in context.lower():
            return self._suggest_post_method()
        elif 'def put' in context.lower():
            return self._suggest_put_method()
        elif 'def destroy' in context.lower():
            return self._suggest_destroy_method()
        return self.patterns['controller']['basic']

    def _suggest_model_code(self, context: str) -> str:
        """Suggests model-specific code."""
        if 'def create' in context.lower():
            return self._suggest_create_method()
        elif 'def update' in context.lower():
            return self._suggest_update_method()
        elif 'def remove' in context.lower():
            return self._suggest_remove_method()
        return self.patterns['model']['basic']

    def _suggest_table_code(self, context: str) -> str:
        """Suggests table-specific code."""
        return self.patterns['table']['basic']

    def _get_class_methods(self, node: ast.ClassDef) -> List[str]:
        """Extracts method names from a class definition."""
        return [n.name for n in node.body if isinstance(n, ast.FunctionDef)]

    def _get_parent_class(self, node: ast.ClassDef) -> Optional[str]:
        """Extracts the parent class name if any."""
        if node.bases:
            return node.bases[0].id if isinstance(node.bases[0], ast.Name) else None
        return None

    def _get_imports(self, tree: ast.AST) -> List[str]:
        """Extracts import statements from the AST."""
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(n.name for n in node.names)
            elif isinstance(node, ast.ImportFrom):
                imports.append(f"{node.module}.{node.names[0].name}")
        return imports

    def _suggest_get_method(self) -> str:
        return '''def get(self, data):
        model = self.model()
        if "id" in data:
            result = model.single(int(data["id"]))
            if not result:
                return Response.bad_request("Item not found")
            return Response.success(result)
        return Response.success(model.list())'''

    def _suggest_post_method(self) -> str:
        return '''def post(self, data):
        model = self.model()
        created = model.create(**data)
        if not created:
            return Response.bad_request(f"Failed to create: {model.error}")
        return Response.success({"success": "Created successfully"})'''

    def _suggest_put_method(self) -> str:
        return '''def put(self, data):
        if "id" not in data:
            return Response.bad_request("ID is required")
        model = self.model()
        updated = model.update(data["id"], **data)
        if not updated:
            return Response.bad_request(f"Failed to update: {model.error}")
        return Response.success({"success": "Updated successfully"})'''

    def _suggest_destroy_method(self) -> str:
        return '''def destroy(self, data):
        if "id" not in data:
            return Response.bad_request("ID is required")
        model = self.model()
        result = model.remove(data["id"])
        if not result:
            return Response.bad_request(f"Failed to destroy: {model.error}")
        return Response.success({"success": "Destroyed successfully"})''' 