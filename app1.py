import json
import difflib
# from difflib import SequenceMatcher
from difflib import get_close_matches

dict = json.load(open("data.json"))

def meaning(s):
    x=get_close_matches(s,dict.keys())
    # z=SequenceMatcher(None,s,y).ratio()
    if s in dict:
        return(dict[s])
    elif len(x)>0:
        y=get_close_matches(s,dict.keys())[0]
        yn=input("Is '%s' the word you're looking for? If yes enter Y, else enter N :" %y) #%s lets you insert anything you want if you put %whatever after it
        if yn.lower() == "y":
            return(dict[y])
        else:
            return("Word not present in dictionary, please check again.")
    else:
        return("Word not present in dictionary, please check again.")

word = input("Enter word: ")
output = meaning(word.lower())

if type(output)== list: #here list means type list. It should've been in blue. 
    for i in output:
        print(i)
else:
    print(output)
