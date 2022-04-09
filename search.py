import os

from parallelHillClimber import PARELLEL_HILL_CLIMBER


phc = PARELLEL_HILL_CLIMBER()
phc.Evolve()
# Wait for keyboard input before showing final sim
input("Press any key to continue... ")
phc.Show_Best()




# for i in range(1):
#     os.system("python generate.py")
#     os.system("python simulate.py")