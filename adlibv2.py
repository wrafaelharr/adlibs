import pyttsx3
import numpy as np
from nltk.corpus import wordnet as wn

#make speaking engine
engine = pyttsx3.init()

#find list of words
noun = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
verb = {x.name().split('.', 1)[0] for x in wn.all_synsets('v')}
adj = {x.name().split('.', 1)[0] for x in wn.all_synsets('a')}
restricted = ['be', 'do', 'has', 'got', 'a', 'as', 'no', 'of', 'to', 'if', 'or', 'there', 'their', 'theyre', 'which',
              'can', 'my', 'mine', 'her', 'his', 'hers', 'hes', 'he', 'she', 'I', 'they', 'them', 'when', 'how',
              'where', 'when', 'why', 'near', 'here', 'any', 'theres', 'heres', 'Im', 'Id', 'it', 'its', 'howd',
              'cant', 'at']

#read the file
words = []
file = open('C:\\Users\\Lrhgr\\white.txt', 'r')
for line in file:
    for word in line.split():
        words.append(word)
        
#lines = file.readlines()
file.close()

#ads to lib
nouns = ['butthole', 'gun', 'blow', 'killishnucough', 'cunnal', 'noodle', 'dome', 'chicken', 'bruv', 'JohnGreen', 
         'child', 'dude', 'moek-boy', 'Tyga', 'keggstand', 'bruh', 'Princeton', 'crime', 'detAss', 'chili', 'cunt',
         'buster']
verbs = ['jogging', 'shooting', 'jihading', 'kamakazing', 'attack', 'protect', 'defending', 'destroy', 'grinding', 
         'buttchugging', 'boofing', 'sniffing', 'waiting', 'chillin', 'rimming', 'pegging', 'slaughtering', 'dripping']
adjs = ['black', 'throbbing', 'enlarged', 'expansive', 'ikky', 'fucked', 'edible', 'sweet', 
        'yummy', 'domed', 'chicken', 'tasty', 'D-lushis', 'prime', 'chilly', 'astonishing', 'salty', 'sensual']

#mix up words
    #analyze for available spots
new_lines = []
temp_line = ''
new_word = ''
old_word = ''
end = False
for i in words:
    if (i[-1] == "."):
        end = True
    if i in restricted:
        if temp_line == '':
            temp_line = i
        else:
            temp_line = temp_line + ' ' + i
    else:
        rnum = np.random.randint(0, 100)
        if (rnum < 100) & (i in adj):
            old_word = new_word
            while old_word == new_word:
                new_word = np.random.choice(adjs)
        elif (rnum < 101) & (i in verb):
            old_word = new_word
            while old_word == new_word:
                new_word = np.random.choice(verbs)
            if old_word == 'to':
                
                new_word = new_word[:(len(new_word) - 3)]
        elif (rnum < 100) & (i in noun):
            old_word = new_word
            while old_word == new_word:
                new_word = np.random.choice(nouns)
            if i[-1] == 's':
                new_word += 's'
        else:
            new_word = i
        if temp_line == '':
            temp_line = new_word
        else:
            temp_line = temp_line + ' ' + new_word
    
    if (end):
        new_lines.append(temp_line)
        temp_line = ''
        end = False
        

#speak
for i in range(len(new_lines)):
    print(new_lines[i])
    #speak
    engine.say(new_lines[i])
    engine.runAndWait()
    
    #user input
    user_in = input("stop?: ") 
    
    #stop
    if user_in == 'stop':
        break
    
engine.runAndWait()