# -*- coding: utf-8 -*-
"""Genetic Algo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IJNGo0420079Iy3Sh6FzD8womFHtIx19
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
import random

def fun(x, y):
    return 25 * (1 + x)**2 + (y + x**2)**2

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

x = y = np.arange(-100, 100, 0.1)
X, Y = np.meshgrid(x, y)
zs = np.array(fun(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)


ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

ax.view_init(30, 270)
plt.show()
for angle in range(0, 360):
    
    plt.draw()

import random

def expression(x,y):
  op1 = (y + x**2)
  op2 = (1 + x)
  exp = 25 * op1**2 + op2**2  #The expression of the fitness function
  return exp

def fitness(x,y):
  value = expression(x,y)   #Fitness function

  if value ==0:
    return 999999999  #checking the parameters against the fitness function. if it zero then we have a solution
  else:
    return abs(1/value) #a way to rank the parameter. the smaller the value the higher the ranked result for the said parameter

def mutation(genes):
  children = []

  for j in range(1000):
    mutate = random.uniform(0.1,0.1)
    x = round(random.choice(genes) * mutate , 5) #mutating the genes of previous generation
    y = round(random.choice(genes) * mutate, 5)
    children.append((round(x,5),round(y,5)))

  return children


def best_genes(best_children): #for extracting the parameters of the best children  
  genes = []

  for i in best_children:
    genes.append(i[1][0])
    genes.append(i[1][1])
  
  return genes

def genetic_algo(generations):
  datapoints = []
  prev_gen = 0
  for s in range(100000): #setting parameters. This is a set of datapoint parameters from range -100 to 100
    x = random.uniform(-100,100) 
    y = random.uniform(-100,100)
    datapoints.append((x, y))  
  

  for i in range(generations):
    solutions = []
    for s in datapoints:
      x = s[0]
      y = s[1]
      #print(x,y)
      solutions.append( (fitness(x,y),s) ) #Feeding to fitness functions

    solutions.sort(reverse = True) #sorting the highest scores for parameters

    if prev_gen == solutions[0][0]:   #Stopped when results do not change anymore
      print("Best result reached: ", solutions[0][0])
      x,y = solutions[0][1]
      print(f'{x:.20f}', f'{y:.20f}')
      print("Generation required: ", i)
      break

    print("best solutions for Generaion: ", i)
    print(solutions[0])
    prev_gen = solutions[0][0]
    
    genes = best_genes(solutions[:10])
    

    datapoints = mutation(genes)

generations = 500
genetic_algo(generations)

