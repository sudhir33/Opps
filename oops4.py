from abc import ABC,abstractmethod

class Student(ABC):
    def fun3(self):
        pass
    @abstractmethod
    def fun1(self):
        pass
    @abstractmethod
    def fun2(self):
        pass

class Engistudent(Student):
    def fun1(self):
        pass
    def fun2(self):
        pass
    pass

s1=Engistudent()
