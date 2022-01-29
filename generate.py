import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxs.sdf")

x = 0
y = 0
z = .5
for k in range(5):
    for j in range(5):
        length = 1
        width = 1
        height = 1
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+k,y+j,z+i] , size=[length,width,height])
            width = width * .9
            length = length * .9
            height = height * .9


pyrosim.End()