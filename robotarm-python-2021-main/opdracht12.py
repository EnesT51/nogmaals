from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for e in range(9-i):
            robotArm.moveRight()
        robotArm.drop()
        for f in range(9-i):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
        



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
