import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Конвертация JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Путь до входного файла")
    p1.add_argument("--out", dest="output", required=True, help="Путь до выходного файла")

    p2 = sub.add_parser("csv2json", help="Конвертация CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Путь до входного файла")
    p2.add_argument("--out", dest="output", required=True, help="Путь до выходного файла")

    p3 = sub.add_parser("csv2xlsx", help="Конвертация CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Путь до входного файла")
    p3.add_argument("--out", dest="output", required=True, help="Путь до выходного файла")

    args = parser.parse_args()

    if args.cmd == 'json2csv':
        json_to_csv(args.input, args.output)
    elif args.cmd == 'csv2json':
        csv_to_json(args.input, args.output)
    elif args.cmd == 'csv2xlsx':
        csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()
