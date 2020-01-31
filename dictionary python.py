import json
from difflib import get_close_matches

data = json.load(open('Downloads/data.json'))

def dictionary(words):
    words = words.lower()
    if words in data:
        return data[words]
    elif len(get_close_matches(words, data.keys())) > 0:
        y_or_n = input('Did you mean %s instead?  Enter Y or N: ') % get_close_matches(words, data.keys())[0]
        if y_or_n == 'Y' or 'y':
            return data[get_close_matches(words, data.keys())[0]]
        elif y_or_n == 'N' or 'n':
            return 'Word doesnt not exist.'
        else:
            return 'I dont understand what you are attempting to define.'
    else:
        return 'Word does not exist, please check your spelling.'

word = input('Enter word: ')

output = dictionary(word))

if type(output) == list:
    for item in output:
        print(~~~ * 20)
        print(item)
        print(~~~ * 20)

else:
    print(~~~ * 20)
    print(output)
    print(~~~ * 20)