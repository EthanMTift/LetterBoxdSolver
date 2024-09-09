from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=False, alpha=True)
wordlist = list(web2lowerset)
print(wordlist[0:100])
print(len(wordlist))

