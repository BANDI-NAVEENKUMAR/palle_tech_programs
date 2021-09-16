class goals:
    def __init__(self,name,prevgoals):
        self.name = name
        self.prevgoals = prevgoals
        self.currentgoals = 0
        self.totalgoals = self.prevgoals + self.currentgoals

    def make_goal(self):
        self.currentgoals = self.currentgoals + 1
        self.totalgoals = self.totalgoals + 1

g1 = goals("naveen",100)
g2 = goals("cricket",77)
g1.make_goal()
g1.make_goal()
g1.make_goal()
g2.make_goal()
print(g1.__dict__)
print(g2.__dict__)

