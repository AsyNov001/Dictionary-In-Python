import json as js
from difflib import get_close_matches as gs
Data = js.load(open("Data.json"))

def Translate(Word):
    Word = Word.lower()
    if(Word in Data):
        list1 = Data[Word]
        if(type(list1) == list):
            for i in list1:
                print(i)
            return "All Found Meanings"
        else:
            return Data[Word]
    else:
        Temp_l = gs(Word,Data.keys(),3,0.5)
        if(len(Temp_l) == 0):
            return "It is a Meaningless Word"
        else:
            print("The Closest Found Word is")
            print(Temp_l[0])
            choice = input("Do you want its Meaning")
            if(choice == "Y"):
                return Data[Temp_l[0]]
            else:
                return "You said No"

Word = input("Enter the Word Which to look up in dictionary")
print(Translate(Word))
