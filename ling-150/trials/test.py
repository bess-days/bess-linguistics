#this page will input phonetic instructions


alveolar = ['d' ,'n','r','ch','l', 't']
doublecon = ['ll', 'zz', 'ff', 'dd']
velar = ['k', 'c' , 'g','x']
vowels = ['a', 'e', 'i', 'o', 'u']
word = ['fal']


for w in word:
    if len(w) == 3 and w.endswith(tuple(alveolar)):
        print(w.replace(w[1],'er',1)),
        print(w + 'lin')

    if w.endswith(tuple(doublecon)):
        print(w + 'ion')
        if 'ia' in w:
            print(w.replace('ia', 'ai', 1)),
    elif w.endswith(tuple(velar)) and not w.endswith('k'):
            print(w + 'on')
    elif w.endswith(tuple(velar)) and w.endswith('ck'):
            print(w.replace('ck', 'cian', 1))

    if len(w) == 3 and not w.endswith(tuple(alveolar)):
        print(w.replace(w[1], 'ai', 1))
        print(w + 'an')



