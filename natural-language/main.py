import nltk

TEXT = '''
These are the words you will most commonly hear upon entering the 
Natural Language Processing (NLP) space, but there are many more that 
we will be covering in time. With that, let's show an example of 
how one might actually tokenize something into tokens with the NLTK module.
'''

TEXT = TEXT.replace("\n", "")
sentences = nltk.tokenize.sent_tokenize(TEXT)

print(*sentences, sep="\n\n")