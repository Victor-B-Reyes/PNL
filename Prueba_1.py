from urllib import request
import nltk
url = "https://www.gutenberg.org/cache/epub/44173/pg44173.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

text.concordance("albedrío") #Busqueda de palabras y correlacion de oraciones
text.similar("realidad") # busqueda cerca de la palabra
#text.collocations()
#fdist1 = nltk.FreqDist(text)
#fdist1.hapaxes()[:50]
#text.dispersion_plot(["albedrío", "realidad", "libertad"])
text.generate()