import pyrosim.pyrosim as pyrosim


x = .5
y = .5
z = .5

length = 1
width = 1
height = 1

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    #pyrosim.Send_Cube(name="T", pos=[x-2, y-2, z], size=[length, width, height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="BackLeg", pos=[x, y, z], size=[length, width, height])
    pyrosim.Send_Joint(name="BackLeg_Torso", parent="BackLeg", child="Torso",
                       type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="Torso", pos=[.5, .5, .5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                       type="revolute", position=[1,.5,0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[length, width, height])

    pyrosim.End()


Create_World()
Create_Robot()