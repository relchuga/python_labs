from pathlib import Path
from src.lib.text import normalize
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    """FileNotFoundError - файл не найден
    UnicodeDecodeError - неверная кодировка
    Пример с другой кодировкой - encoding='cp1251'"""
    return normalize(p.read_text(encoding=encoding))

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
from collections import Counter

def frequencies_from_text(text: str) -> dict[str, int]:
    from lib.text import normalize, tokenize  # из ЛР3
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))