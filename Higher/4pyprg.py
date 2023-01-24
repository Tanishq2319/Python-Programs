class newone():
    def __init__(self,name,DateOfBirth,number,address):
        self.name=name
        self.DateOfBirth=DateOfBirth
        self.number=number
        self.address=address
class second(newone):
    def __init__(self,name,DateOfBirth,number,address,SatScore):
        newone.__init__(self,name,DateOfBirth,number,address)
        self.SatScore=SatScore
x=second("tanishq",27-12-2001,8077455815,"agra",5002)
print("student name=",x.name)
print("student contact number=",x.number)
print("students date of birth=",x.DateOfBirth)
print("students address=",x.address)