alveolar = ['d', 'n','l', 't']
doublecon = ['ll', 'zz', 'ff', 'dd']
velar = ['k', 'c', 'g', 'x']
vowels = ['a', 'e', 'i', 'o', 'u']
word = 'fat'

def endings(word):
    if word.endswith(tuple(alveolar)) and len(word) > 3 and not word.endswith('l' or 'n' or 'r' or 't'):
        print(word + 'el')
        #why these paramaters? 'rel' is a root for religion, relationship, nel isn't a common lexicon combiniation, since 'l' could be double or would be a VcVC which would give the final 'e' a different vowel and  the'l' sound
    #words, specifically adjectives with 3 letters tend to have a CVC pattern with a short vowel in the middle
    elif len(word) == 3 and word.endswith(tuple(alveolar)):
        print(word.replace(word[1], 'ai', 1))
    elif word[1] in list(vowels) and len(word) == 3 and not word.endswith(tuple(vowels)):
        print(word[:2] + ':' + 'rn')
        # based on that, I will expand the vowel to a :i or ae depending on the manner of articulation
    elif word.endswith(tuple(velar)) and len(word) > 3 and not word.endswith('k'):
        print(word + 'on')
    elif word.endswith(tuple(velar)) and len(word) > 3 and word.endswith('ck'):
        print(word.replace('ck', ':kern',1))
    elif word.endswith(tuple(vowels)) and len(word) > 3 and word.endswith('o' or 'a' or 'e'):
        print(word + 'rn')
    elif word.endswith(tuple(doublecon)):
        print(word + 'an')
    elif word.endswith(tuple(alveolar)) and len(word) == 3 and not word.endswith('l' or 'n' or 'r'):
        print(word.replace(word[2], 'nt' , 1))
        print(word.replace(word[1], 'ee',1))
    elif word.endswith(tuple(alveolar)) and len(word) == 3 and word.endswith('l' or 'n' or 'r'):
        print(word + 'nar')
        print(word.replace(word[1], 'e', 1))
    elif 'ea' in word:
        print(word.replace('ea', 'ai',1))


#other rules I could not code: if resembles current english word - insert a different stress or stop'
#does not keep the first vowel - either makes it longer it or makes it a dipthong


endings("suck")





