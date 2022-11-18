from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 3
y = 10
# Jouw python instructies zet je vanaf hier:
for x in range(5):
    y = y - 1
    robotArm.grab()
    for x in range(y):
        robotArm.moveRight()
    robotArm.drop()
    y = y - 1
    for x in range(y):
        robotArm.moveLeft()


        

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()