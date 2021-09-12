class human:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=a+d
        self.c=a*c
        self.d=a+b

h1 = human(10,20,30,40)
h2 = human(25,21,34,56)

print(h1.__dict__)
print(h2.__dict__)
