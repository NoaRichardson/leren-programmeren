from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
y = 10
# Jouw python instructies zet je vanaf hier:
for x in range(7):
    y = y - 1
    robotArm.grab()
    for x in range(y):
        robotArm.moveRight()
    for x in range(y):
        robotArm.moveLeft
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
robotArm.speed = 3