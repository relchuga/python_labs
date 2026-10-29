import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
textos = sys.stdin.read()
k = 0
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