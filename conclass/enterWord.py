from coloring import *
from definitions import write
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

word = input('Word: ')
for w in word:
    if word.endswith('s'):
        print('The', chartreuse('system'), 'detects your inputed word might be a', violet('plural'))
        print('Is your word plural?')
        print('Type', sienna('Y for yes'), 'or', aquamarine('N for no'))
        plural = str(input('Y/N: '))
        plural.upper()
        print(plural)
        if plural == 'Y':
            print('Please re-enter your word to be singular')
            exit()
        if plural == 'N':
            print('Great! In the future, adding plurals will be adding a \"z\" sound no matter enviroment.')
            break
for w in word:
    if word.endswith('ly' or 'able' or 'er' or 'ed' or 'ing'):
        print(
        'The system detected suffixes that serve as bound morphemes providing tense or changing a word to an adverb.')
        print('Are you using the simplist syntax to relay your meaning and intention?')
        print('Type', sienna('Y for yes'), 'or', aquamarine('N for no'))
        simple = str(input('Y/N: '))
        simple.upper()
        if simple == 'Y':
            print(
            'Good to know! In this language, since the words being edited are often nouns or adjectives to '
            'describe '
            'a person,')
            print('or thing does not need to be edited with \"ly\" or \"able\" because the words in this language'
              'are exclusively positive, they can\'t be negated')
        else:
            print('Please re-input your word.')
            exit()
write(word)

import r1


