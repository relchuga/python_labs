from src.lib.text import *
def text_stats(textos: str) -> str:
    tokens = tokenize(textos)
    total = len(tokens)
    freqs = count_freq(tokens)
    unique = len(freqs)
    tierlist = top_n(freqs, 5)
    print(f'Всего слов: {total}')
    print(f'Уникальных слов: {unique}')
    print('Топ-5:')
    for word, frequency in tierlist:
        print(f'{word}: {frequency}')