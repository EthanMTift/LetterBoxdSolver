from english_words import get_english_words_set
import string
web2lowerset = get_english_words_set(['web2'], lower=False, alpha=True)
wordlist = list(web2lowerset)
wordlist = [word for word in wordlist if not word[0].isupper()]

print(wordlist[0:100])
print(len(wordlist))
wordlist = [word for word in wordlist if len(word) >= 3]
print(wordlist[0:100])
print(len(wordlist))

alphabet = set(string.ascii_lowercase)
userletters = input("Enter 12 unique letters separated by spaces, starting with the top left letter and continuing clockwise: ").split()
if len(userletters) != 12 or len(set(userletters)) != 12:
        print("Please enter exactly 12 unique letters.")
    
groups = [userletters[i:i+3] for i in range(0, len(userletters), 3)]
print(groups)



userset = set(userletters)
badletters = alphabet-userset
print(badletters)
wordlist = [word for word in wordlist if not badletters.intersection(set(word))]
print(len(wordlist))
print(wordlist[0:100])
goodwords = []
for word in wordlist:
        for index, letter in enumerate(word):
                if (index == (len(word)-1)):
                        goodwords.append(word)
                else:
                        if (word[index + 1] == word[index]):
                                break
                        
print(len(goodwords))
print(goodwords[0:100])
pogwords = []
print(groups[1])
for word in goodwords:
        for index, letter in enumerate(word):
                if (index == (len(word)-1)):
                        pogwords.append(word)
                else:
                        if (((word[index] in groups[0]) and (word[index+1] in groups[0])) or ((word[index] in groups[1]) and (word[index+1] in groups[1])) or ((word[index] in groups[2]) and (word[index+1] in groups[2])) or ((word[index] in groups[3]) and (word[index+1] in groups[3]))):
                                break

print(len(pogwords))
print(pogwords[0:100])


