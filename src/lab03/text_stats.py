import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
lib_path = project_root / "src" / "lib"
sys.path.append(str(lib_path))
from text import normalize
from text import tokenize
from text import count_freq
from text import top_n
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