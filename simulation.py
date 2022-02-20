from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        robotID = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(robotID)