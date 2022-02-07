import time

import numpy
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np

#Sensors
run = True
LOOP_LEN = 100

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")
i = 0

file = "data\\sensor_values.npy"

pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = numpy.zeros(LOOP_LEN)
for i in range(LOOP_LEN):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    backLegSensorValues[i] = backLegTouch
    time.sleep(1 / 60)
p.disconnect()
np.save(file, backLegSensorValues)

