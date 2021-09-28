#this page will input phonetic instructions


alveolar = ['d' ,'n','r','ch','ll', 't']
doublecon = ['ll', 'zz', 'ff', 'dd']
velar = ['k', 'c' , 'g','x']
vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Far'
w = 'Far'
for w in word:
    if len(w) >= 1:
        print("The word is:")
        if len(w) == 3 and not w.endswith(tuple(alveolar)):
            print(w.replace(w[1],'ee',1))
        elif len(w) == 3 and w.endswith(tuple(alveolar)):
            print(w.replace(w[1], 'ai', 1))
        elif 'ia' in w:
            print(w.replace('ia', 'ai', 1))
        elif w.endswith(tuple(alveolar)):
            print(w + 'an')
        elif w.endswith(tuple(doublecon)):
            print(w + 'ion')
        elif w.endswith(tuple(velar)) and not w.endswith('k'):
            print(w + 'on')
        elif w.endswith(tuple(velar)) and w.endswith('ck'):
            print(w.replace('ck', 'cian', 1))
    else:
        print("Ummm")


