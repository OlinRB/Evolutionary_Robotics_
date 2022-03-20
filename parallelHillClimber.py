
from solution import SOLUTION
import constants as c
import copy
class PARELLEL_HILL_CLIMBER:


    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        # self.parent = SOLUTION()

    def Print(self):
        print("\nParent fitness: {}, Child fitness: {}\n".format(self.parent.fitness, self.child.fitness))

    def Evolve_For_One_Generation(self,mode):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate(mode)

        self.Print()

        self.Select()

    def Evolve(self):
        for parent in self.parents:
            self.parent = self.parents[parent]
            self.parent.Evaluate("GUI")
            print("\nParent fitness: {}".format(self.parent.fitness))

            for currentGeneration in range(c.numberOfGenerations):
                if currentGeneration == c.numberOfGenerations-1:
                    self.Evolve_For_One_Generation("DIRECT")
                else:
                    self.Evolve_For_One_Generation("DIRECT")
            self.Show_Best()

    def Show_Best(self):
        #pass
        self.Evolve_For_One_Generation("GUI")
        #print("Parent Fitness: {}".format(self.parent.fitness))


    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1

    def Mutate(self):
        self.parent.Mutate()


    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child
