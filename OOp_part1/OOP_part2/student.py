class student:

    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks

    def set_marks(self,student_marks):
        if student_marks >= 0 and student_marks <= 100:
            self.__marks = student_marks
        else:
            print('Marks must be greater than 0 under in 100: ')

    def get_marks(self):
        return self.__marks

    def display_result(self):
        print('Student name is',self.__name)
        if  self.__marks >= 50:
            print('Resylt: Pass ')
        else:
            print('Result: Fail ')

obj = student('akash',10)
obj.set_marks(90)
obj.get_marks()
obj.display_result()
