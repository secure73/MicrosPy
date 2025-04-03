from table.AutoTable import AutoTable
from table.DBConnection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
from interface.IModel import IModel
from helper.FormatCheck import FormatCheck

class AutoModel(IModel): 
    def __init__(self):
        self.Session = DBConnection.Session
        self.error = None
    
    def create(self,name:str, ps:int)->None|bool:
        validation_result = self.__validateData(name=name,ps=ps)
        if not validation_result:
            return None
        return self.__insert(name=name, ps=ps)
         
    def single(self,id:int)->None|dict:
        with self.Session() as session:
            try:
                auto = session.query(AutoTable).filter_by(id=id).first()
                if auto:
                    return {"id": auto.id, "name": auto.name, "ps": auto.ps}
                return None
            except SQLAlchemyError as e:
                self.error = f"Database failure: {str(e)}"
                return None

    def list(self):
        with self.Session() as session:
            try:
                autos = session.query(AutoTable).all()
                return [{"id":auto.id , "name":auto.name , "ps":auto.ps} for auto in autos]
            except SQLAlchemyError as e:
                self.error = f"Database failure: {str(e)}"
                return None

    def update(self, auto_id: int , name:str = None , ps: int = None)->AutoTable|None:
        auto = self.single(auto_id)
        if not auto:
            self.error = "Auto not found"
            return None
        
        validation_result = self.__validateData(name=name, ps=ps)
        if not validation_result:
            return None

        with self.Session() as session:
            try:
                if name:
                    session.query(AutoTable).filter(AutoTable.id == auto_id).update({
                        AutoTable.name:name
                    })
                if ps:
                    session.query(AutoTable).filter(AutoTable.id == auto_id).update({
                            AutoTable.ps:ps
                    })          
                session.commit()
                return self.single(auto_id)
            except SQLAlchemyError as e:
                session.rollback()
                self.error = f"Database Error: {str(e)}"
                return None

    def remove(self, id:int)->bool:
        auto = self.single(id)
        if not auto:
            self.error = f"Auto with ID {id} not found"
            return False
        with self.Session() as session:
            try:
                auto_to_delete = session.query(AutoTable).filter_by(id=id).first()
                if not auto_to_delete:
                    self.error = f"Auto with ID {id} not found"
                    return False
                session.delete(auto_to_delete)
                session.commit()
                return True
            except SQLAlchemyError as e:
                session.rollback()
                self.error = f"Database error: {str(e)}"
                return False

    def __validateData(self, name: str = None, ps: int = None) -> bool:
        if name and not FormatCheck.minimumLength(name, 2):
            self.error = "Name must be at least 2 characters long"
            return False
        if ps is not None and not isinstance(ps, int):
            self.error = "PS must be a number"
            return False
        if ps is not None and ps <= 0:
            self.error = "PS must be greater than 0"
            return False
        return True
    
    def __insert(self, name: str, ps: int) -> bool:
        with self.Session() as session:
            try:
                new_auto = AutoTable(name=name, ps=ps)
                session.add(new_auto)
                session.commit()
                return True
            except SQLAlchemyError as e:
                session.rollback()
                self.error = f"Database failure: {str(e)}"
                return False