import pyperclip as pc
#TODO add /i/ extended for every /i/
#TODO Every vowel after another vowel becomes an /i/
#TODO if word ends in vowel and swedish syllabic
#TODO if ends in alveolar and 'eel'
#TODO add subset for making things adjectives, words inputted all act as nouns or basic adjectives - ie not adverbs or abstract feelings
alveolar = ['d', 'l', 'n', 't', 's']
doublecon = ['ll', 'zz', 'ff', 'dd']
velar = ['k', 'c', 'g', 'x']
bilabial = ['b','p','m']
vowels = ['a', 'e', 'i', 'o', 'u']
syllabic = ['n=', 'm=', 'l=']
swede_syllabic = ['n>', 'l>']
gollatal = ['g?']
seperated = alveolar + doublecon + velar + vowels + bilabial
word = str(input('Word: '))


for w in word:
    if word.endswith(tuple(doublecon)):
        word = word + 'an'
        if word[1] in list(vowels):
            word = word[:2] + ':' + word[2:]
            break
        else:
            break
#CK edit >3
    elif word.endswith(tuple(velar)) and len(word) > 3:
        word = word + syllabic[1]
        if 'ck' in word:
            word = word.replace('ck', 'k', 1)
            if word[1] in tuple(vowels):
                word = word[:2] + ':' + word[2:]
                break
            else:
                break
        else:
            if word[1] in tuple(vowels):
                word = word[:2] + ':' + word[:]
                break
            else:
                pass
#3-letter
    if len(word) == 3:
        #Ends in what provided
        if word.endswith(tuple(seperated)):
            #ends with vowels
            if word.endswith(tuple(vowels)):
                if word[1] in vowels:
                    word = word[:2] + ':' + 'g?' + syllabic[2]
                    break
                else:
                    word = word + syllabic[2]
            #ends with alveolar
            if word.endswith(tuple(alveolar)):
                if word[1] in vowels:
                    word = word[:2] + ':' + word[2:] + syllabic[2]
                    break
                else:
                    pass
            #ends with velar
            if word.endswith(tuple(velar)):
                if word[1] in vowels:
                    word = word[:2] + ':' + word[2:] + swede_syllabic[0]
                    break
                else:
                    pass
            # ends with bilabial
            if word.endswith(tuple(bilabial)):
                if word[1] in vowels:
                    word = word[:2] + ':' + word[2:] + syllabic[1]
                    break
                else:
                    pass

        #if any other letter
        else:
            if word[1] in vowels:
                word = word[:2] + ':' + word[2:] + swede_syllabic[0]
            else:
                word = word + 'g?' + syllabic[2]
    if 3 < len(word) < 6:
        #Ends in what provided
        if word.endswith(tuple(seperated)):
            #ends with vowels
            if word.endswith(tuple(vowels)):
                if word[1] in vowels and word[2] in alveolar or velar:
                    word = word[:2] + ':' + word[2:3] + 'g?' + syllabic[2]
                    break
                else:
                    word = word + syllabic[2]
            #ends with alveolar
            if word.endswith(tuple(alveolar)):
                if word[2] in vowels and word[3] in vowels:
                    print('hi')
                    word = word[:3] + ':' + word[4:]

                if word[1] in vowels and word[2] in alveolar or velar:
                    word = word[:2] + ':' + word[3:] + syllabic[2]
                    break
                else:
                        word = word[:3] + ':' + word[4:] + syllabic[2]
            #ends with velar
            if word.endswith(tuple(velar)):
                if word[1] in vowels:
                    word = word[:2] + ':' + word[2:] + swede_syllabic[0]
                    break
                else:
                    if word[2:] in vowels:
                        word = word[:3] + ':' + word[2:] + swede_syllabic[0]
                        break

            # ends with bilabial
            if word.endswith(tuple(bilabial)):
                if word[1] in vowels:
                    word = word[:2] + ':' + word[3:] + syllabic[1]
                    break
                else:
                        word = word[:3] + ':' + word[4:] + syllabic[1]
                        break
        #if any other letter
        else:
            if word[1] in vowels:
                word = word[:2] + ':' + word[2:] + swede_syllabic[0]
            else:
                word = word + 'g?' + syllabic[2]

for w in word:
    if word[1] in vowels and word[3] in vowels:
        word = word.replace(word[3], 'g?',1)
print('Below is the IPA:')

word = word.replace('tS', 'ʧ')
word = word.replace('th', 'θ')
word = word.replace('sh', 'ʃ', )
word = word.replace('n=', ' ̩̩n')
word = word.replace('l=', ' ̩̩l')
word = word.replace('m=', ' ̩̩m')
word = word.replace('ll', 'l')
word = word.replace('n>', 'ɳ')
word = word.replace('l>', 'ɭ')
word = word.replace('g?', 'ʔ')
word = word.replace('y', '')

IPA = ('[' + word + ']')
print(IPA)
pc.copy(IPA)
word = list(word)

#Adding aditional vowel changing rules

# Checks wether applicable
for i in range(len(word)):
    for i in range(len(word)):
        if word[i] == any(vowels) == word[i+1]:
            print('First part: This word cannot be calculated accuratly by system.')
            break
    for i in range(len(word) -3):
        if word[i] == word[i+1] == word[i+2]:
            print('Second part:This word cannot be calculated accuratly by system.')
            break
        else:
            pass

