import json
import csv
from pathlib import Path
def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """    
    js_path = Path(json_path)
    c_path = Path(csv_path)
    if js_path.suffix != ".json":
        raise ValueError("Некорректное расширение json-файла")
    if c_path.suffix != ".csv":
        raise ValueError("Некорректное расширение csv-файла")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"Файл {json_path} пуст или содержит битый json")
    except FileNotFoundError:
        raise ValueError(f"Файл {json_path} не найден")
    if not data:
        raise ValueError(f"JSON пуст")
    if isinstance(data, dict):
        data = [data]
    fieldnames = data[0].keys()
    with open(csv_path, 'w', encoding='utf-8', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    js_path = Path(json_path)
    c_path = Path(csv_path)
    if js_path.suffix != ".json":
        raise ValueError("Некорректное расширение json-файла")
    if c_path.suffix != ".csv":
        raise ValueError("Некорректное расширение csv-файла")
    if not Path.is_file(csv_path):
            raise FileNotFoundError("Файл не найден")
    if not Path.is_file(json_path):
            raise FileNotFoundError("Файл не найден")
    with open(csv_path, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("Пустой заголовок")
        data = list(reader)
        if not data:
            raise ValueError("Пустой CSV файл")
    with open(json_path, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
