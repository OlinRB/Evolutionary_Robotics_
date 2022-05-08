from search import Run_PHC
import constants as c

# Create 2d array to store vals
all_fitness = []

for i in range(5):
    run = Run_PHC()
    all_fitness.append(run.fitness_curve)

for run in all_fitness:
    print(run)

if c.NO_ARMS:
    with open("no_arms_phc_fitness.csv", "a+") as file:
        for i in range(c.RUN_RANGE):
            for run in all_fitness:
                file.write(str(run[i]) + ",")
            file.write("\n")
else:
    with open("with_arms_phc_fitness.csv", "a+") as file:
        for i in range(c.RUN_RANGE):
            for run in all_fitness:
                file.write(str(run[i]) + ",")
            file.write("\n")
