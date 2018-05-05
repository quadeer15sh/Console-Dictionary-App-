import json
from difflib import get_close_matches
data=json.load(open("data.json","r"))
def translate(word):
    if word in data:
        return(data[word])
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Sorry, did you mean %s ? Press Y if YES, or N if NO: " % get_close_matches(word,data.keys())[0])
        if yn=='Y':
            return get_close_matches(word,data.keys())[0]
        elif yn=='N':
            return "Word doesn't exist. Please double check it."
        else:
            return "Invalid Input."
    else:
        return "Word doesn't exist. Please double check it."
word=input("Enter a term: ")
word=word.lower()
output=translate(word)
if type(output)==list:
    for items in output:
        print(items)
else:
    print(output)
    
