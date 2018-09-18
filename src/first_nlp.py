# First NLP Program
import nltk
from nltk.corpus import treebank
nltk.download('treebank')

# sets sentence and sends it to a token, then prints
sentence = "This is my first program using nltk. Should I do hello world?"
tokens = nltk.word_tokenize(sentence)
print(tokens)

# tags the token and prints them
tag_one = nltk.pos_tag(tokens)
print(tag_one)

# sets an entity to the tag and prints is
entities = nltk.chunk.ne_chunk(tag_one)
print(entities)

# ?
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
