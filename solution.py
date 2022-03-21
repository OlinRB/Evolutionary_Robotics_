import time

import numpy

import pyrosim.pyrosim as pyrosim
from constants import*
import random
import os

length = 1
width = 1
height = 1

class SOLUTION:

    def __init__(self, myID):
        self.myID = myID
        self.weights = [[numpy.random.rand(),numpy.random.rand()],
                        [numpy.random.rand(),numpy.random.rand()],
                        [numpy.random.rand(),numpy.random.rand()]]

        for row in self.weights:
            for i in range(len(row)):
                row[i] = row[i] * 2 - 1

        # self.weights * 2 - 1

    # def Evaluate(self, GUI):
    #     self.Create_World()
    #     self.Create_Body()
    #     self.Create_Brain()
    #     os.system("start /B python simulate.py {} {}".format(GUI, self.myID))
    #     while not os.path.exists('fitness{}.txt'.format(self.myID)):
    #         time.sleep(0.01)
    #     with open('fitness{}.txt'.format(self.myID), 'r') as f:
    #         result = f.readline()
    #         result = float(result)
    #     self.fitness = result

    def Start_Simulation(self, GUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py {} {}".format(GUI, self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists('fitness{}.txt'.format(self.myID)):
            time.sleep(0.01)
        with open('fitness{}.txt'.format(self.myID), 'r') as f:
            result = f.readline()
            result = float(result)
        self.fitness = result
        #print("\n\nFitness of ID: {}, = {}".format(self.myID, self.fitness))
        os.system("del fitness{}.txt".format(self.myID))

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        # pyrosim.Send_Cube(name="T", pos=[x-2, y-2, z], size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[length, width, height])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        sensors = [1, 2, 3]
        motors = [3, 4]
        for currentRow in range(len(sensors)):
            for currentColumn in range(len(motors)):
                pyrosim.Send_Synapse(sourceNeuronName=sensors[currentRow],
                                     targetNeuronName=motors[currentColumn], weight=self.weights[currentRow][currentColumn])

        pyrosim.End()


    def Mutate(self):

        randRow = random.randint(0, 2)

        randColumn = random.randint(0, 1)


        self.weights[randRow][randColumn] = random.random() * 2 - 1


    def Set_ID(self, ID):
        self.myID = ID


