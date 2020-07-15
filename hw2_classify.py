#hw2_prob.py
#adamSun
#import math
word_spam = []
word_spam_P = []
word_ham = []
word_ham_P = []
p_spam = 0.15
p_ham = 0.85
read_email = []

def main():
    readTarget()
    readPfile()
    SpamR = checkSpam()
    HamR = checkHam()
    if SpamR >= HamR:
        print("Conclusion:This message in calssifed as Spam")
    else:
        print("Conclusion:This message in calssifed as Ham")
        
def readPfile():
    f = open("probability_spam_words.txt","r")
    fc = f.readlines()
    for value in fc:
        stringdata = value.split(" ")
        word_spam.append(stringdata[0])
        word_spam_P.append(stringdata[1])
    f.close()
    
    f2 = open("probability_ham_words.txt","r")
    fc2 = f2.readlines()
    for value2 in fc2:
        stringdata = value2.split(" ")
        word_ham.append(stringdata[0])
        word_ham_P.append(stringdata[1])
    f2.close()
def readTarget():
    fileName = input("what's the path of the txt file?")
    Target = open(fileName,"r")
    TargetStr = Target.readlines()
    for word in TargetStr:
        lineData = word.split(" ")
        for i in range(len(lineData)):
            read_email.append(lineData[i])
    
def checkSpam():
    totalp = math.log(p_spam,10)
    print("P(Spam) = ",p_spam)
    for i in range(len(read_email)):
        if read_email[i] in word_spam:
            listIn = word_spam.index(read_email[i])
            print("P(",read_email[i] ,"|Spam) = ",float(word_spam_P[listIn][0:6]))
            totalp = totalp + math.log(float(word_spam_P[listIn][0:6]),10)
    result = totalp
    print("log P(Spam|,all words) = ", result)
    return result

def checkHam():
    totalp = math.log(p_ham,10)
    print("P(Ham) = ",p_ham)
    for i in range(len(read_email)):
        if read_email[i] in word_ham:
            listIn = word_ham.index(read_email[i])
            print("P(",read_email[i] ,"|Ham) = ",float(word_ham_P[listIn][0:6]))
            totalp = totalp + math.log(float(word_ham_P[listIn][0:6]),10)
    result = totalp
    print("log P(Ham|,all words) = ", result)
    return result

main()