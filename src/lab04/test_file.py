#from src.lab04.io_txt_csv import read_text, write_csv
#from src.lib.text import normalize
#txt = read_text("data/lab04/input.txt")  # должен вернуть строку
#print(normalize(txt))
#write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV
#print('Файл data/check.csv создан, ура!')
from pathlib import Path

p = Path("data/lab04/input.txt")
p.write_text("Привет", encoding="cp1251")
print(p.resolve())          # реальный путь файла
print(p.stat().st_size)     # размер: для «Привет» в cp1251 должно быть 6
