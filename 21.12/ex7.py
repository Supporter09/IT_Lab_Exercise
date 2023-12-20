import json

with open('C:/Users/Admin/Desktop/Code/IT_Lab_Exercise/21.12/test.inp','r') as f:
    word_dict = {}
    for line in f:
        wordslist = line.split(' ')
        for word in wordslist:
            word_dict[word] = word_dict.get(word, 0) + 1

with open('test.out', 'w') as out:
    out.write(json.dumps(word_dict))