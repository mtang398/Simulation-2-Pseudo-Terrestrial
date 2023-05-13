import graphlib
import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt
from PIL import Image
import math

M = np.zeros((15,15))

A = np.zeros((15,15))
for episode in range(0,20):
    Action = pd.read_csv("C:/Users/mstan/project/Data/Simulation_5/VisualRange_25/Depth_1000/Episode_%d.csv" %(episode))
    AgentX = Action['Agent X'].tolist()
    AgentY = Action['Agent Y'].tolist()
    for i in range(len(AgentX)):
        A[14-AgentY[i]][AgentX[i]] += 1
plt.imsave("C:/users/mstan/project/ActionFrequency.png", A, cmap = "Reds")
im = Image.open('C:/users/mstan/project/ActionFrequency.png')
Color = list(im.getdata())
Graph = [[] for row in A]
for row in range(15):
        for col in range(15):
            Graph[row].append((0,0,0,0))
for row in range(15):
        for col in range(15):
            if A[14-row][col] != 0:
                Graph[14-row][col] = Color[(14-row)*15+col]
plt.imshow(Graph)
plt.show()