
"""
 Ejercicio 3 sustitución de Liskov
"""
class Bird:
    def has_wings(self):
            return "Esta ave tiene alas"
    
class FlyingBird(Bird):
    def fly(self):
        return "Esta ave vuela"

class NonFlyingBird(Bird):
     def non_fly(self):
          return "Esta ave no puede volar" 

class Penguin(NonFlyingBird):
     def displace(self):
          return "Puede caminar o nadar"
    
    
penguin = Penguin()
print(penguin.has_wings())     
print(penguin.non_fly())
print(penguin.displace())  


