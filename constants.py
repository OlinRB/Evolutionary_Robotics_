import numpy as np
LOOP_LEN = 1000
motor_val = 45
badResult = 0
# Population
numberOfGenerations = 20
populationSize = 10

# Num Neurons
numSensorNeurons = 9
numMotorNeurons = 8

# Multipliers
amplitude_BackLeg = np.pi/4
frequency_BackLeg = 8
phaseOffset_BackLeg = 5
amplitude_FrontLeg = np.pi/4
frequency_FrontLeg = 125
phaseOffset_FrontLeg = 1 * (np.pi/4)

sensorValues = "data\\sensor_values.npy"
motorValues = "data\\motor_values.npy"