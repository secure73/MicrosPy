from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from pathlib import Path
import importlib
import sys
import os

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from typing import List, Type, Dict
from table.DBConnection import Base, DBConnection

class DatabaseMigration:
    def __init__(self):
        self.engine = DBConnection.engine
        self.migration_summary = {
            'created_tables': [],
            'new_columns': {},
            'removed_columns': {}
        }
        
    def get_all_tables(self) -> List[str]:
        """Get all existing tables in the database."""
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))
            return [row[0] for row in result]
    
    def get_table_columns(self, table_name: str) -> List[str]:
        """Get all columns in a specific table."""
        with self.engine.connect() as conn:
            result = conn.execute(text(f"PRAGMA table_info({table_name})"))
            return [row[1] for row in result]
    
    def import_table_models(self) -> List[Type]:
        """Import all table models from the table directory."""
        table_models = []
        table_dir = Path(project_root) / "table"
        
        # Import all Python files in the table directory
        for file in table_dir.glob("*.py"):
            if file.name.startswith("__"):
                continue
                
            try:
                # Convert file path to module path
                relative_path = file.relative_to(project_root)
                module_name = str(relative_path.with_suffix('')).replace(os.sep, '.')
                
                # Import the module
                module = importlib.import_module(module_name)
                
                # Find all classes that have __tablename__
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and hasattr(attr, '__tablename__'):
                        table_models.append(attr)
                        
            except ImportError as e:
                print(f"❌ Error importing {file.name}: {e}")
            except Exception as e:
                print(f"❌ Unexpected error with {file.name}: {e}")
        
        return table_models
    
    def create_missing_tables(self) -> None:
        """Create any missing tables in the database."""
        try:
            # Get all table models
            table_models = self.import_table_models()
            
            if not table_models:
                print("⚠️ No table models found!")
                return
                
            # Get existing tables
            existing_tables = self.get_all_tables()
            
            # Create tables that don't exist
            for model in table_models:
                if model.__tablename__ not in existing_tables:
                    print(f"📝 Creating table: {model.__tablename__}")
                    model.__table__.create(self.engine)
                    self.migration_summary['created_tables'].append(model.__tablename__)
            
            if self.migration_summary['created_tables']:
                print("\n✅ Tables created successfully:")
                for table in self.migration_summary['created_tables']:
                    print(f"  - {table}")
            else:
                print("\n✓ No new tables needed to be created.")
            
        except SQLAlchemyError as e:
            print(f"❌ Error during migration: {e}")
            raise
    
    def check_column_changes(self) -> None:
        """Check for any column changes in existing tables."""
        table_models = self.import_table_models()
        
        if not table_models:
            return
            
        for model in table_models:
            if model.__tablename__ in self.get_all_tables():
                existing_columns = self.get_table_columns(model.__tablename__)
                model_columns = [col.name for col in model.__table__.columns]
                
                # Check for new columns
                new_columns = set(model_columns) - set(existing_columns)
                if new_columns:
                    print(f"\nDetected new columns in {model.__tablename__}:")
                    for col in new_columns:
                        print(f"  + {col}")
                    self.migration_summary['new_columns'][model.__tablename__] = list(new_columns)
                
                # Check for removed columns
                removed_columns = set(existing_columns) - set(model_columns)
                if removed_columns:
                    print(f"\nDetected removed columns in {model.__tablename__}:")
                    for col in removed_columns:
                        print(f"  - {col}")
                    self.migration_summary['removed_columns'][model.__tablename__] = list(removed_columns)
    
    def print_migration_summary(self) -> None:
        """Print a summary of all migration actions."""
        print("\n=== Migration Summary ===")
        
        if self.migration_summary['created_tables']:
            print("\n📦 Created Tables:")
            for table in self.migration_summary['created_tables']:
                print(f"  ✓ {table}")
        
        if self.migration_summary['new_columns']:
            print("\n📋 New Columns:")
            for table, columns in self.migration_summary['new_columns'].items():
                print(f"  Table: {table}")
                for col in columns:
                    print(f"    + {col}")
        
        if self.migration_summary['removed_columns']:
            print("\n🗑️ Removed Columns:")
            for table, columns in self.migration_summary['removed_columns'].items():
                print(f"  Table: {table}")
                for col in columns:
                    print(f"    - {col}")
        
        if not any(self.migration_summary.values()):
            print("\n✓ No changes were necessary. Database is up to date!")
    
    def migrate(self) -> None:
        """Run the complete migration process."""
        print("🚀 Starting database migration...")
        self.create_missing_tables()
        self.check_column_changes()
        self.print_migration_summary()
        print("🚀 Thanks from Ali Khorsandfard for using this micro python Framework, Enjoy!")
        print("\n✨ Migration process completed!") 