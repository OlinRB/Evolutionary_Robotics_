import pybullet as p


p.connect(p.DIRECT)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
#         p.setGravity(0, 0, -9.8 + c.gravityAddition)
p.stepSimulation()