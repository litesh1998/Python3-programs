class Student:
    s=10
    @staticmethod
    def mod():
        Student.s+=1
        print(Student.s)
    '''def __init__(self):
        self.x=1
    @classmethod
    def mod(cls):
        cls.x+=1'''
s1=Student()
s2=Student()
s1.mod()
print(Student.s)