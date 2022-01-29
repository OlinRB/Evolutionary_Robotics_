import time
import pybullet_data

#test
import pybullet as p

run = True

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeID = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")
while run:
    p.stepSimulation()
p.disconnect()

