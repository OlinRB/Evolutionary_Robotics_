import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, desiredAngle, robotID):
        # if self.jointName == "Torso_BackLeg":
        #     direction = 1
        #     frequency = self.frequency
        # else:
        #     direction = 1
        #     frequency = self.frequency/2
        # desiredAngle = self.amplitude * \
        #                           np.sin(frequency * desiredAngle
        #                                  + self.offset)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotID,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.motor_val)

        # if index == c.LOOP_LEN-1:
        #     print(self.motorValues)

