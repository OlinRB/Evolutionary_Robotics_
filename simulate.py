import time
import pybullet_data
import pybullet as p

run = True

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeID = p.loadURDF("plane.urdf")
p.loadSDF("boxs.sdf")
i = 0
while run:
    time.sleep(1/60)
    p.stepSimulation()
p.disconnect()

