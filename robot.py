import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self):
        self.robotID = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()


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

    def Act(self, index):
        for jointName in pyrosim.jointNamesToIndices:
            MOTOR.Set_Value(self.motors[jointName], index, self.robotID)
