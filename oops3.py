class Student:
    def __init__(self,marks,branch,grade):
        self.marks=marks
        self.branch=branch
        self.grade=grade
    def display_data(self):
        print(self.marks,self.branch,self.grade)

class SportsPerson:
    def __init__(self,gametype,awards):
        self.gametype=gametype
        self.awards=awards
    def display_data(self):
        print(self.gametype,self.awards)
    

class Person(Student,SportsPerson):
    def __init__(self,name,phno,email,marks,branch,grade,gametype,awards):
        super().__init__(marks,branch,grade)
        SportsPerson.__init__(self,gametype,awards)
        self.name=name
        self.phno=phno
        self.email=email
    def display_data(self):
        super().display_data()
        SportsPerson.display_data(self)
        print(self.name,self.phno,self.email)


s1=Person("sudhir",123456,"sudhir@gmail.com",60,'B','C',"cricket",2)
s1.display_data()











    
