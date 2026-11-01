from pathlib import Path

path = Path("data/input.txt")
path.write_text("Привет", encoding="cp1251")
print('Тут',path.resolve())
