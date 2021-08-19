# This code is working on data present in json file

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]
        
    elif len(get_close_matches(word, data.keys())):
        yn = input("Did you mean '%s' instead? Enter Y if yes or N id no: " \
                    % get_close_matches(word, data.keys())[0])

        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]

        elif yn =="N":
            return "The word doesn't exist. Please double check it."

        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."

while True:
    word = input("Enter word: ")
    if word=="q":
        break
    output = translate(word)
    if isinstance(output,list):
        for item in output:
            print(item)
    else:
        print(output)