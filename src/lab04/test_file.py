from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize
txt = read_text("data/lab04/input.txt")  # должен вернуть строку
print(normalize(txt))
write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV
print('Файл data/check.csv создан, ура!')