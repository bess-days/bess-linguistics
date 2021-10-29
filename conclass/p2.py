import colored
from coloring import *
from definitions import theline, write
word = str(theline("word.txt", 1))
print(word)


bilabial = ['p', 'b', 'm']
labiodental = ['f', 'v']
alveolar = ['t', 'n', 'r', 'd', 's', 'ʤ', 'ʃ', 'θ', 'ʧ', 'l']
retroflex = ['n>', 'l>']
velar = ['k', 'g']
palatal = ['c', 'j']
glottal = ['g?']
swede_syllabic = ['n>', 'l>']
syllabic = ['n=', 'm=', 'l=']
rcolored = ['i-', 'a-']
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
doublecon = ['ll', 'tt', 'ss']
inventory = bilabial + labiodental + alveolar + retroflex + velar + palatal + glottal + vowels
# vowel-level 1(checking fro VV)
for i in range(0, len(word)-1):
    if word[i] in vowels and word[i + 1] in vowels:
        word = word.replace('oo', 'U', 1)
        word = word.replace('ee', 'I', 1)
        word = word.replace('ea', 'I', 1)
        word = word.replace('ou', 'W', 1)
        word = word.replace('oi', 'I', 1)
        word = word.replace('ai', 'A', 1)
        word = word.replace('ay', 'A', 1)
        word = word.replace('oy', 'U', 1)
        print(word)
    else:
        pass
for w in word:
    if len(word) <= 3:
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        if word[1] in vowels and not word[2] in vowels:
            vowels = ['a', 'e', 'i', 'o', 'u', 'y']
            word = word.replace('a', 'æ', 1)
            word = word.replace('o', 'ɔ', 1)
            word = word.replace('u', 'ʌ', 1)
            word = word.replace('i', 'ɪ', 1)
            word = word.replace('e', 'ɜ', 1)
            print(word, 'CVC replacement')
        else:
            pass
for w in word:
    if len(word) >= 4:
        word = word.replace('a', 'A', 1)
        word = word.replace('o', 'O', 1)
        word = word.replace('u', 'U', 1)
        word = word.replace('i', 'I', 1)
        word = word.replace('e', 'I', 1)
        print(word, 'CVC replacement')
choice = str(input('Do you want to continue? Y/N: '))
for c in choice:
    if choice == 'Y':
        print('hi')
        import p2
    if choice == '2':
        print('bye')
        exit()
write(word)






