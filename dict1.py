import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))
#print(data)
#data["rain"]
#data.keys()

def translate(word):
    word= word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did You Mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(word,data.keys())[0])
        if yn== "Y" or yn == "y":
            return data[get_close_matches(word,data.keys())[0]]
        
        elif yn== "N" or yn== "n":
            return "The Word Does not exist, Plz  double check it."
        else:
            return "we did not understand querry"
    else:
        return "The word does not exist, Please double check it. "

word = input("Enter a word: ")

output =translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)





