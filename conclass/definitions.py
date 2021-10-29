import linecache
def theline(thefilepath, desired_line_number):
    theline = linecache.getline(thefilepath, desired_line_number)
    print(theline)


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
def writeWord1(word):
    with open('word.txt', 'w') as f:
        print('Enters')
        f.write(word)
def writeWord2(word):
    with open('word.txt', 'a+') as f:
        print('Enters')
        f.write(word)

def readWord1():
    with open("word.txt") as f:
        word = f.readline().rstrip()
        print(word)

def replace1(word):
        word = word.replace('sh', 'ʃ', 1)
        word = word.replace('th', 'θ', 1)
        word = word.replace('j', 'ʤ', 1)
        word = word.replace('ch', 'ʧ', 1)


def vvreplace(word):
    for i in range(0, len(word) - 1):
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
            return word
def vreplace3(word):
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
        return word
def vreplace(word):
    if len(word) >= 4:
        word = word.replace('a', 'A', 1)
        word = word.replace('o', 'O', 1)
        word = word.replace('u', 'U', 1)
        word = word.replace('i', 'I', 1)
        word = word.replace('e', 'I', 1)
        print(word, 'CVC replacement')

def write(word):
    f = open("word.txt", "a+")
    f.write(word+'\n')

def read(line):
    f = open("word.txt")
    word = f.readlines(line)
    print(word)




