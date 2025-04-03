from table.UserTable import UserTable
from table.DBConnection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
import bcrypt
from helper.FormatCheck import FormatCheck
from interface.IModel import IModel
from sqlalchemy import update

class UserModel(IModel): 
    def __init__(self):
        self.Session = DBConnection.Session
        self.error = None
    
    def create(self,email:str, password:str , name: str)->None|bool:
        validation_result = self.__validateUserInfo(name=name,email=email)
        if not validation_result:
            return None
        if self.singleByEmail(email):
            self.error = "user already exists"
            return None
        #hashing password before insert into database
        hash_pass = self.__setPassword(password=password)
        if not hash_pass:
            return None
        return self.__insert(email,hash_pass,name)
         
    def single(self,id:int)->None|UserTable:
        with self.Session() as session:
            try:
                return session.query(UserTable).filter_by(id=id).first()
            except SQLAlchemyError as e:
                self.error = f"Database failure: {str(e)}"
                return None

    def list(self):
        # with ist ein Ansatz dass macht Resouces frei nach dem nutzung. SQL Alchemy empfehlt thise method
        with self.Session() as session:
            #session.query: ermöglich uns zu Sagen was genau brauchen wir von allem Spalten von Tabelle
            # all() ist method das bringt zurück all data in table. (select * ) 
            users  = session.query(UserTable).all()
            return [{"id":user.id , "name":user.name , "email":user.email , "password":user.password} for user in users] 
    
    def singleByEmail(self, email:str)->None|UserTable:
        with self.Session() as session:
            try:
                user = session.query(UserTable).filter_by(email=email).first()
                return {"id":user.id, "name":user.name , "email":user.email , "password":user.password} if user else None
            except SQLAlchemyError as e:
                self.error = f"Database failure: {str(e)}"
                return None

    def update(self, id: int, **data) -> None|object:
        user = self.single(id)
        if not user:
            self.error = "User not found"
            return None

        if 'name' in data:
            if not self.__validateUserInfo(name=data['name']):
                return None

        with self.Session() as session:
            try:
                if 'name' in data:
                    session.query(UserTable).filter(UserTable.id == id).update({
                        UserTable.name: data['name']
                    })

                if 'password' in data:
                    hashed_password = self.__setPassword(data['password'])
                    if not hashed_password:
                        return None
                    session.query(UserTable).filter(UserTable.id == id).update({
                        UserTable.password: hashed_password
                    })
                session.commit()
                return self.single(id)
            except SQLAlchemyError as e:
                session.rollback()
                self.error = f"Database Error: {str(e)}"
                return None

    def remove(self, id:int)->bool:
        user = self.single(id)
        if not user:
            self.error = "User not found"
            return False
        with self.Session() as session:
            try:
                session.delete(user)
                session.commit()
                return True
            except SQLAlchemyError as e:
                session.rollback()
                self.error = f"Database Error: {str(e)}"
                return False



#--------------------Private Methods ---------------------------------------

    def __validateUserInfo(self, name: str = None , email: str = None)->bool:
        if name:
            if not FormatCheck.minimumLength(name,2):
                self.error = "name length must have at least 2 characters"
                return False
        if email:
            if not FormatCheck.email(email=email):
                self.error = "your given email address doesn't follow email format, please check email address and try again"
                return False
        return True
    
    def __setPassword(self, password:str)->None|str:
        if not FormatCheck.minimumLength(password,6):
            self.error = "password length must have at least 6 characters"
            return None
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    def __insert(self,email:str, password:str , name: str)->bool:
        with self.Session() as session:
            try:
                new_user = UserTable(email=email,password=password,name=name)
                session.add(new_user)
            #method commit schreib änderungen in Datanbank , egal insert, update, oder delete . 
            # ohne commit , änderungen bleibt in session , und datenbank wurde Aktualiert nicht! 
                session.commit()
                return True
            except SQLAlchemyError as e:
                session.rollback()
                self.error = f"Database failure: {str(e)}"
                return False