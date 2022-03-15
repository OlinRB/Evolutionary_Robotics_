import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        self.robotID = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")


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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                MOTOR.Set_Value(self.motors[jointName], desiredAngle, self.robotID)
                #print("NN name: {}, Joint Name: {}, Value: {}".format(neuronName, jointName, desiredAngle))


    def Get_Fitness(self):
        self.stateOfLinkZero = p.getLinkState(self.robotID,0)
        positionOfLinkZero = self.stateOfLinkZero[0]

        xCoordinateOfLinkZero = positionOfLinkZero[0]

        with open('fitness.txt', 'w') as f:
            f.write(str(xCoordinateOfLinkZero))
        exit()


