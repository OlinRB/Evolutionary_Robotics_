from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import constants as c
import time
import pyrosim.pyrosim as pyrosim


class SIMULATION:

    def __init__(self, GUI, solutionID):
        self.mode = GUI
        self.solutionID = solutionID
        if GUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8 + c.gravityAddition)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):

        for i in range(c.LOOP_LEN):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.mode == "GUI":
                time.sleep(1 / 60)

    def Get_Fitness(self):
        self.robot.Get_Fitness(self.solutionID)

    def __del__(self):
        p.disconnect()
