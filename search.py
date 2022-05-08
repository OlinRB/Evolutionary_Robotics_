import os
import constants as c


from parallelHillClimber import PARELLEL_HILL_CLIMBER
import constants as c
import numpy as np

# Write best fitness to 0
class Run_PHC:
    def __init__(self):
        with open("best_fitness.txt", "w") as fitness_file:
            fitness_file.writelines("0")

        # Delete files from previous runs
        os.system("del best_weights")

        self.fitness_curve = []

        for i in range(c.RUN_RANGE):
            self.return_fitness = None
            phc = PARELLEL_HILL_CLIMBER()
            phc.Evolve()
            phc.Check_Best()
            phc.Show_Best(False)
            self.fitness_curve.append(phc.return_fitness)


        # Wait for keyboard input before showing final sim
        if not c.building:
            pass
            #input("Press any key to continue... ")
        #phc.Show_Best(True)

        print("Fitness curve:\n--------------------------------")
        for fitness in self.fitness_curve:
            print(fitness)

