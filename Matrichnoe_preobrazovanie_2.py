# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:01:00 2021

@author: Vilams
"""
import math

import numpy as np
import random 
import matplotlib.pyplot as plt
print('операции')

T=1
main=0
choice=[1,-1]
while True:
    
    operation=int(input('заполение матрицы №1\nшахматная матрицы №2: '))
    if operation==1 or operation==2 :
        break
    else: 
        print('вводите только 1 или 2')
        print ('')
n=int(input('Матрица какого порядка: '))
repeat=int(input('количество повторов: '))
choice_namber=range(n) #список для координат случайонго выбора матрицы e
E=np.zeros((n,n))   #Заполнение матрицы числами -1,1 
for i in range(n):
    for j in range(n):
        E[i][j]=random.choice(choice)      
main=E.copy()

plt.ion()
for m in range(repeat): 
    print('текущая итерация' ,m, end='\r')
    sum_1=0
    sum_2=0
    number_1=random.choice(choice_namber) #выбор координаты х для замены в матрицы е 
    number_2=random.choice(choice_namber) #выбор координаты у для замены в матрицы е
    e=E.copy() #сопия матрицы е 
    e[number_1][number_2]*=-1 #случайная замена 
    for i in range(n):        #сумма элементов матриц
        for j in range(n):
            sum_1+=E[i][j]*E[i][j-1]+E[i-1][j]*E[i][j] 
            sum_2+=e[i][j]*e[i][j-1]+e[i-1][j]*e[i][j] 
    if operation==1:
        delta=-1*(sum_2-sum_1) #рвзность суии матриц * -1
    else:
        delta=(sum_2-sum_1) #рвзность суии матриц
        
    if (delta<=0):    #заменяет Е старую на е новую 
        E=e.copy()
    elif (delta>0): # мат. дейсвия 
        W=math.exp(-delta/T)
        P=random.random() 
        if W>=P:    # Е остаеться без изменения, main сохраняет значение E
            main=E.copy()
        elif W<0:   # Е принимает значеине самой первой матрицы 
            E=main.copy()
    plt.clf()  #Граффическое отображение
    plt.imshow(E)
    plt.draw()
    plt.show()
    plt.gcf().canvas.flush_events()
plt.ioff() 
#spplt.show()
gfgf=input()  
    