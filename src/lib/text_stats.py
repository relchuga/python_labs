from src.lib.text import *
def text_stats(textos: str, top: int = 5) -> None:
    top = abs(top)
    tokens = tokenize(textos)
    total = len(tokens)
    freqs = count_freq(tokens)
    unique = len(freqs)
    tierlist = top_n(freqs, top)
    lines = [(f'Всего слов: {total}'),
    (f'Уникальных слов: {unique}'),
    (f'Топ-{top}:')]
    for word, frequency in tierlist:
        lines.append(f'{word}: {frequency}')
    return '\n'.join(lines)
