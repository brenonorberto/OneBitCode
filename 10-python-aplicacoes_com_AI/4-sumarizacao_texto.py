from goose3 import Goose
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.tokenizers import Tokenizer

# 1 - Coletando artigo da internet
g = Goose()
url = 'https://olhardigital.com.br/2024/07/11/pro/drex-moeda-digital-pode-servir-para-pagamentos-off-line/'

artigo = g.extract(url)
# print(artigo.cleaned_text)

# 2 - Aplicando Sumarização
parcer = PlaintextParser.from_string(
    artigo.cleaned_text, 
    Tokenizer('portuguese')
)
sumarizador = LuhnSummarizer()
resumo = sumarizador(parcer.document, 2)
for sentenca in resumo:
    print(sentenca)
