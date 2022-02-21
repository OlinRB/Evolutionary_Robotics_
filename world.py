import pybullet as p
import pyrosim.pyrosim as pyrosim


class WORLD:
    def __init__(self):
        pass
        self.planeID = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")