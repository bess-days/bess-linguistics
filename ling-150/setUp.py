#this page will input phonetic instructions


alveolar = ['d' ,'n','r','ch','ll', 't']
doublecon = ['ll', 'zz', 'ff', 'dd']
velar = ['k', 'c' , 'g','x']

def adjectives(word):
    #words, specifically adjectives with 3 letters tend to have a CVC pattern with a short vowel in the middle
    #based on that, I will expand the vowel to a :i or ae depending on the manner of articulation
    if len(word) == 3 and not word.endswith(tuple(alveolar)):
        print(word.replace(word[1],'ee',1))
        #I made alveolar false because many words that end in alveolars can contian the rather rare double letters
    elif len(word) == 3 and word.endswith(tuple(alveolar)):
        print(word.replace(word[1], 'ai', 1))
    elif word.endswith(tuple(alveolar)):
        print(word + 'an')
        #I chose 'an' because 'en' can result in the addition of meaning like 'thick-en'
    elif word.endswith(tuple(doublecon)):
        print(word + 'in')
        #I chose 'in' for double constants cause it is common use in latin languages to add more meaning to words
    elif word.endswith(tuple(velar)):
        print(word + 'on')


adjectives("basic")
#Type word between the ()
