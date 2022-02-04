import time
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim

#Sensors
run = True

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
i = 0

pyrosim.Prepare_To_Simulate(robotID)
while run:

    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(backLegTouch)
    time.sleep(1 / 60)
p.disconnect()

