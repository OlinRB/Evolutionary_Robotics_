
from solution import SOLUTION
import constants as c
import copy
import os
class PARELLEL_HILL_CLIMBER:


    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Print(self):
        print("\nParent fitness: {}, Child fitness: {}\n".format(self.parent.fitness, self.child.fitness))

    def Evolve_For_One_Generation(self,mode):

        self.Spawn()
        #
        # self.Mutate()
        #
        # self.child.Evaluate(mode)
        #
        # self.Print()
        #
        # self.Select()

    def Evolve(self):
        self.Evaluate(self.parents)

        for parent in self.parents:
            self.parent = self.parents[parent]
            for currentGeneration in range(c.numberOfGenerations):
                self.Evolve_For_One_Generation("DIRECT")
                # self.parent.Start_Simulation("GUI")
            #self.Show_Best()

    def Show_Best(self):
        #pass
        self.Evolve_For_One_Generation("GUI")
        #print("Parent Fitness: {}".format(self.parent.fitness))


    def Spawn(self):
        self.children = {}
        for i in range(len(self.parents)):
            self.child = copy.deepcopy(self.parents[i])
            self.child.Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            self.children[i] = self.child


    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()


    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child


    def Evaluate(self, solutions):
        for parent in solutions:
            self.parent = self.parents[parent]
            self.parent.Start_Simulation("GUI")

        for parent in solutions:
            self.parent = self.parents[parent]
            self.parent.Wait_For_Simulation_To_End()
