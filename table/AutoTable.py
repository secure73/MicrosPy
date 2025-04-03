from sqlalchemy import Column, Integer , String
from .DBConnection import Base

class AutoTable(Base):
    __tablename__ = "autos"

    id = Column(Integer , primary_key=True, autoincrement=True)
    name = Column(String,nullable=False)
    ps = Column(Integer,nullable=False)

    def __repr__(self):
        return f"Auto(id='{self.id}',name='{self.name}',ps='{self.ps}')"



