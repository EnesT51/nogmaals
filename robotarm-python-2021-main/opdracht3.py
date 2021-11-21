from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
# robotArm.grab()
# for i in range(1):
#     robotArm.moveRight()
# robotArm.drop()
# for i in range(1):
#     robotArm.moveLeft()
# robotArm.grab()
# for i in range(1):
#     robotArm.moveRight()
# robotArm.drop()
# for i in range(1):
#     robotArm.moveLeft()
# robotArm.grab()
# for i in range(1):
#     robotArm.moveRight()
# robotArm.drop()
# for i in range(1):
#     robotArm.moveLeft()
# robotArm.grab()
# for i in range(1):
#     robotArm.moveRight()
# robotArm.drop()
for i in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
