#TODO update this inventory, try and make it match with the steps
doublecon = ['ll','tt','ss']
bilabial = ['p','b','m']
labiodental = ['f','v']
alveolar = ['t','n','r','d','s', 'ʤ','ʃ','θ','ʧ']
retroflex = ['n>', 'l>']
velar = ['k','g']
palatal = ['c','j']
glottal = ['g=']
swede_syllabic = ['n>', 'l>']
syllabic = ['n=', 'm=', 'l=']
rcolored = ['i-','a-']
vowels = ['a', 'e', 'i', 'o', 'u']
inventory = bilabial + labiodental + alveolar + retroflex + velar + palatal + glottal + vowels

word = input('Word: ')
if word[-1:] in inventory:
    print('Okay')
else:
    print('Not Okay')
