
from simulation import SIMULATION
import os
import sys

directOrGUI = sys.argv[1]

simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()
