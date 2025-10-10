# 05b - OOP 1

class Undergraduate_Course:
    def __init__(self, course_code, description):
        self.set_course_code(course_code)
        self.__description = description

    def get_course_code(self):
        return self.__course_code
    
    def set_course_code(self, course_code):
        self.__course_code = course_code
    
    def __repr__(self):
        return f'{self.__course_code} ({self.__description})'

    def __lt__(self, other):
        # <
        # if self.get_course_code() < other.get_course_code():
        #     return True 
        # else:
        #     return False 
        return self.get_course_code() < other.get_course_code()

cs1030 = Undergraduate_Course('CS1030', "Intro to CS")
cs1030.set_course_code('CSCI1030U')
cs1030.__course_code = ''

print(f'{str(cs1030) = }')


cs1060 = Undergraduate_Course(course_code="CSCI1060U", description='Programming Workshop I')
print(f'{cs1030 = }')
print(f'{cs1060 = }')
print(f'{cs1030 < cs1060 = }')

# coding exercise 05b.1

class Cat:
    def __init__(self, name: str, mass: float) -> None:
        self.name = name
        self.mass = mass
    
    def __repr__(self):
        return f'{self.name} ({self.mass} kg)'
    
    def __lt__(self, other) -> bool:
        return self.mass < other.mass

lenny = Cat('Lenny', 0.8)
po = Cat('Po', 2.0)
print(f'{lenny = }')
print(f'{po = }')
print(f'{lenny < po = }')
