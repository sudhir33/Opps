class Student:
    def __init__(self,name,phno,email):
        self.name=name
        self.phno=phno
        self.email=email
    def display_data(self):
        print(self.name,self.phno,self.email)

class EngStudent(Student):
    def __init__(self,rollno,branch,section,name,phno,email):
        super().__init__(name,phno,email)
        self.branch=branch
        self.rollno=rollno
        self.section=section
    def display_data(self):
        print(self.rollno,self.branch,self.section,self.name,self.phno,self.email)

class HighSchoolStudent(Student):
    def __init__(self,clas,grade,name,phno,email):
        super().__init__(name,phno,email)
        self.clas=clas
        self.grade=grade
    def display_data(self):
        print(self.clas,self.grade,self.name,self.phno,self.email)

hss1=HighSchoolStudent(9,'A','shiva','12345','shiva@gmail.com')
hss1.display_data()

s1=EngStudent(123,"CSE","A","sudhir","995172211","sudhir@gmailcom")
s1.display_data()





