#ass3.py
#Adam Sun
#1497030
import os
import random 
files = os.listdir("C:/Users/adams/OneDrive/Documents/Data/Data/Train/ham")
inputN = []
oneEightNine = []
hidden_layer = []
answer = []
def main():
    weight = 0
    #then use codes below to caculate p value 
    readTrain()
    readAnswer()   
    for i in range(100):
        hidden(weight)
        newList = fliter(hidden_layer)
        rightrate = compareResult(newList,answer)
        print(rightrate)
        weight = random.randint(-1,1)
        if rightrate >= 0.9:
            print("epoch is ", i)
            break
    
    
def readTrain():
    f = open("C:/Users/adams/Downloads/train.txt","r")
    for x in f:
        temp = x
        counter = 0
        tempLast = []
        words = temp.split(" ")
        for word in words:
            if word != 0 and word != 1:
                if word == '1.0000' or word == '0.0000':
                    inputN.append(float(word))
            elif word == 0 or word == 1:  
                tempLast.append(word)
            if len(tempLast) == 3:
                print(tempLast)
                tempLast = []
def readAnswer():
    f = open("C:/Users/adams/Downloads/correct_answer.txt","r")
    for x in f:
        temp = x
        words = temp.split(" ")
        for word in words:
            if word != 0 and word != 1:
                if word == '1' or word == '8' or word == '9':
                    answer.append(int(word))

def hidden(weight):
    sum = 0.0000
    counter = 0
    for i in range(len(inputN)):
        if counter != 256:
            sum = sum + inputN[i] * weight
        counter = counter + 1
        if counter == 256:
            hidden_layer.append(sum/10)
            sum = 0
            counter = 0
def fliter(listA):
    listB = []
    for i in listA:
        if i <=8:
            listB.append(1)
        elif i > 8 and i <= 9:
            listB.append(8)
        else:
            listB.append(9)
    return listB
def compareResult(ListA,ListB):
    total = len(ListB)
    error = 0
    for i in range(total):
        if ListA[i] != ListB[i]:
            error = error + 1
    right = 1 - (error/total)
    return right
main()