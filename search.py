import os
import constants as c

from parallelHillClimber import PARELLEL_HILL_CLIMBER
import constants as c

for i in range(c.RUN_RANGE):
    phc = PARELLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Check_Best()
    phc.Show_Best(False)
# Wait for keyboard input before showing final sim
if not c.building:
    input("Press any key to continue... ")
phc.Show_Best(True)




# for i in range(1):
#     os.system("python generate.py")
#     os.system("python simulate.py")