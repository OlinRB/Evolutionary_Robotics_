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
#Refactoring

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")
i = 0
pi = 3.1415926536
motor_val = 15

amplitude_BackLeg = np.pi/4
frequency_BackLeg = 8
phaseOffset_BackLeg = 5
amplitude_FrontLeg = np.pi/4
frequency_FrontLeg = 125
phaseOffset_FrontLeg = 1* (np.pi/4)

file1 = "data\\sensor_values.npy"
file2 = "data\\frontLegSensorValues.npy"
file3 = "data\\targetValues_BackLeg.npy"
file4 = "data\\targetValues_FrontLeg.npy"
pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = numpy.zeros(LOOP_LEN)
frontLegSensorValues = numpy.zeros(LOOP_LEN)
targetAngles_BackLeg = np.linspace(0, 2*np.pi, LOOP_LEN)
targetAngles_FrontLeg = np.linspace(0, 2*np.pi, LOOP_LEN)
for i in range(LOOP_LEN):
    # targetAngles[i] = targetAngles[i] * (pi / 4)
    targetAngles_BackLeg[i] = amplitude_BackLeg * np.sin(frequency_BackLeg * targetAngles_BackLeg[i] + phaseOffset_BackLeg)
    targetAngles_FrontLeg[i] = amplitude_FrontLeg * np.sin(frequency_FrontLeg * targetAngles_FrontLeg[i] + phaseOffset_FrontLeg)
# np.save(file3, targetAngles_BackLeg)
# np.save(file4, targetAngles_FrontLeg)
# exit()
for i in range(LOOP_LEN):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName="BackLeg_Torso",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_BackLeg[i],
        maxForce=motor_val)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=-targetAngles_FrontLeg[i],
        maxForce=motor_val)
    time.sleep(1 / 60)
p.disconnect()
np.save(file1, backLegSensorValues)
np.save(file2, frontLegSensorValues)

