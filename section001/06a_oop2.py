# 06a - OOP 2

class Pet:
    def __init__(self, name: str, mass: float) -> None:
        self._name = name
        self._mass = mass 
    
    def get_name(self) -> str:
        return self._name
    
    def get_mass(self) -> float:
        return self._mass

    def __repr__(self):
        return f'{self._name} ({self._mass} kg)'

    def __lt__(self, other):
        return self._mass < other._mass

class Cat(Pet):
    pass 

class Dog(Pet):
    def __init__(self, name, mass, can_fetch):
        # Pet.__init__(self, name, mass)
        super().__init__(name, mass)
        self.__can_fetch = can_fetch
    
    def __repr__(self):
        if self.__can_fetch:
            return f'{self._name} is a fetchy boy/girl'
        else:
            return f'{self._name} is still a good girl/boy'
    
teddy = Dog('Teddy', 30.0, False)
print(f'{teddy = }')