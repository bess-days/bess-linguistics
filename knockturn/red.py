from word2word import Word2word
from nltk.corpus import wordnet
import random


#Creating a list
synonyms = []
themesyns = []
for syn in wordnet.synsets("red"):
    for lm in syn.lemmas():
             synonyms.append(lm.name())
for syn in wordnet.synsets("danger"):
    for lm in syn.lemmas():
             themesyns.append(lm.name())
sset = synonyms + themesyns


en2fr = Word2word("en", "fr")
redFr = en2fr("red")


en2lt = Word2word("en", "lt")
redLt = en2lt("red")


en2es = Word2word("en", "es")
redEs = en2es("red")


en2de = Word2word("en", "de")
redDe = en2de("red")

fsyn = redDe + redLt + redFr + sset
fsetsyn = set(fsyn)



redbase = random.choice(list(fsetsyn))
s = redbase
dt = s.replace('e','t', 1)
const = ['q', 'w','r','t','p','s','d', 'f','g','h', 'k','l','z','x', 'c', 'v', 'b','n', 'm']
gl = s.replace('ge','l',1)



def firstreplace():
    if 'red' in redbase:
        print(s.replace('red', '', 1))
    elif '-' in redbase:
        pass
    elif 'j' in redbase:
        print(s.replace('j','l',2))
    elif 'ge' in redbase:
        print(s.replace('ge', 'lion',1))
        print(s.replace('ge', 'sion', 1))
    elif redbase.endswith('d'):
        print(s.replace('d','lium',1))
        print(s.replace('d', 'lium', 1))
        print(s.replace('d', 'lious', 1))
    elif redbase.endswith('y'):
        print(s.replace('y','iel',1))
        print(s.replace('y', 'ion', 1))
        print(s.replace('y', 'ios', 1))
    elif redbase.endswith('s'):
        print(s.replace('s', 'ion', 1))
        print(s.replace('s', 'ius', 1))
        print(s.replace('s', 'iun', 1))
    elif redbase.endswith(tuple(const)):
        print(redbase + 'ium')
        print(redbase + 'ious')




firstreplace()