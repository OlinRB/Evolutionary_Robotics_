import pyrosim.pyrosim as pyrosim
import random

x = .5
y = .5
z = .5

# x = 0
# y = 0
# z = 0

length = 1
width = 1
height = 1

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    #pyrosim.Send_Cube(name="T", pos=[x-2, y-2, z], size=[length, width, height])
    pyrosim.End()

def Create_Robot():
    pass
    # pyrosim.Start_URDF("body.urdf")
    # pyrosim.Send_Cube(name="BackLeg", pos=[x, y, z], size=[length, width, height])
    # pyrosim.Send_Joint(name="BackLeg_Torso", parent="BackLeg", child="Torso",
    #                    type="revolute", position=[1, 0, 1])
    # pyrosim.Send_Cube(name="Torso", pos=[.5, .5, .5], size=[length, width, height])
    # pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
    #                    type="revolute", position=[1,.5,0])
    # pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[length, width, height])
    #
    # pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[length, width, height])


    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    sensors = [1,2,3]
    motors = [3,4]
    for sensor in sensors:
        for motor in motors:
            pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=motor, weight=random.uniform(-1,1))




    pyrosim.End()


Create_World()
Generate_Brain()
Generate_Body()