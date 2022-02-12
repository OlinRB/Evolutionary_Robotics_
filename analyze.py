import matplotlib.pyplot as plot
import numpy as np

with open("data\\sensor_values.npy", "rb") as file:
    back_values = np.load(file)

with open("data\\frontLegSensorValues.npy", "rb") as file:
    front_values = np.load(file)

with open("data\\targetValues_BackLeg.npy", "rb") as file:
    target_values_BackLeg = np.load(file)

with open("data\\targetValues_FrontLeg.npy", "rb") as file:
    target_values_FrontLeg = np.load(file)

plot.plot(target_values_BackLeg, label="Back Leg Angles", linewidth=3)
plot.plot(target_values_FrontLeg, label="Front Leg Angles")
# plot.plot(back_values, label="Back Leg Sensor Values", linewidth=5)
# plot.plot(front_values, label="Front Leg Sensor Values")
plot.legend()
plot.show()