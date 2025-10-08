# 05b - OOP 1

class Undergraduate_Course:
    def __init__(self):
        # self.set_course_code('')
        pass
    
    def __init__(self, course_code):
        self.set_course_code(course_code)

    def get_course_code(self):
        return self.course_code
    
    def set_course_code(self, course_code):
        self.course_code = course_code

cs1030 = Undergraduate_Course()
cs1030.set_course_code('CSCI1030U')

cs1060 = Undergraduate_Course(course_code="CSCI1060U")

