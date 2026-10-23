import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
lib_path = project_root / "src" / "lib"
sys.path.append(str(lib_path))
from text import tokenize
from text import count_freq
from text import top_n

textos = sys.stdin.read()
k = 0
total = len(tokenize(textos))
unique = len(count_freq(tokenize(textos)))
tierlist = top_n(tokenize(textos), unique)
print(textos)
print(f'Всего слов: {total}')
print(f'Уникальных слов: {unique}')
print("Топ-5:")
for i in range(unique):
    k += 1
    print(f'{tierlist[i][0]}: {tierlist[i][1]}')
    if k == 5:
        break
