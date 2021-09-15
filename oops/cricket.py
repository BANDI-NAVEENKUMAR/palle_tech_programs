class cricket:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

c1 = cricket('pant',24,100)
c2 = cricket('virat',32,140)
c3 = cricket('rohit',33,200)
c4 = cricket('rahul',27,170)

print(c1.__dict__)
print(c2.__dict__)
print(c3.__dict__)
print(c4.__dict__)