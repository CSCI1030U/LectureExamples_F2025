# 06a - OOP 2

# Coding Exercise 06a.1
class Pet:
    def __init__(self, name: str, breed: str, mass: float, gender: str) -> None:
        self._name = name
        self._mass = mass 
        self._breed = breed 
        self._gender = gender
    
    def get_name(self) -> str:
        return self._name
    
    def get_mass(self) -> float:
        return self._mass

    def __repr__(self):
        return f'{self._name} ({self._mass} kg)'

    def __lt__(self, other):
        return self._mass < other._mass

class Cat(Pet):
    def speak(self) -> None:
        print(f'{self._name}: Meow!')

class Dog(Pet):
    # def __init__(self, name, breed, mass, gender):
    #     # Pet.__init__(self, name, mass)
    #     super().__init__(name, mass)
    #     self.__can_fetch = False
    
    # def __repr__(self):
    #     if self.__can_fetch:
    #         return f'{self._name} is a fetchy boy/girl'
    #     else:
    #         return f'{self._name} is still a good girl/boy'

    def speak(self) -> None:
        print(f'{self._name}: Woof!')

# teddy = Dog('Teddy', 30.0, False)
# print(f'{teddy = }')

pets = [
    Dog('Rufus', 'Husky', 8.0, 'female'),
    Cat('Boots', 'Long hair', 3.2, 'male')
]
for pet in pets:
    pet.speak()

# Rufus: Woof!
# Boots: Meow!

# coding exercise 06a.2

class Product:
    def __init__(self, price: float, description: str) -> None:
        self.price = price
        self.description = description
    
    def __repr__(self) -> str:
        return f'{self.description} ({self.price:0.2f})'

class Shoe(Product):
    def __init__(self, price: float, description: str, 
                 brand: str, size: float, colour: str) -> None:
        super().__init__(price, description)
        self.brand = brand 
        self.size = size 
        self.colour = colour
    
    def __repr__(self) -> str:
        return f'{self.brand} {self.description} (${self.price:0.2f})'

products = [
    Product(price=29.99, description='Black with metal belt'),
    Product(price=249.99, description='Green bowler hat'),
    Product(price=49.99, description='T-Shirt'),
    Shoe(price=99.99, description='Stiletto', brand='Nike', size=6.5, colour='Black'),
    Shoe(price=69.99, description='Joggers', brand='Louis Vitton', size=9.5, colour='White'),
    Shoe(price=84.99, description='High tops', brand='Reebok', size=10.5, colour='White'),
]

for prod in products:
    print(f'{prod = }')
