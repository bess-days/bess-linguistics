import colored
from coloring import *
from definitions import alveolar, syllabic, swede_syllabic, bilabial, vowels, velar, rcolored, palatal, doublecon, \
    glottal

with open("word.txt", "r") as f:
    word = f.read()

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


if len(word) <= 3:
    word = word.replace('oo', 'U', 1)
    word = word.replace('ee', 'I', 1)
    word = word.replace('ea', 'I', 1)
    word = word.replace('ou', 'W', 1)
    word = word.replace('oi', 'I', 1)
    word = word.replace('ai', 'A', 1)
    word = word.replace('ay', 'A', 1)
    word = word.replace('oy', 'U', 1)
    print('vvv-3')
    if word[1] in vowels and not word[2] in vowels:
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        word = word.replace('a', 'æ', 1)
        word = word.replace('o', 'ɔ', 1)
        word = word.replace('u', 'ʌ', 1)
        word = word.replace('i', 'ɪ', 1)
        word = word.replace('e', 'ɜ', 1)
        print(word, 'CVC replacement 3')

if len(word) >= 4:
    word = word.replace('oo', 'U', 1)
    word = word.replace('ee', 'I', 1)
    print('eeee')
    print(word)
    word = word.replace('ea', 'I', 1)
    word = word.replace('ou', 'W', 1)
    word = word.replace('oi', 'I', 1)
    word = word.replace('ai', 'A', 1)
    word = word.replace('ay', 'A', 1)
    word = word.replace('oy', 'U', 1)
    print(word)
    print('VVC')
    if len(word) >= 4:
        word = word.replace('a', 'A', 1)
        word = word.replace('o', 'O', 1)
        word = word.replace('u', 'U', 1)
        word = word.replace('i', 'I', 1)
        word = word.replace('e', 'I', 1)
        print(word, 'CVC replacement')

with open("word.txt", "w") as f:
    word = f.write(word)
import replace2
