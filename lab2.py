# lab2.py
# AUCSC460
# Adam Sun  
# 1497030  
# Feb 10, 2020
tup1 = (3,3,1,0,0,0)
list = []
def main(): 
    dls(15)
    
    
def checkGoal(tup):
        #If (0,0,0,3,3,1)
        if  tup[0]== 0 and tup[1] == 0 and tup[2] == 0 and tup[3] == 3 and tup[4] == 3 and tup[5] == 1:
            return True
        else:
            return False
    
def validState(tup):
    if tup in list: #check if it is cycle
        return False
    if  tup[0] >= 0 and tup[1] >= 0 and tup[3] >= 0 and tup[4] >= 0:
        if tup[0] == 0 or tup[0] >= tup[1]:
            if tup[3] == 0 or tup[3]>=tup[4]:
                list.append(tup)
                return True
            elif tup == (3,3,1,0,0,0):
                return False            
            else:
                return False
    else:
        return False

def dls(limit): 
    return Recursive_dls(tup1,limit)

def Recursive_dls(tup,limit):
    if checkGoal(tup) == True:
        print("<Goal>",tup)
    elif limit <= 0:
        pass
    else:
        if tup[2] == 1 and tup[5] == 0:#boat in side A
            if validState((tup[0],tup[1]-2,0,tup[3],tup[4]+2,1)) == True:
                Recursive_dls((tup[0],tup[1]-2,0,tup[3],tup[4]+2,1),limit-1)   
                print("At the current"+str(tup)+"you will take the action,<move 2 cannibal from side A to side B>,and then, your new state is ,"
                      +str((tup[0],tup[1]-2,0,tup[3],tup[4]+2,1))) 
            if validState((tup[0],tup[1]-1,0,tup[3],tup[4]+1,1)) == True:
                Recursive_dls((tup[0],tup[1]-1,0,tup[3],tup[4]+1,1),limit-1)   
                print("At the current"+str(tup)+"you will take the action,<move 1 cannibal from side A to side B>,and then, your new state is ,"
                      +str((tup[0],tup[1]-1,0,tup[3],tup[4]+1,1)))              
            if validState((tup[0]-2,tup[1],0,tup[3]+2,tup[4],1)) == True:
                Recursive_dls((tup[0]-2,tup[1],0,tup[3]+2,tup[4],1),limit-1)
                print("At the current"+str(tup)+"you will take the action,<move 2 missionary from side A to side B>,and then, your new state is ,"
                      +str((tup[0]-2,tup[1],0,tup[3]+2,tup[4],1)))                
            if validState((tup[0]-1,tup[1],0,tup[3]+1,tup[4],1)) == True:
                Recursive_dls((tup[0]-1,tup[1],0,tup[3]+1,tup[4],1),limit-1) 
                print("At the current"+str(tup)+"you will take the action,<move 1 missionary from side A to side B>,and then, your new state is ,"
                      +str((tup[0]-1,tup[1],0,tup[3]+1,tup[4],1)))    
            if validState((tup[0]-1,tup[1]-1,0,tup[3]+1,tup[4]+1,1)) == True:
                Recursive_dls((tup[0]-1,tup[1]-1,0,tup[3]+1,tup[4]+1,1),limit-1)
                print("At the current"+str(tup)+"you will take the action,<move 1 missionary and 1 cannibal from side A to side B>,and then, your new state is ,"
                      +str((tup[0]-1,tup[1]-1,0,tup[3]+1,tup[4]+1,1)))     
                
        elif tup[2]==0 and tup[5]==1:#boat in side B
            if validState((tup[0],tup[1]+1,1,tup[3],tup[4]-1,0)) == True:
                Recursive_dls((tup[0],tup[1]+1,1,tup[3],tup[4]-1,0),limit-1) 
                print("At the current"+str(tup)+"you will take the action,<move 1 cannibal from side B to side A>,and then, your new state is ,"
                      +str((tup[0],tup[1]+1,1,tup[3],tup[4]-1,0)))
               
            if validState((tup[0],tup[1]+2,1,tup[3],tup[4]-2,0)) == True:
                Recursive_dls((tup[0],tup[1]+2,1,tup[3],tup[4]-2,0),limit-1)  
                print("At the current"+str(tup)+"you will take the action,<move 2 cannibal from side B to side A>,and then, your new state is ,"
                      +str((tup[0],tup[1]+2,1,tup[3],tup[4]-2,0)))            
                
            if validState((tup[0]+2,tup[1],1,tup[3]-2,tup[4],0)) == True:
                Recursive_dls((tup[0]+2,tup[1],1,tup[3]-2,tup[4],0),limit-1) 
                print("At the current"+str(tup)+"you will take the action,<move 2 missionary from side B to side A>,and then, your new state is ,"
                      +str((tup[0]+2,tup[1],1,tup[3]-2,tup[4],0)))
                
            if validState((tup[0]+1,tup[1],1,tup[3]-1,tup[4],0)) == True:
                Recursive_dls((tup[0]+1,tup[1],1,tup[3]-1,tup[4],0),limit-1)    
                print("At the current"+str(tup)+"you will take the action,<move 1 missionary from side B to side A>,and then, your new state is ,"
                      +str((tup[0]+1,tup[1],1,tup[3]-1,tup[4],0)))
                
            if validState((tup[0]+1,tup[1]+1,1,tup[3]-1,tup[4]-1,0)) == True:
                Recursive_dls((tup[0]+1,tup[1]+1,1,tup[3]-1,tup[4]-1,0),limit-1) 
                print("At the current"+str(tup)+"you will take the action,<move 1 missionary and 1 cannibal from side B to side A>,and then, your new state is ,"
                      +str((tup[0]+1,tup[1]+1,1,tup[3]-1,tup[4]-1,0)))   
main()