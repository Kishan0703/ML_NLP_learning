import nltk
from string import punctuation
nltk.download('punkt_tab')

from nltk import sent_tokenize,word_tokenize,wordpunct_tokenize

corpus="Artificial Intelligence (AI) is transforming industries! From healthcare to finance, AI is helping automate processes, improve decision-making, and create innovative products. But, it also raises ethical concerns—such as job displacement and data privacy."

sent=sent_tokenize(corpus)
words=word_tokenize(corpus)
wordswithoutpun=wordpunct_tokenize(corpus)

print("Sentences: ")
for i in sent:
    print(i)

print("Words:")
for i in words:
    print(i)

total=0
for i in wordswithoutpun:
    if i not in punctuation:
        total+=1

print(f"Total num of words is {total}")
