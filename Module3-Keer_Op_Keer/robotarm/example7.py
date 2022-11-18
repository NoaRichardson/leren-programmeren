from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:
for x in range(9):
    robotArm.moveRight()
for x in range(4):
   for x in range(6):
      robotArm.grab()
      robotArm.moveLeft()
      robotArm.drop()
      robotArm.moveRight()
   for x in range(2):
      robotArm.moveLeft()
for x in range(6):
      robotArm.grab()
      robotArm.moveLeft()
      robotArm.drop()
      robotArm.moveRight()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()