import numpy as np
LOOP_LEN = 3000

motor_val = 35
badResult = 0
# Population
numberOfGenerations = 3
populationSize = 3

# Num Neurons
numSensorNeurons = 10
numMotorNeurons = 12

xMultiplier = 5
zMultiplier = 2

building = False

# Multipliers
amplitude_BackLeg = np.pi/4
frequency_BackLeg = 8
phaseOffset_BackLeg = 5
amplitude_FrontLeg = np.pi/4
frequency_FrontLeg = 125
phaseOffset_FrontLeg = 1 * (np.pi/4)
motorJointRange = 0.4
gravityAddition = 0

sensorValues = "data\\sensor_values.npy"
motorValues = "data\\motor_values.npy"