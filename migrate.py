from helper.DatabaseMigration import DatabaseMigration

def main():
    print("Starting database migration...")
    migrator = DatabaseMigration()
    migrator.migrate()

if __name__ == "__main__":
    main() 