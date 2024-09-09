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
userletters = input("Enter 12 unique letters separated by spaces: ").split()
if len(userletters) != 12 or len(set(userletters)) != 12:
    print("Please enter exactly 12 unique letters.")
    

userset = set(userletters)
badletters = alphabet-userset
print(badletters)
wordlist = [word for word in wordlist if not badletters.intersection(set(word))]
print(len(wordlist))
print(wordlist[0:100])


