import pyrosim.pyrosim as pyrosim


x = 0
y = 0
z = .5

length = 1
width = 1
height = 1

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Torso", pos=[x-2, y-2, z], size=[length, width, height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[x, y, z], size=[length, width, height])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1",
                       type="revolute", position=[0, 1, 1])
    pyrosim.Send_Cube(name="Link1", pos=[0, 0, .5], size=[length, width, height])
    pyrosim.End()


Create_World()
Create_Robot()