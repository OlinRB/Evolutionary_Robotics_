import time

import numpy

import pyrosim.pyrosim as pyrosim
import constants as c
from constants import *
import random
import os

length = 1
width = 1
height = 1


class SOLUTION:

    def __init__(self, myID):
        self.myID = myID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1


    def Start_Simulation(self, GUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py {} {}".format(GUI, self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists('fitness{}.txt'.format(self.myID)):
            time.sleep(0.01)
        # while not os.access('fitness{}.txt'.format(self.myID), os.R_OK):
        #     time.sleep(0.01)
        try:
            with open('fitness{}.txt'.format(self.myID), 'r') as f:
                result = f.readline()
                result = float(result)
        except PermissionError:
            result = c.badResult
        self.fitness = result
        # print("\n\nFitness of ID: {}, = {}".format(self.myID, self.fitness))
        os.system("del fitness{}.txt".format(self.myID))

    def Open_World(self):
        try:
            pyrosim.Start_SDF("world.sdf")
            return True

        except:
            return False

    def Create_World(self):
        world = self.Open_World()

        while not world:
            world = self.Open_World()

        pyrosim.End()

    def Open_Body(self):
        try:
            pyrosim.Start_URDF("body.urdf")
            return True

        except:
            return False

    def Create_Body(self):
        body = self.Open_Body()

        while not body:
            body = self.Open_Body()

        pyrosim.Send_Cube(name="Head", pos=[0, 0, 3.5], size=[.5, .5, .5])
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0], size=[.75, 1, 1.5])
        pyrosim.Send_Joint(name="Head_Torso", parent="Head", child="Torso", type="revolute",
                           position=[0, 0, 2.5], jointAxis="1 0 0")

        """  LOWER BODY   """

        # Left Leg

        pyrosim.Send_Joint(name="Torso_Upper_Lleg", parent="Torso", child="Upper_Lleg", type="revolute",
                           position=[0,.4,-1.1], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="Upper_Lleg", pos=[0, 0, 0], size=[.2, .3, .8])

        pyrosim.Send_Joint(name="Upper_Lleg_Lower_Lleg", parent="Upper_Lleg", child="Lower_Lleg", type="revolute",
                           position=[0,0,-.8], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="Lower_Lleg", pos=[0, 0, 0], size=[.2, .2, .8])

        # Right Leg

        pyrosim.Send_Joint(name="Torso_Upper_Rleg", parent="Torso", child="Upper_Rleg", type="revolute",
                           position=[0,-.4,-1.1], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="Upper_Rleg", pos=[0, 0, 0], size=[.2, .3, .8])

        pyrosim.Send_Joint(name="Upper_Rleg_Lower_Rleg", parent="Upper_Rleg", child="Lower_Rleg", type="revolute",
                           position=[0,0,-.8], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="Lower_Rleg", pos=[0, 0, 0], size=[.2, .2, .8])


        # Feet

        pyrosim.Send_Joint(name="Lower_Lleg_L_Foot", parent="Lower_Lleg", child="L_Foot", type="revolute",
                           position=[.15, 0, -.5], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="L_Foot", pos=[0,0,0], size=[.5,.2,.2])

        pyrosim.Send_Joint(name="Lower_Rleg_L_Foot", parent="Lower_Rleg", child="R_Foot", type="revolute",
                           position=[.15, 0, -.5], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="R_Foot", pos=[0, 0, 0], size=[.5, .2, .2])

        #
        # # Shoulders and arms
        #
        # pyrosim.Send_Joint(name="Torso_Lshoulder", parent="Torso", child="Lshoulder", type="revolute",
        #                    position=[0,.5,1], jointAxis="1 0 0")
        #
        # pyrosim.Send_Cube(name="Lshoulder", pos=[0, 0, 1.6], size=[.3, .2, .2])
        #
        # pyrosim.Send_Joint(name="Torso_Rshoulder", parent="Torso", child="Rshoulder", type="revolute",
        #                    position=[0, -.5, 1], jointAxis="1 0 0")
        #
        # pyrosim.Send_Cube(name="Rshoulder", pos=[0, 0, 1.6], size=[.3, .2, .2])
        #
        #
        # # Legs
        #



        # pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
        #                    position=[0, .5, 1], jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="FrontLeg", pos=[0, .5, 0], size=[0.2, 1, 0.2])
        # pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -.5, 1],
        #                    jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="BackLeg", pos=[0, -.5, -0], size=[0.2, 1, 0.2])
        # pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
        #                    position=[-.5, 0, 1], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-.5, 0, 0], size=[1, 0.2, 0.2])
        # pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
        #                    position=[.5, 0, 1], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="RightLeg", pos=[.5, 0, 0], size=[1, 0.2, 0.2])
        #
        # pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
        #                    position=[0, 1, 0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])
        #
        # pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
        #                    position=[0, -1, 0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])
        #
        # pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
        #                    position=[1, 0, 0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])
        #
        # pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
        #                    position=[-1, 0, 0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        # #pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        # pyrosim.Send_Sensor_Neuron(name=0, linkName="BackLeg")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLeg")
        # pyrosim.Send_Sensor_Neuron(name=4, linkName="FrontLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=5, linkName="BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=6, linkName="LeftLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=7, linkName="RightLowerLeg")
        #
        # pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron(name=12, jointName="FrontLeg_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=13, jointName="BackLeg_BackLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=14, jointName="LeftLeg_LeftLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=15, jointName="RightLeg_RightLowerLeg")
        #
        # sensors = [1, 2, 3]
        # motors = [3, 4]
        # for currentRow in range(c.numSensorNeurons):
        #     for currentColumn in range(c.numMotorNeurons):
        #         pyrosim.Send_Synapse(sourceNeuronName=currentRow,
        #                              targetNeuronName=currentColumn + c.numSensorNeurons,
        #                              weight=self.weights[currentRow][currentColumn])
        #                              #weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):

        randRow = random.randint(0, c.numSensorNeurons - 1)

        randColumn = random.randint(0, c.numMotorNeurons - 1)

        self.weights[randRow][randColumn] = random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID
