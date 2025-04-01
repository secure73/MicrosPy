from typing import Dict, List, Optional, Any
import ast
from pathlib import Path
import re
from collections import defaultdict

class PatternRecognition:
    def __init__(self):
        self.patterns = defaultdict(list)
        self.relationships = defaultdict(list)
        self.common_practices = defaultdict(int)
        self.naming_conventions = defaultdict(list)
        
    def analyze_patterns(self, file_content: str, file_type: str) -> None:
        """Analyzes code patterns in the given file content."""
        tree = ast.parse(file_content)
        
        # Analyze method patterns
        self._analyze_method_patterns(tree, file_type)
        
        # Analyze error handling patterns
        self._analyze_error_handling(tree, file_type)
        
        # Analyze naming conventions
        self._analyze_naming_conventions(tree, file_type)
        
        # Analyze relationships
        self._analyze_relationships(tree, file_type)
    
    def _analyze_method_patterns(self, tree: ast.AST, file_type: str) -> None:
        """Analyzes common method patterns."""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                pattern = self._extract_method_pattern(node)
                self.patterns[file_type].append({
                    'name': node.name,
                    'pattern': pattern,
                    'args': [arg.arg for arg in node.args.args],
                    'decorators': [d.id for d in node.decorator_list if isinstance(d, ast.Name)]
                })
    
    def _analyze_error_handling(self, tree: ast.AST, file_type: str) -> None:
        """Analyzes error handling patterns."""
        for node in ast.walk(tree):
            if isinstance(node, ast.Try):
                handlers = []
                for handler in node.handlers:
                    if isinstance(handler.type, ast.Name):
                        handlers.append(handler.type.id)
                self.patterns[f"{file_type}_error_handling"].append({
                    'exceptions': handlers,
                    'has_finally': bool(node.finalbody),
                    'has_else': bool(node.orelse)
                })
    
    def _analyze_naming_conventions(self, tree: ast.AST, file_type: str) -> None:
        """Analyzes naming conventions."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                self.naming_conventions[f"{file_type}_class"].append(node.name)
            elif isinstance(node, ast.FunctionDef):
                self.naming_conventions[f"{file_type}_method"].append(node.name)
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                self.naming_conventions[f"{file_type}_variable"].append(node.id)
    
    def _analyze_relationships(self, tree: ast.AST, file_type: str) -> None:
        """Analyzes relationships between components."""
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(n.name for n in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
        self.relationships[file_type].extend(imports)
    
    def _extract_method_pattern(self, node: ast.FunctionDef) -> Dict[str, Any]:
        """Extracts the pattern of a method."""
        return {
            'has_try_except': any(isinstance(n, ast.Try) for n in ast.walk(node)),
            'returns_response': any(
                isinstance(n, ast.Return) and 
                isinstance(n.value, ast.Call) and 
                hasattr(n.value.func, 'attr') and 
                'Response' in n.value.func.attr
                for n in ast.walk(node)
            ),
            'uses_session': any(
                isinstance(n, ast.With) and 
                'Session' in ast.unparse(n.items[0])
                for n in ast.walk(node)
            ),
            'validates_input': any(
                isinstance(n, ast.Call) and 
                hasattr(n.func, 'attr') and 
                'validate' in n.func.attr.lower()
                for n in ast.walk(node)
            )
        }
    
    def suggest_improvements(self, file_content: str, file_type: str) -> List[Dict[str, str]]:
        """Suggests improvements based on recognized patterns."""
        suggestions = []
        
        # Analyze the current file
        tree = ast.parse(file_content)
        
        # Check for missing error handling
        if not any(isinstance(n, ast.Try) for n in ast.walk(tree)):
            suggestions.append({
                'type': 'error_handling',
                'message': 'Consider adding error handling using try-except blocks',
                'severity': 'suggestion'
            })
        
        # Check for input validation
        if file_type == 'controller' and not any(
            isinstance(n, ast.Call) and 
            hasattr(n.func, 'attr') and 
            'validate' in n.func.attr.lower()
            for n in ast.walk(tree)
        ):
            suggestions.append({
                'type': 'validation',
                'message': 'Add input validation for request data',
                'severity': 'warning'
            })
        
        # Check for proper response handling
        if file_type == 'controller' and not any(
            isinstance(n, ast.Return) and 
            isinstance(n.value, ast.Call) and 
            hasattr(n.value.func, 'attr') and 
            'Response' in n.value.func.attr
            for n in ast.walk(tree)
        ):
            suggestions.append({
                'type': 'response',
                'message': 'Use Response helper for consistent API responses',
                'severity': 'warning'
            })
        
        return suggestions
    
    def get_common_patterns(self, file_type: str) -> Dict[str, Any]:
        """Returns common patterns for the given file type."""
        return {
            'method_patterns': self.patterns.get(file_type, []),
            'error_handling': self.patterns.get(f"{file_type}_error_handling", []),
            'naming_conventions': {
                'classes': self.naming_conventions.get(f"{file_type}_class", []),
                'methods': self.naming_conventions.get(f"{file_type}_method", []),
                'variables': self.naming_conventions.get(f"{file_type}_variable", [])
            },
            'relationships': self.relationships.get(file_type, [])
        }
    
    def generate_documentation(self, file_type: str) -> str:
        """Generates documentation based on recognized patterns."""
        patterns = self.get_common_patterns(file_type)
        
        doc = f"# {file_type.capitalize()} Patterns\n\n"
        
        # Method patterns
        doc += "## Common Method Patterns\n"
        for pattern in patterns['method_patterns']:
            doc += f"- {pattern['name']}\n"
            doc += f"  - Arguments: {', '.join(pattern['args'])}\n"
            doc += f"  - Decorators: {', '.join(pattern['decorators'])}\n"
            doc += f"  - Characteristics:\n"
            for key, value in pattern['pattern'].items():
                doc += f"    - {key.replace('_', ' ').title()}: {value}\n"
        
        # Error handling
        doc += "\n## Error Handling Patterns\n"
        for pattern in patterns['error_handling']:
            doc += f"- Handles exceptions: {', '.join(pattern['exceptions'])}\n"
            doc += f"  - Has finally block: {pattern['has_finally']}\n"
            doc += f"  - Has else block: {pattern['has_else']}\n"
        
        # Naming conventions
        doc += "\n## Naming Conventions\n"
        for category, names in patterns['naming_conventions'].items():
            doc += f"### {category.title()}\n"
            doc += "- " + "\n- ".join(names) + "\n"
        
        # Relationships
        doc += "\n## Component Relationships\n"
        doc += "- " + "\n- ".join(patterns['relationships']) + "\n"
        
        return doc 