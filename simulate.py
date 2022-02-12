import time

import numpy
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np

#Sensors
run = True
LOOP_LEN = 10000

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")
i = 0

file1 = "data\\sensor_values.npy"
file2 = "data\\frontLegSensorValues.npy"
pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = numpy.zeros(LOOP_LEN)
frontLegSensorValues = numpy.zeros(LOOP_LEN)
for i in range(LOOP_LEN):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName="BackLeg_Torso",
        controlMode=p.POSITION_CONTROL,
        targetPosition=0.0,
        maxForce=500)
    time.sleep(1 / 60)
p.disconnect()
np.save(file1, backLegSensorValues)
np.save(file2, frontLegSensorValues)

