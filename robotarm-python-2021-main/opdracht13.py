from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
# Jouw python instructies zet je vanaf hier:
robotarm = True
beweeg = 1
for robotarm in range(7):
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for r in range(beweeg):
            robotArm.moveRight()
        beweeg +=1
        robotArm.drop()
        for i in range(beweeg):
            robotArm.moveLeft()
    else:
        beweeg,robotarm = False
    
            

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
