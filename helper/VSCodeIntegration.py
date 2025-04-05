from typing import Dict, List, Optional, Any
import json
from pathlib import Path
import re

class VSCodeIntegration:
    def __init__(self):
        self.snippets = {
            'controller': {},
            'authenticated_controller': {},
            'model': {},
            'table': {},
            'helper': {}
        }
        self.completions = []
        self.diagnostics = []
        
    def generate_snippets(self, patterns: Dict[str, Any]) -> None:
        """Generates VS Code snippets from code patterns."""
        for category, category_patterns in patterns.items():
            if category not in self.snippets:
                continue
                
            for pattern_name, pattern in category_patterns.items():
                snippet_name = f"micro_py_{category}_{pattern_name}"
                self.snippets[category][snippet_name] = {
                    "prefix": f"micro_{category}_{pattern_name}",
                    "body": pattern.split('\n'),
                    "description": f"Create a new {pattern_name} {category}"
                }
        self._save_snippets()
    
    def add_completion(self, trigger: str, content: str, detail: str) -> None:
        """Adds a completion item for VS Code IntelliSense."""
        self.completions.append({
            "label": trigger,
            "insertText": content,
            "detail": detail,
            "kind": 15  # Snippet
        })
        self._save_completions()
    
    def add_diagnostic(self, file_path: str, line: int, message: str, severity: str = "Warning") -> None:
        """Adds a diagnostic (warning/error) for VS Code."""
        self.diagnostics.append({
            "file": file_path,
            "line": line,
            "message": message,
            "severity": severity
        })
        self._save_diagnostics()
    
    def _save_snippets(self) -> None:
        """Saves snippets to VS Code snippets file."""
        snippets_dir = Path.home() / ".vscode" / "snippets"
        snippets_dir.mkdir(parents=True, exist_ok=True)
        
        for category, snippets in self.snippets.items():
            snippet_file = snippets_dir / f"micro_py_{category}.code-snippets"
            with open(snippet_file, 'w') as f:
                json.dump(snippets, f, indent=2)
    
    def _save_completions(self) -> None:
        """Saves completions for VS Code IntelliSense."""
        completion_file = Path(".vscode") / "micro_py.code-completion"
        with open(completion_file, 'w') as f:
            json.dump(self.completions, f, indent=2)
    
    def _save_diagnostics(self) -> None:
        """Saves diagnostics for VS Code Problems panel."""
        diagnostic_file = Path(".vscode") / "micro_py.code-diagnostic"
        with open(diagnostic_file, 'w') as f:
            json.dump(self.diagnostics, f, indent=2)
    
    def suggest_imports(self, file_content: str, file_type: str) -> List[str]:
        """Suggests imports based on file content and type."""
        suggestions = []
        if file_type == 'controller':
            if 'IController' not in file_content:
                suggestions.append('from interface.IController import IController')
            if 'Response' not in file_content:
                suggestions.append('from helper.Response import Response')
        elif file_type == 'model':
            if 'IModel' not in file_content:
                suggestions.append('from interface.IModel import IModel')
            if 'DBConnection' not in file_content:
                suggestions.append('from table.DBConnection import DBConnection')
            if 'SQLAlchemyError' not in file_content:
                suggestions.append('from sqlalchemy.exc import SQLAlchemyError')
        return suggestions
    
    def validate_structure(self, file_content: str, file_type: str) -> List[Dict[str, Any]]:
        """Validates file structure according to framework conventions."""
        issues = []
        if file_type == 'controller':
            if not re.search(r'class \w+\(IController\):', file_content):
                issues.append({
                    "message": "Controller must inherit from IController",
                    "severity": "Error"
                })
            required_methods = ['get', 'post', 'put', 'destroy']
            for method in required_methods:
                if f"def {method}" not in file_content:
                    issues.append({
                        "message": f"Controller missing required method: {method}",
                        "severity": "Warning"
                    })
        elif file_type == 'model':
            if not re.search(r'class \w+\(IModel\):', file_content):
                issues.append({
                    "message": "Model must inherit from IModel",
                    "severity": "Error"
                })
        return issues 