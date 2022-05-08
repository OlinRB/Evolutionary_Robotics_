import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import os
import time


class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        body = self.Load_Body()
        while not body:
            body = self.Load_Body()
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain{}.nndf".format(self.solutionID))
        os.system("del brain{}.nndf".format(self.solutionID))

        self.start_time = time.time()
        self.end_time = None

    def Load_Body(self):
        try:
            self.robotID = p.loadURDF("body.urdf")
            return True

        except:
            return False


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, index):
        for linkName in self.sensors:
            SENSOR.Get_Value(self.sensors[linkName], index)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()


    def Act(self, index):

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                MOTOR.Set_Value(self.motors[jointName], desiredAngle, self.robotID)
                #print("NN name: {}, Joint Name: {}, Value: {}".format(neuronName, jointName, desiredAngle))
        # Record time robot was standing
        self.Check_Z_Val()

    def Check_Z_Val(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotID)
        basePosition = basePositionAndOrientation[0]
        zPosition = basePosition[2]
        if zPosition < 3:
            self.end_time = time.time()

    def Get_Fitness(self, solutionID):
        # self.stateOfLinkZero = p.getLinkState(self.robotID,0)
        # positionOfLinkZero = self.stateOfLinkZero[0]
        #
        # xCoordinateOfLinkZero = positionOfLinkZero[0]
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotID)

        basePosition = basePositionAndOrientation[0]

        xPosition = basePosition[0]
        zPosition = basePosition[2]

        # Determine time robot was upright
        if self.end_time is None:
            self.end_time = time.time()

        upright_time = self.end_time - self.start_time

        fitness = xPosition * (zPosition ** 3) * upright_time

        with open('tmp{}.txt'.format(solutionID), 'w') as f:
            f.write(str(fitness))

        os.rename("tmp"+str(solutionID)+".txt" , "fitness"+str(solutionID)+".txt")