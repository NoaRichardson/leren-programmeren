from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:2 5
for x in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()