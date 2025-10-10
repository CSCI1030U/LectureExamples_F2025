# 06a - OOP 2

class Pet:
    def __init__(self, name: str, mass: float) -> None:
        self.name = name
        self.mass = mass
    
    def __repr__(self):
        return f'{self.name} ({self.mass} kg)'
    
    def __lt__(self, other) -> bool:
        return self.mass < other.mass

class Cat(Pet):
    def speak(self):
        print(f'{self.name}: Meow')

class Dog(Pet):
    def speak(self):
        print(f'{self.name}: Woof')

simba = Cat('Simba', 4.0)
boots = Dog('Boots', 30.0)

simba.speak()
boots.speak()
print(f'{simba = }')
