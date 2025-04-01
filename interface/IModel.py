from abc import ABC,abstractmethod

class IModel(ABC):

    @abstractmethod
    def create()->None|object:
        pass

    @abstractmethod
    def update()->None|object:
        pass
    
    @abstractmethod
    def single(id :int)->None|object:
        pass

    @abstractmethod
    def remove(id : int)->bool:
        pass

    @abstractmethod
    def list()->None|list:
        pass
    
