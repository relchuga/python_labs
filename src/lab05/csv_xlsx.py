import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from pathlib import Path
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    c_path = Path(csv_path)
    if c_path.suffix != ".csv":
        raise ValueError(f"Ожидался csv-файл, получен {c_path}")
    if not Path.is_file(csv_path):
        raise FileNotFoundError("Файл не найден")
    if not Path.is_file(xlsx_path):
            raise FileNotFoundError("Файл не найден")
    with open(csv_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader if row]
    if not data:
        raise ValueError("Пустой csv-файл")
    fieldnames = list(reader.fieldnames)
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(fieldnames)
    for row in data:
        ws.append(list(row.values()))
    for col_idx in range(1, len(fieldnames) + 1):
        max_len = len(str(fieldnames[col_idx - 1]))
        for row in data:
            value = str(row[fieldnames[col_idx - 1]])
            max_len = max(max_len, len(value))
        ws.column_dimensions[get_column_letter(col_idx)].width = max(8, max_len + 2)

    wb.save(xlsx_path)
