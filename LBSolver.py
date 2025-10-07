import string

def solve_letters(userletters):
    with open('words_alpha.txt', 'r') as file:
    
        wordlist = [line.strip() for line in file]

    wordlist = [word for word in wordlist if not word[0].isupper()]



    wordlist = [word for word in wordlist if len(word) >= 3]

    print(userletters)

    userletters = [letters.lower() for letters in userletters]
    userletters = [letters for letters in userletters if letters != ' ']
    temp_letter = userletters[4]
    userletters[4] = userletters[7]
    userletters[7] = temp_letter

    print(userletters)




    alphabet = set(string.ascii_lowercase)

    
    groups = [userletters[i:i+3] for i in range(0, len(userletters), 3)]




    userset = set(userletters)
    
    badletters = alphabet-userset

    wordlist = [word for word in wordlist if not badletters.intersection(set(word))]


    goodwords = []
    for word in wordlist:
        for index, letter in enumerate(word):
                if (index == (len(word)-1)):
                        goodwords.append(word)
                else:
                        if (word[index + 1] == word[index]):
                                break
                        

    allowedwords = []

    for word in goodwords:
        for index, letter in enumerate(word):
                if (index == (len(word)-1)):
                        allowedwords.append(word)
                else:
                        if (((word[index] in groups[0]) and (word[index+1] in groups[0])) or ((word[index] in groups[1]) and (word[index+1] in groups[1])) or ((word[index] in groups[2]) and (word[index+1] in groups[2])) or ((word[index] in groups[3]) and (word[index+1] in groups[3]))):
                                break

    validguesses = {'ZORA IS AWESOME'}

    for word in allowedwords:
        remainingletters = userset-set(word)
        for guess in allowedwords:
                if (set(guess).intersection(remainingletters) == remainingletters) and (guess[-1] == word[0]):
                        validguesses.add((guess, word))
                elif (set(guess).intersection(remainingletters) == remainingletters) and (word[-1] == guess[0]): 
                        validguesses.add((word, guess))
                        


    for items in validguesses:
        print(items)
        print("----------------------------------")

    print(len(validguesses))



