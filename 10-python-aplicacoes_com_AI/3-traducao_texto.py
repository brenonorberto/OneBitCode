from deep_translator import GoogleTranslator

# 1 - Idiomas disponíveis
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
# print(langs_dict)

# 2 - Tradução de texto Portugues para Inglês
text = 'Estamos estudando processamento de linguagem natural'
translate = GoogleTranslator(
    source='pt', target='en'
).translate(text)
print(translate)

# 3 - Tradução em itens de uma lista
texts = [
    'Estamos estudando processamento de linguagem natural',
    'Estou aprendendo automação com python',
    'Estou gostando muito'
]
translate_itens = GoogleTranslator(
    source='pt', target='en'
).translate_batch(texts)
print(translate_itens)