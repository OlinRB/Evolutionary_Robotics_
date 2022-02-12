import matplotlib.pyplot as plot
import numpy as np

with open("data\\sensor_values.npy", "rb") as file:
    back_values = np.load(file)

with open("data\\frontLegSensorValues.npy", "rb") as file:
    front_values = np.load(file)

with open("data\\targetValues.npy", "rb") as file:
    target_values = np.load(file)

print(target_values)
plot.plot(target_values, label="Target Values")
# plot.plot(back_values, label="Back Leg Sensor Values", linewidth=5)
# plot.plot(front_values, label="Front Leg Sensor Values")
plot.legend()
plot.show()