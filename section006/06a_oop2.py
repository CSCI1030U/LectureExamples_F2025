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

# coding exercise 06a.1

class Pet:
    def __init__(self, name: str, breed: str, mass: float, gender: str) -> None:
        self.name = name
        self.breed = breed 
        self.mass = mass
        self.gender = gender
    
    # def speak(self) -> None:
    #     print(f'{self.name}: Speaks')

class Dog(Pet):
    def speak(self) -> None:
        print(f'{self.name}: Woof!')

class Cat(Pet):
    def speak(self) -> None:
        print(f'{self.name}: Meow!')

pets = [
    Dog('Rufus', 'Husky', 8.0, 'female'),
    Cat('Boots', 'Long hair', 3.2, 'male')
]
for pet in pets:
    pet.speak()

# coding exercise 06a.2

class Product:
    def __init__(self, price: float, description: str) -> None:
        self.price = price
        self.description = description
    
    def __repr__(self) -> str:
        return f'{self.description} (${self.price:0.2f})'

class Shoe(Product):
    def __init__(self, price: float, description: str, brand: str, size: float, colour: str) -> None:
        super().__init__(price, description)
        self.brand = brand
        self.size = size
        self.colour = colour
    
    def __repr__(self) -> str:
        return f'{self.brand} {self.description} {self.size} (${self.price:0.2f})'

products = [
    Product(price=79.99, description='Top Hat'),
    Product(price=275.00, description='Luxury Coat'),
    Shoe(price=899.99, description="'91 Classic Air Jordans", brand='Nike', size=12.0, colour='white'),
    Shoe(price=2.99, description="Temu Classic Shoe", brand='Nuke', size=12.0, colour='white'),
]

for prod in products:
    print(f'{prod = }')