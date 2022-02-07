import matplotlib.pyplot as plot
import numpy as np

with open("data\\sensor_values.npy", "rb") as file:
    values = np.load(file)

plot.plot(values)
plot.show()