import numpy as np
LOOP_LEN = 3000

RUN_RANGE = 1

motor_val = 200
badResult = 0
# Population
numberOfGenerations = 10
populationSize = 10

# Num Neurons
numSensorNeurons = 6
numMotorNeurons = 6

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