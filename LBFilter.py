from wordfreq import zipf_frequency

def filter_words(wordlist, num, userset):
    filteredWords = []
    
    for word in wordlist:
        if zipf_frequency(word, 'en') >= num:
              filteredWords.append(word)
              
    
    validguesses = set()

    for word in filteredWords:
        remainingletters = userset-set(word)
        for guess in filteredWords:
                if (set(guess).intersection(remainingletters) == remainingletters) and (guess[-1] == word[0]):
                        validguesses.add((guess, word))
                elif (set(guess).intersection(remainingletters) == remainingletters) and (word[-1] == guess[0]): 
                        validguesses.add((word, guess))

    if len(validguesses) > 0:
        return validguesses
    else:
          return False