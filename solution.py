import time

import numpy as np

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
        probability = random.randint(1,3)
        if probability != 1:
            file = open("best_weights", "rb")
            self.weights = np.load(file)
            file.close()
        else:
            self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
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

        pyrosim.Send_Joint(name="Torso_UpperLleg", parent="Torso", child="UpperLleg", type="revolute",
                           position=[0,.3,-1.1], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="UpperLleg", pos=[0, 0, 0], size=[.4, .4, .8])

        pyrosim.Send_Joint(name="UpperLleg_LowerLleg", parent="UpperLleg", child="LowerLleg", type="revolute",
                           position=[0,0,-.8], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="LowerLleg", pos=[0, 0, 0], size=[.3, .4, .8])

        # Right Leg

        pyrosim.Send_Joint(name="Torso_UpperRleg", parent="Torso", child="UpperRleg", type="revolute",
                           position=[0,-.3,-1.1], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="UpperRleg", pos=[0, 0, 0], size=[.4, .4, .8])

        pyrosim.Send_Joint(name="UpperRleg_LowerRleg", parent="UpperRleg", child="LowerRleg", type="revolute",
                           position=[0,0,-.8], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="LowerRleg", pos=[0, 0, 0], size=[.3, .4, .8])


        # Feet

        pyrosim.Send_Joint(name="LowerLleg_LFoot", parent="LowerLleg", child="LFoot", type="revolute",
                           position=[.1, 0, -.5], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="LFoot", pos=[0,0,0], size=[.7,.3,.2])

        pyrosim.Send_Joint(name="LowerRleg_RFoot", parent="LowerRleg", child="RFoot", type="revolute",
                           position=[.1, 0, -.5], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="RFoot", pos=[0, 0, 0], size=[.7, .3, .2])



        """ UPPER BODY  """

        # Shoulders and arms

        pyrosim.Send_Joint(name="Torso_Lshoulder", parent="Torso", child="Lshoulder", type="revolute",
                           position=[0,.5,.55], jointAxis="1 1 0")

        pyrosim.Send_Cube(name="Lshoulder", pos=[0, 0, 0], size=[.3, .2, .2])


        pyrosim.Send_Joint(name="Torso_Rshoulder", parent="Torso", child="Rshoulder", type="revolute",
                           position=[0, -.5, .55], jointAxis="1 1 0")

        pyrosim.Send_Cube(name="Rshoulder", pos=[0, 0, 0], size=[.3, .2, .2])


        # Arms

        pyrosim.Send_Joint(name="Lshoulder_LUpperArm", parent="Lshoulder", child="LUpperArm", type="revolute",
                           position=[0, .2, -.3], jointAxis="1 1 0")

        pyrosim.Send_Cube(name="LUpperArm", pos=[0, 0, 0], size=[.2, .2, .75])

        pyrosim.Send_Joint(name="LUpperArm_LLowerArm", parent="LUpperArm", child="LLowerArm", type="revolute",
                           position=[0, 0, -.7], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="LLowerArm", pos=[0, 0, 0], size=[.1, .2, .7])


        pyrosim.Send_Joint(name="Rshoulder_RUpperArm", parent="Rshoulder", child="RUpperArm", type="revolute",
                           position=[0, -.2, -.3], jointAxis="1 1 1")

        pyrosim.Send_Cube(name="RUpperArm", pos=[0, 0, 0], size=[.2, .2, .75])

        pyrosim.Send_Joint(name="RUpperArm_RLowerArm", parent="RUpperArm", child="RLowerArm", type="revolute",
                           position=[0, 0, -.7], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="RLowerArm", pos=[0, 0, 0], size=[.1, .2, .7])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))

        pyrosim.Send_Sensor_Neuron(name=0, linkName="LFoot")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="RFoot")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LowerLleg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LowerRleg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="UpperLleg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="UpperRleg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="LUpperArm")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="RUpperArm")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="LLowerArm")
        pyrosim.Send_Sensor_Neuron(name=9, linkName="RLowerArm")

        if not c.building:
            pyrosim.Send_Motor_Neuron(name=10, jointName="LowerLleg_LFoot")
            pyrosim.Send_Motor_Neuron(name=11, jointName="LowerRleg_RFoot")
            pyrosim.Send_Motor_Neuron(name=12, jointName="UpperLleg_LowerLleg")
            pyrosim.Send_Motor_Neuron(name=13, jointName="UpperRleg_LowerRleg")
            pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_UpperLleg")
            pyrosim.Send_Motor_Neuron(name=16, jointName="Torso_UpperRleg")

            pyrosim.Send_Motor_Neuron(name=17, jointName="Lshoulder_LUpperArm")
            pyrosim.Send_Motor_Neuron(name=18, jointName="Rshoulder_RUpperArm")
            pyrosim.Send_Motor_Neuron(name=19, jointName="LUpperArm_LLowerArm")
            pyrosim.Send_Motor_Neuron(name=20, jointName="RUpperArm_RLowerArm")
            pyrosim.Send_Motor_Neuron(name=21, jointName="Torso_Lshoulder")
            pyrosim.Send_Motor_Neuron(name=22, jointName="Torso_Rshoulder")


        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])
                                     #weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):

        randRow = random.randint(0, c.numSensorNeurons - 1)

        randColumn = random.randint(0, c.numMotorNeurons - 1)

        self.weights[randRow][randColumn] = random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID
