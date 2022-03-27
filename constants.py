import numpy as np
LOOP_LEN = 500
motor_val = 40
badResult = 0
numberOfGenerations = 5
numSensorNeurons = 3
numMotorNeurons = 2
populationSize = 5
amplitude_BackLeg = np.pi/4
frequency_BackLeg = 8
phaseOffset_BackLeg = 5
amplitude_FrontLeg = np.pi/4
frequency_FrontLeg = 125
phaseOffset_FrontLeg = 1* (np.pi/4)

sensorValues = "data\\sensor_values.npy"
motorValues = "data\\motor_values.npy"