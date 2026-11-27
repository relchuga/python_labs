import csv
import timeit
from src.lab04.io_txt_csv import write_csv
import random
from src.lab07.sorting import bubble_sort, selection_sort, insertion_sort
from src.lab07.search import binary_search, linear_search, two_sum_fast, two_sum_brute

def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]
 
def generate_nums(n):
    random.seed(42)
    nums = [[random.randint(-100,100)] for _ in range(n)]
    write_csv(nums, f"data/samples/lab07/numbers_{n}.csv", header=('value',))

def bench_sorts(n):
    data = read_numbers(f"data/samples/lab07/numbers_{n}.csv")
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", t))
    # TODO: то же для своих сортировок на ТЕХ ЖЕ data; на 10**5 — с ограничением
    return rows

SORTS = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
}

def bench_sorting(n):
    data = read_numbers(f"data/samples/lab07/numbers_{n}.csv")
    rows = []
    for name, fn in SORTS.items():
        t = timeit.timeit(lambda: fn(data), number=1)
        rows.append(("sort", n, name, t))
    return rows

SEARCH = {
    "binary": binary_search,
    "linear": linear_search,
}

def bench_search(n):
    data = read_numbers(f"data/samples/lab07/numbers_{n}.csv")
    rows = []
    for name, fn in SEARCH.items():
        target = random.choice(data)
        t = timeit.timeit(lambda: fn(data, target), number=1)
        rows.append(("search", n, name, t))
    return rows

TWO_SUM = {
    "two_sum_brute": two_sum_brute,
    "two_sum_fast": two_sum_fast
}

def bench_two_sum(n):
    data = read_numbers(f"data/samples/lab07/numbers_{n}.csv")
    rows = []
    for name, fn in TWO_SUM.items():
        target_first, target_second = random.sample(data, 2)
        target = target_first + target_second
        t = timeit.timeit(lambda: fn(data, target), number=1)
        rows.append(("two_sum", n, name, t))
    return rows

NS = [1000, 10_000, 100_000]

def print_table(rows, header=("task", "n", "impl", "seconds")):
    table = [list(header)] + [[str(c) for c in r] for r in rows]
    widths = [max(len(row[i]) for row in table) for i in range(len(header))]
    for i, row in enumerate(table):
        cells = [f"{cell:<{w}}" for cell, w in zip(row, widths[:-1])]
        cells.append(f"{row[-1]:<{widths[-1]}}")
        print(" | ".join(cells))
        if i == 0:
            print(" | ".join("-" * w for w in widths))

def main():
    rows = []
    for n in NS:
        rows += bench_sorts(n)
        if n <= 10_000:
            rows += bench_sorting(n)
            rows += bench_two_sum(n)
        else:
            # O(n^2) на 100000 не гоняем — по образцу это "> 60"
            for name in SORTS:
                rows.append(("sort", n, name, "> 60"))
        rows += bench_search(n)

    write_csv(rows, "src/lab07/bench.csv",
              header=("task", "n", "impl", "seconds"))
    print_table(rows)

main()