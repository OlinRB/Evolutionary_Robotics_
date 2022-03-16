
from solution import SOLUTION
import constants as c
import copy
class HILL_CLIMBER:


    def __init__(self):
        self.parent = SOLUTION()

    def Print(self):
        print("\nParent fitness: {}, Child fitness: {}\n".format(self.parent.fitness, self.child.fitness))

    def Evolve_For_One_Generation(self,mode):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate(mode)

        self.Print()

        self.Select()

    def Evolve(self):
        self.parent.Evaluate("GUI")
        print("\nParent fitness: {}".format(self.parent.fitness))

        for currentGeneration in range(c.numberOfGenerations):
            if currentGeneration == c.numberOfGenerations-1:
                self.Evolve_For_One_Generation("GUI")
            else:
                self.Evolve_For_One_Generation("DIRECT")

    def Show_Best(self):
        self.Spawn()
        self.Mutate()
        self.parent.Evaluate("GUI")
        self.Print()


    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.parent.Mutate()


    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child
