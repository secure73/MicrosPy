#sqlalchemy ist eine Mächtige Python Library , Arbeitet mit Relational Database
#create_engine : ist verantwürtlich für connection zum Database zu Verwalten , generieren und schließen
from sqlalchemy import create_engine 

#sqlalchemy.orl ist Object relational mapper (mapping) welch arbeitet mit connection das connection_engine vorbereitet 
#decrative_base : baut rine globale Base class , dass arbitet als interface Zwischen Python Objects and ORM
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class DBConnection:
    try:
        engine = create_engine("sqlite:///db.db" ,echo=False)
        #engine = create_engine("mysql+pymsql://roor@localhost:3306/project_db") beispiel für mysql oder mariadb
    except Exception as e:
        print(f"failure bei connect to db {e}")

    Session = sessionmaker(bind=engine)

    @classmethod
    def create_all(cls):
        Base.metadata.create_all(cls)
    
    @classmethod
    def get_session(cls):
        return cls.Session()



