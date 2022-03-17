import numpy as np
LOOP_LEN = 1500
motor_val = 30
numberOfGenerations = 10
amplitude_BackLeg = np.pi/4
frequency_BackLeg = 8
phaseOffset_BackLeg = 5
amplitude_FrontLeg = np.pi/4
frequency_FrontLeg = 125
phaseOffset_FrontLeg = 1* (np.pi/4)

sensorValues = "data\\sensor_values.npy"
motorValues = "data\\motor_values.npy"