
word = 'suck'

alveolar = ['d', 'n','l', 't', 's']
doublecon = ['ll', 'zz', 'ff', 'dd']
velar = ['k', 'c', 'g', 'x']
vowels = ['a', 'e', 'i', 'o', 'u']
syllabic = [ '̩̩n', '̩̩m','l̩̩']
swede_syllabic = ['ɳ', 'ɭ']
ck_end = word.replace('ck','k',1)




def lexicon(word):
    for w in word:
        if word.endswith(tuple(alveolar)) and len(word) > 3:
            print(word + syllabic[2] )
        elif len(word) == 3 and word.endswith(tuple(alveolar)):
            print(word.replace(word[1], 'ai', 1))
        elif word[1] in list(vowels) and len(word) == 3 and not word.endswith(tuple(vowels)):
            print(word[:2] + ':' + syllabic[2])
        elif word.endswith(tuple(velar)) and len(word) > 3 and not word.endswith('k'):
            print(word + syllabic[0])
        elif word.endswith(tuple(velar)) and len(word) > 3 and word.endswith('ck'):
            print(ck_end + syllabic[1])
        elif word.endswith(tuple(vowels)) and len(word) > 3 and word.endswith('o' or 'a' or 'e'):
            print(word + syllabic[0])
        elif word.endswith(tuple(doublecon)):
            print(word + 'an')
        elif word.endswith(tuple(alveolar)) and len(word) == 3 and not word.endswith('l' or 'n' or 'r'):
            print(word.replace(word[2], 'nt' , 1))
            print(word.replace(word[1], 'ee',1))
        elif word.endswith(tuple(alveolar)) and len(word) == 3 and word.endswith('l' or 'n' or 'r'):
            print(word + 'ᶏ')
            print(word.replace(word[1], 'e', 1))
        elif 'ea' in word:
            print(word.replace('ea', 'ai',1))
    return  word
#other rules I could not code: if resembles current english word - insert a different stress or stop'


lexicon("suck")
#insert word above





