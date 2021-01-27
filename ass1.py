# ass1.py
# AUCSC460
# Adam Sun  
# 1497030  
# Feb 26, 2020
from heapq import heappush, heappop
import numpy as np
from random import random,choice
import math
def main():
    initial_state = inputL()
    AstarA(initial_state)
def AstarA(initial_state):
    
    print("Output:")
    fixstate = replaceZero(initial_state)
    printM(np.array(initial_state).reshape(3,3))
    
    print("(f =",man(np.array(initial_state).reshape(3,3)),")")
    astarQueue = []
    current = initial_state.copy()
    current_fvalue = 0
    step = 0
    pastlist = []          
    for j in range(100):
        step = step + 1
        child = putAllchild(current.copy())
        
        for i in range(len(child)):
            if child[i] != None and child[i] not in pastlist:
                astarQueue.append([child[i],step] )  
                pastlist.append(child[i])
                
        result = searchMin(astarQueue.copy())
        indexChoose = choice(result[1])
        current = astarQueue[indexChoose][0]
        step = astarQueue[indexChoose][1]
        current_fvalue = man((np.array(current).reshape(3,3)))
        
        print("next state:")
        print("(f value =",man(np.array(current).reshape(3,3)) + step,")")
        fixstate = replaceZero(current)
        printM(np.array(fixstate).reshape(3,3))
        
        astarQueue.pop(indexChoose)
        pastlist.remove(pastlist[0])
        if checkGoal(current) == True:
            print("find solution when t is ", j+1)
            break          
# this method is to search min value among queue
def searchMin(lista):
    min = 1000
    index = []
    for i in range(len(lista)):
        if min > lista[i][1] + man(np.array(lista[i][0]).reshape(3,3)):
            min = lista[i][1] + man(np.array(lista[i][0]).reshape(3,3))
            index = []
            index.append(i)
        elif min == lista[i][1]+ man(np.array(lista[i][0]).reshape(3,3)):
            index.append(i)
    return [min, index]
        
# this method is to return manhattan distance 
def man(state):
    current = state
    goal_position = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),0:(2,2)}
    sum_m = 0
    for i in range(3):
        for j in range(3):
            if current[i,j] != 0:
                sum_m += sum(abs(a-b) for a,b in zip((i,j),goal_position[current[i,j]]))
    return sum_m
# this method is to return the list after move top
def TopMove(state):
    currentstate = state.copy()
    ZeroPosition = checkZero(currentstate)
    if ZeroPosition != 0 and ZeroPosition != 1 and ZeroPosition != 2:
        temp = currentstate[ZeroPosition-3]
        currentstate[ZeroPosition-3] = 0
        currentstate[ZeroPosition] = temp
        return currentstate
    else:
        return None
# this method is to return the list after move down
def DownMove(state):
    currentstate = state.copy()
    ZeroPosition = checkZero(currentstate)
    if ZeroPosition != 6 and ZeroPosition != 7 and ZeroPosition != 8:
        temp = currentstate[ZeroPosition+3]
        currentstate[ZeroPosition+3] = 0
        currentstate[ZeroPosition] = temp
        return currentstate
    else:
        return None   
# this method is to return the list after move left
def LeftMove(state):
    currentstate = state.copy()
    ZeroPosition = checkZero(currentstate)
    if ZeroPosition != 0 and ZeroPosition != 3 and ZeroPosition != 6:
        temp = currentstate[ZeroPosition-1]
        currentstate[ZeroPosition-1] = 0
        currentstate[ZeroPosition] = temp
        return currentstate
    else:
        return None    
# this method is to return the list after move right
def RightMove(state):
    currentstate = state.copy()
    ZeroPosition = checkZero(currentstate)
    if ZeroPosition != 2 and ZeroPosition != 5 and ZeroPosition != 8:
        temp = currentstate[ZeroPosition+1]
        currentstate[ZeroPosition+1] = 0
        currentstate[ZeroPosition] = temp
        return currentstate
    else:
        return None    
# this method is to gather all possbile moves into child list
def putAllchild(state):
    currentstate = state.copy()
    lista = []
    if TopMove(currentstate.copy()) != None:
        lista.append(TopMove(currentstate.copy()))
    if DownMove(currentstate.copy()) != None:
        lista.append(DownMove(currentstate.copy()))
    if LeftMove(currentstate.copy()) != None:
        lista.append(LeftMove(currentstate.copy()))
    if RightMove(currentstate.copy()) != None:
        lista.append(RightMove(currentstate.copy()))
    return lista
#this method is to check the postition of 0  
def checkZero(alist):
    zero = alist.index(0)
    return zero
#print the list as 8-puzzle
def printM(list):
    aa = list.copy()
    print(aa,'\n')
    
#return true if current node is goal    
def replaceZero(lista):
    state = lista.copy()
    zeroid = checkZero(state)
    state[zeroid] = ' '
    return state

def checkGoal(checklist):
    if checklist == [1,2,3,4,5,6,7,8,0]:
        return True
    else:
        return False
#return true if next node is bad move 

def checkBadmove(old,new):
    oldL = man(np.array(old.copy()).reshape(3,3))
    newL = man(np.array(new.copy()).reshape(3,3))
    if newL < oldL:
        return True
    else:
        return False
def inputL():
    numList = list(int(num) for num in input("Enter 9 numbers (including 0): ").strip().split())[:9]
    return numList
main()