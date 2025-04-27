"""
Ejercicio 4 ISP:  Segregaciòn de interfaces
"""

from abc  import ABC , abstractmethod

class Animal(ABC):
 
    def species (self):
        pass


class Walkable(ABC):
    
    def walk(self):
        pass

class Swimmable(ABC):
   
    def swim(self):
        pass

class Flyable(ABC):
   
    def fly(self):
        pass

class Dog(Animal, Walkable, Swimmable):
    def species(self):
        return "Perro"
    
    def walk(self):
        return "Camina en 4 patas"
    
    def swim(self):
        return "Puede nadar"


dog = Dog()
print(f"Animal de especie: {dog.species()}")
print(dog.walk())
print(dog.swim())
