class cricket:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s1 = cricket('virat',33,90)
s2 = cricket('rohit',32,100)
s3 = cricket('pant',24,127)
s4 = cricket ('rahul',27,110)

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
print(s4.__dict__)

