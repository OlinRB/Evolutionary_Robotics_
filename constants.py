import numpy as np
LOOP_LEN = 100
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