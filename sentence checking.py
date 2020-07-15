#sentence checking
#AUCSS460
#Adam Sun 
#1497030 
agenda = []
kb = []
def main():
    inputKnowledge()
    query = input("What is your Query? \n")
    forwardAl(query)
#class for knowledgebank
class KB:
    def __init__(self,premise,conclusion,count):
        self.premise = premise
        self.conclusion = conclusion
        self.count = count
        
    def deleteC(self):
        self.count = self.count - 1
#check string and return premise,conclusion
def check(sentence):
    premise = []
    conclusion = ""
    for i in range(len(sentence)):
        if sentence[i] == "^":
            pass
        elif sentence[i] != ">" and i !=len(sentence)-1 and sentence[i] != "=" and sentence[i-1] !=">":
            premise.append(sentence[i])
        if i == len(sentence)-1 and sentence[i-1] == ">":
            conclusion = sentence[i]
    return premise,conclusion
#ask user to input agenda and rules
def inputKnowledge():
    i = 0
    kbNumber =0
    while i < 8:
        userInput = input("Please input knowledge base:(type 'exit' if you want to stop)\n")
        if userInput == "exit":
            print("stopped")
            break       
        elif len(userInput) == 1:
            agenda.append(userInput)
            print("Agenda[" , len(agenda)-1 ,"]" , agenda[len(agenda)-1])
        else:
            result = check(userInput)
            kb.append(KB(result[0],result[1],len(result[0])))
            print("KB[",len(kb)-1,"]:",kb[kbNumber].premise,"conclusion:",kb[kbNumber].conclusion,"count:",kb[kbNumber].count)  
            kbNumber=kbNumber+1
        i = i + 1    
#print rule properly
def printRule(list,conclusion,count):
    length = len(list)
    for i in range(length):
        if i != 0:
            print("^",end = '')
        print(list[i],end = '')
    print("=>",conclusion,", count:",count)
#forwardAlgorithm
def forwardAl(query):
    print("=============")
    print("Forward chaining algorithm starts")
    print("=============")
    j = 0
    lengthKnow = len(kb)
    while j != len(agenda):
        print("*****","Current agenda",agenda[j],"*****")
        if agenda[j] == query:
            print("Goal Achieved")
            print("The query ", query,"is true based on the knowledge.")
            
        for o in range(lengthKnow):
            if agenda[j] in kb[o].premise:
                printRule(kb[o].premise,kb[o].conclusion,kb[o].count)
                print("Premise",agenda[j],"matched agenda")
                print("Count is reduced to 1")
                kb[o].deleteC()
                if kb[o].count == 0:
                    agenda.append(kb[o].conclusion)
                    print("Agenda",kb[o].conclusion,"is created")
        j = j + 1    
main()