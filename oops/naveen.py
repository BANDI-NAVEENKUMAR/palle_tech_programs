class naveen:
    def __init__(self,name,village,age,course,games,):
        self.name = name
        self.village = village
        self.course = course
        self.games = games

n1 = naveen('bandi','matli',23,'MCA','cricket')

print(n1.__dict__)