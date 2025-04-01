from sqlalchemy import Column, Integer , String
from .DBConnection import Base

class UserTable(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True, autoincrement=True)
    email = Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)
    name = Column(String,nullable=False)

    def __repr__(self):
        return f"User(id='{self.id}',email='{self.email}',password='{self.password}',name='{self.name}')"



