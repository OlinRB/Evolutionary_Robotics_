import time

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
            print(i) # Sometimes spawns empty pybullet window
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Print(self):
        for i in range(len(self.parents)):
            print("\n\nParent{} fitness: {}, Child{} fitness: {}\n".format(i,self.parents[i].fitness, i, self.children[i].fitness))

    def Evolve_For_One_Generation(self,mode):

        self.Spawn()
        #
        self.Mutate()
        #
        self.Evaluate(self.children)
        #
        self.Print()
        #
        self.Select()

    def Evolve(self):
        self.Evaluate(self.parents)
        for parent in self.parents:
            self.parent = self.parents[parent]
            for currentGeneration in range(c.numberOfGenerations):
                self.Evolve_For_One_Generation("DIRECT")

    def Show_Best(self):
        best = 0
        bestIdx = 0
        for parent in self.parents:
            if self.parents[parent].fitness > best:
                bestIdx = parent
                best = self.parents[parent].fitness

        # Show best sim
        self.parents[bestIdx].Start_Simulation("GUI")


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
        for index in self.parents:
            if self.children[index].fitness > self.parents[index].fitness:
                self.parents[index] = self.children[index]



        if self.child.fitness > self.parent.fitness:
            self.parent = self.child


    def Evaluate(self, solutions):

        for solution in solutions:
            solutions[solution].Start_Simulation("DIRECT")

        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

        # for parent in solutions:
        #     self.parent = self.parents[parent]
        #     self.parent.Wait_For_Simulation_To_End()
