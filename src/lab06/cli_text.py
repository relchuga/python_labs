import argparse
from src.lib.text_stats import *
from pathlib import Path
def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла построчно")
    cat_parser.add_argument("--input", type=str, required=True, help="Путь до входного файла")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Статистика по частотам файла")
    stats_parser.add_argument("--input", type=str, required=True, help="Путь до входного файла")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество слов в топе")

    args = parser.parse_args()

    try:
        if args.command == "cat":
            k = 0
            with open(args.input, 'r', encoding='utf-8') as f:
                for line in f:
                    k+=1
                    string = line.strip('\n')
                    if args.n == True:
                        print(f'{k}. {string}')
                    else:
                        print(line)
        elif args.command == "stats":
            data = ''
            with open(args.input, 'r', encoding='utf-8') as  f:
                for line in f:
                    data += line
            print(text_stats(data, args.top))
    except FileNotFoundError:
        print("Файл не найден")

if __name__ == "__main__":
    main()