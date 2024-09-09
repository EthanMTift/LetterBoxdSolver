from english_words import get_english_words_set
import string
#web2lowerset = get_english_words_set(['web2'], lower=False, alpha=True)
#wordlist = list(web2lowerset)

with open('words_alpha.txt', 'r') as file:
    
    wordlist = [line.strip() for line in file]

wordlist = [word for word in wordlist if not word[0].isupper()]



wordlist = [word for word in wordlist if len(word) >= 3]




alphabet = set(string.ascii_lowercase)
userletters = input("Enter 12 unique letters separated by spaces, starting with the top left letter and continuing clockwise: ").split()
if len(userletters) != 12 or len(set(userletters)) != 12:
        print("Please enter exactly 12 unique letters.")
    
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


