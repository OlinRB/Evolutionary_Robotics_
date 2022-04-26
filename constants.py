import numpy as np
LOOP_LEN = 3000

RUN_RANGE = 1

motor_val = 200
badResult = 0
# Population
populationSize = 1
numberOfGenerations = 1

NO_ARMS = True

# Num Neurons
if NO_ARMS:
    numSensorNeurons = 6
    numMotorNeurons = 6

else:
    numSensorNeurons = 10
    numMotorNeurons = 12

xMultiplier = 2
zMultiplier = 3

building = False

# Multipliers
amplitude_BackLeg = np.pi/4
frequency_BackLeg = 8
phaseOffset_BackLeg = 5
amplitude_FrontLeg = np.pi/4
frequency_FrontLeg = 125
phaseOffset_FrontLeg = 1 * (np.pi/4)
motorJointRange = -0.5
gravityAddition = 0

sensorValues = "data\\sensor_values.npy"
motorValues = "data\\motor_values.npy"