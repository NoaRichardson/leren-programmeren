from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 3
y = 10
# Jouw python instructies zet je vanaf hier:
for x in range(9):
    robotArm.grab()
    y = y - 1
    i = robotArm.scan()
    if i == "red":
        for x in range(y):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(y):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()