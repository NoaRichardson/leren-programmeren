from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:
for x in range(8):
    robotArm.moveRight()
for x in range(9):
    robotArm.grab()
    i = robotArm.scan()
    if i == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()