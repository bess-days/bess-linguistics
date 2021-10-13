#Working on a third part of the function to eliminate any results that aren't phonetically possibly
#TODO make sure 'i' appear
vowels = ['a', 'e', 'i', 'o']
word = str(input('Word: '))
word = list(word)
# Checks wether applicable
for i in range(len(word)):
    if word[i] == vowels[i] == word[i+1]:
        print('First part: This word cannot be calculated accuratly by system.')
        break
    else:
        pass
    if word[i] == word[i+1] == word[i+2]:
        print('Second part:This word cannot be calculated accuratly by system.')
        break
    else:
        pass
