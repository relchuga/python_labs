# Лабораторная работа №4
## Задание A
Функция read_text
```python
from pathlib import Path
from src.lib.text import normalize
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    """FileNotFoundError - файл не найден
    UnicodeDecodeError - неверная кодировка
    Пример с другой кодировкой - encoding='cp1251'"""
    return normalize(p.read_text(encoding=encoding))
```
Функция write_csv
```python
import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```
Генерация отчета: функции frequencies_from_text и sorted_word_counts
```python
from collections import Counter

def frequencies_from_text(text: str) -> dict[str, int]:
    from src.lib.text import normalize, tokenize  # из ЛР3
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
```
# Тест-кейсы
## A. Один файл (база)
Вход(```data/lab04/input.txt```):

```Привет, мир! Привет!!!```

Получаем report.csv:
![файл первого тест-кейса](../../images/lab04/test_a_report.png)

Консоль:
![файл первого тест-кейса](../../images/lab04/test_a.png)
## B. Пустой файл

Вход: пустой ```data/input.txt```

Файл report.csv содержит только заголовок:

![файл второго тест-кейса](../../images/lab04/test_b_report.png)

## C. Кодировка cp1251

Вход содержит "Привет" в cp1251

Файл report.csv:

![](../../images/lab04/test_c_report.png)