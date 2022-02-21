from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import constants as c
import time
import pyrosim.pyrosim as pyrosim


class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):

        for i in range(c.LOOP_LEN):
            #print(i)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotID,
            #     jointName="BackLeg_Torso",
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=targetAngles_BackLeg[i],
            #     maxForce=motor_val)
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotID,
            #     jointName="Torso_FrontLeg",
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=-targetAngles_FrontLeg[i],
            #     maxForce=motor_val)
            time.sleep(1 / 60)


    def __del__(self):
        p.disconnect()
