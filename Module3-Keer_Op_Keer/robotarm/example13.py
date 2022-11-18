from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
y = 9
# Jouw python instructies zet je vanaf hier:
for x in range(7):
    robotArm.grab()
    i = robotArm.scan()
    if i == "":
        robotArm.wait()
    else:
        for x in range(y):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(y):
            robotArm.moveLeft()
        y = y - 1
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
