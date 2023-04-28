import random
import numpy as np
import matplotlib.pyplot as plt
PointsC = 0
PointsP = 0
length = 1000


for i in range(length):
    #Player = int(input())
    player = random.randint(1,3)
    Computer = random.randint(1,3)
    print(Computer)
    if Player == 1:
        if Computer == 1:
            print("draw")
        elif Computer == 2:
            print("You lost")
            PointsC += 1
            print("Computer points" + " " + str(PointsC))
        else:
            print("You won")
            PointsP += 1
            print("PLayer points" + " " + str(PointsP))
            
    if Player == 2:
        if Computer == 1:
            print("You won")
            PointsP += 1
            print("PLayer points" + " " + str(PointsP))
        elif Computer == 2:
            print("Draw")
        else:
            print("You lost")
            PointsC += 1
            print("Computer points" + " " + str(PointsC))
            
            
       
    if Player == 3:
        if Computer == 1:
            print("You lost")
            PointsC += 1
            print("Computer points" + " " + str(PointsC))
        elif Computer == 2:
            print("You won")
            PointsP += 1
            print("Player points" + " " + str(PointsP))
        else:
            print("Draw")
            
plt.plot(range(len(ylist)), ylist, '.', markersize = 1, label = "How many times player wins")
   


    
