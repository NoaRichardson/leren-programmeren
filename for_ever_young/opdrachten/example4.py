from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:
for x in range(5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

for x in range(5):
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()