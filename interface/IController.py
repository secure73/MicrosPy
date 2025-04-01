from abc import ABC,abstractmethod

class IController(ABC):

    @abstractmethod
    def post():
        pass

    @abstractmethod
    def put():
        pass
    
    @abstractmethod
    def destroy(id : int):
        pass

    @abstractmethod
    def get():
        pass