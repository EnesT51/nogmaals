from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
for i in range(7):
    for i in range(9):
        robotArm.moveRight()
        robotArm.grab()
    for i in range(9):
        robotArm.drop()
        robotArm.moveLeft()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
