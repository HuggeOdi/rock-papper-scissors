import random
import numpy as np
import matplotlib.pyplot as plt

length = 100
iterations = 5

def play(itera):
    PointsC = 0
    PointsP = 0
    ylist = [0]
    for i in range(length):
        #Player = int(input())
        Player = random.randint(1,3)
        Computer = random.randint(1,3)
        #print(Computer)



        if Player == 1:
            if Computer == 1:
                #print("draw")
                ylist.append(ylist[-1])
            elif Computer == 2:
                #print("You lost")
                PointsC += 1
                ylist.append(ylist[-1] - 1) 
                #print("Computer points" + " " + str(PointsC))
            else:
                #print("You won")
                PointsP += 1
                ylist.append(ylist[-1] + 1)
                #print("PLayer points" + " " + str(PointsP))

        if Player == 2:
            if Computer == 1:
                #print("You won")
                PointsP += 1
                ylist.append(ylist[-1] + 1)
                #print("PLayer points" + " " + str(PointsP))
            elif Computer == 2:
                #print("Draw")
                ylist.append(ylist[-1])
            else:
                #print("You lost")
                PointsC += 1
                ylist.append(ylist[-1] - 1)
                #print("Computer points" + " " + str(PointsC))

        if Player == 3:
            if Computer == 1:
                #print("You lost")
                PointsC += 1
                ylist.append(ylist[-1] - 1)
                #print("Computer points" + " " + str(PointsC))
            elif Computer == 2:
                #print("You won")
                ylist.append(ylist[-1] + 1)
                PointsP += 1
                #print("Player points" + " " + str(PointsP))
            else:
                #print("Draw")
                ylist.append(ylist[-1])
        
    plt.plot(range(len(ylist)), ylist, '-', markersize = 1, label = "How many times player wins, {}".format(itera))

for i in range(iterations):
    play(i + 1)
plt.axhline(0, 0, len(ylist), color = "red", linestyle = "dashed")
plt.legend()
plt.show()
   # plt.xlabel("X")
   # plt.ylabel("Y")
   # plt.legend()


            


    



            


    
