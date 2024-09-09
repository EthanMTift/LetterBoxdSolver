from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=False, alpha=True)
wordlist = list(web2lowerset)
wordlist = [word for word in wordlist if not word[0].isupper()]

print(wordlist[0:100])
print(len(wordlist))


