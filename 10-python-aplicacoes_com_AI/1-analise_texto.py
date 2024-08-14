import os
import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# nltk.download('punkt')

# 1 - Importação do texto
with open(os.path.join( 'data', 'texto.txt'), 'r', encoding='utf-8') as file:
    texto = file.read()
    print(texto)
    

# 2 - Tokenizando o texto
send_tokens = sent_tokenize(texto)
print(send_tokens)
print(len(send_tokens))

word_tokens = word_tokenize(texto)
print(word_tokens)
print(len(word_tokens))

# 3 - Frequência de distribuição
fdist = FreqDist(word_tokens)
# print(fdist)
print(fdist.most_common(10))
fdist.plot(10)

# 4 - WordCloud / WordCloud customizado
def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    
wordcloud = WordCloud(
    width=3000, 
    height=2000, 
    random_state=1, 
    background_color='salmon', 
    colormap='Pastel1', 
    collocations=False, 
    stopwords=STOPWORDS
).generate(texto)

# plot_cloud(wordcloud)

mascara = np.array(Image.open('data/upvote.png'))
# print(mascara)
wordcloud = WordCloud(
    width=3000, 
    height=2000, 
    random_state=1, 
    background_color='salmon', 
    colormap='Pastel1', 
    collocations=False, 
    stopwords=STOPWORDS,
    mask=mascara
).generate(texto)

plot_cloud(wordcloud)