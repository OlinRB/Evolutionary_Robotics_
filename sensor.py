import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.values = np.zeros(c.LOOP_LEN)

    def Get_Value(self, index):
        self.values[index] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # if index == c.LOOP_LEN-1:
        #     print(self.values)

    def Save_Values(self):
        np.save(c.sensorValues, self.values)
