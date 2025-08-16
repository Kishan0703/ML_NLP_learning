import nltk



from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
result = lemmatizer.lemmatize("goes", pos='n')
print(result)  # ✅ Now it will actually show the output