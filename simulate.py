import time

import numpy
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

#Sensors
run = True
LOOP_LEN = 1000

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")
i = 0
pi = 3.1415926536
motor_val = 25
amplitude = np.pi/4
frequency = 1
phaseOffset = 0

file1 = "data\\sensor_values.npy"
file2 = "data\\frontLegSensorValues.npy"
file3 = "data\\targetValues.npy"
pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = numpy.zeros(LOOP_LEN)
frontLegSensorValues = numpy.zeros(LOOP_LEN)
targetAngles = np.linspace(0, 2*np.pi, LOOP_LEN)
for i in range(LOOP_LEN):
    # targetAngles[i] = targetAngles[i] * (pi / 4)
    targetAngles[i] = amplitude * np.sin(frequency * targetAngles[i] + phaseOffset)
np.save(file3, targetAngles)
exit()
for i in range(LOOP_LEN):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName="BackLeg_Torso",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles[i],
        maxForce=motor_val)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=-targetAngles[i],
        maxForce=motor_val)
    time.sleep(1 / 60)
p.disconnect()
np.save(file1, backLegSensorValues)
np.save(file2, frontLegSensorValues)

