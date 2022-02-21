import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        pass
        self.motorValues = np.linspace(0, 2*np.pi, c.LOOP_LEN)
        self.amplitude = c.amplitude_BackLeg
        self.frequency = c.frequency_BackLeg
        self.offset = c.phaseOffset_BackLeg

    def Set_Value(self, index, robotID):
        if self.jointName == "BackLeg_Torso":
            direction = -1
            frequency = self.frequency
        else:
            direction = 1
            frequency = self.frequency/2
            print(self.motorValues[index-1])
        self.motorValues[index] = self.amplitude * \
                                  np.sin(frequency * self.motorValues[index]
                                         + self.offset)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotID,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=(direction)*self.motorValues[index],
            maxForce=c.motor_val)

        # if index == c.LOOP_LEN-1:
        #     print(self.motorValues)


    def Save_Values(self):
        np.save(c.motorValues, self.motorValues)
