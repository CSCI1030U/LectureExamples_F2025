# 05b - OOP 1

class Student:
    def __init__(self, sid):
        self.set_sid(sid)
        
    def get_sid(self):
        return self.__sid 
    
    def set_sid(self, sid):
        self.__sid = sid

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name 

    def __repr__(self):
        return f'{self.__name} ({self.__sid})'
    
    # def __str__(self):
    #     return f'{self.__name} ({self.__sid})'
    
student1 = Student('100000001')
student1.set_name('Carla Rodriguez')
# print(f'{student1.__sid = }') # information hiding
print(f'{student1.get_sid() = }')
student1.__init__('another sid')
print(f'{student1.get_sid() = }')
print(f'{student1 = }')
print(student1)

# coding exercise 05b.1

class Cat:
    def __init__(self, name: str, mass: float) -> None:
        self.__name = name
        self.__mass = mass 
    
    def get_name(self) -> str:
        return self.__name
    
    def get_mass(self) -> float:
        return self.__mass

    def __repr__(self):
        return f'{self.__name} ({self.__mass} kg)'

    def __lt__(self, other):
        return self.__mass < other.__mass

lenny = Cat('Lenny', 0.8)
lightning = Cat('Lightning', 5.0)

print(f'{lenny = }')
print(f'{lightning = }')
print(f'{lenny < lightning = }')

cats = [
    Cat('AlsoLenny', 0.8),
    Cat('AlsoLightning', 5.0)
]
print(f'{cats[0] = }')
print(f'{cats[1] = }')
