import json

data = json.load(open('dictionary project/data.json'))

def dictionary(words):
    words = words.lower()
    if words in data:
        return data[words]
    else:
        return 'Word does not exist, please check your spelling.'

word = input('Enter word: ')

print(dictionary(word))
