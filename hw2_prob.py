#hw2_prob.py
#adamSun
import os
files = os.listdir("C:/Users/adams/OneDrive/Documents/Data/Data/Train/ham")
wordBank = []
def main():
    for atoms in files:
        readTxt(atoms)   
    #use this code in the first run to read all words
    #writeF()    
    
    #then use codes below to caculate p value 
    readP()       
    writeFinal()    
    
def readTxt(filename):
    f = open("C:/Users/adams/OneDrive/Documents/Data/Data/Train/ham/"+filename,"r")
    for x in f:
        temp = x
        words = temp.split(" ")
        for word in words:
            exist = False
            existNu = 0
            for i in range(len(wordBank)):
                if word == wordBank[i][0]:
                    exist = True
                    existNu = i
                    break
            if exist == True:
                wordBank[existNu][1] =  wordBank[existNu][1] + 1
            else:
                wordBank.append([word,1])

def getTotalW():
    total = 0
    for j in range(len(wordBank)):
        total = total + wordBank[j][1]
    return total

def writeF():
    with open("probabality.txt","w") as outputF:
        for j in range(len(wordBank)):
            word = wordBank[j][0]
            wordNumber = wordBank[j][1]
            for number in range(wordNumber):
                outputF.write("%s\n" % word)
def writeFinal():
    with open("probabality.txt","w") as outputF:
        for j in range(len(wordBank)):
            word = wordBank[j][0]
            wordNumber = wordBank[j][1]
            wordTotal = getTotalW()
            outputF.writelines(word+" "+str(wordNumber/wordTotal)+"\n")
            
def readP():
    f = open("p.txt","r")
    for x in f:
        temp = x
        words = temp.split()
        for word in words:
            exist = False
            existNu = 0
            for i in range(len(wordBank)):
                if word == wordBank[i][0]:
                    exist = True
                    existNu = i
                    break
            if exist == True:
                wordBank[existNu][1] =  wordBank[existNu][1] + 1
            else:
                wordBank.append([word,1])
               
main()