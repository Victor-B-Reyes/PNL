from urllib import request
import nltk
url = "https://www.gutenberg.org/cache/epub/44173/pg44173.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

# Busqueda de palabras y correlacion de oraciones
text.concordance("albedrío")

# busqueda cerca de la palabra
text.similar("realidad")

text.collocations()

fdist1 = nltk.FreqDist(text)
fdist1.hapaxes()[:50]

text.generate()
