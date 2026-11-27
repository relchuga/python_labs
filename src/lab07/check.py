import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
 
 
def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
 
def check_search(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = sorted([random.randint(-100, 100) for _ in range(n)])
        if not nums:
            continue
        x = random.choice(nums)
        original = list(nums)
        result = fn(nums, x)
        assert original[result] == original[original.index(x)], \
            f"{fn.__name__} ошиблась на {original}: {result}, элемент:{x}, ожидалось:{original.index(x)}"

def check_two_sum(trials=100):
    for _ in range(trials):
        n = random.randint(2, 50)
        original = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-200, 200)
        result_brute = two_sum_brute(original, x)
        result_fast = two_sum_fast(original, x)
        if result_fast and result_brute:
            assert sum([original[i] for i in result_brute]) == sum([original[i] for i in result_fast]) == x, f"Одна из функций ошиблась:\nbrute: {result_brute}\nfast:{result_fast}\n data: {original}, {x}"
        else:
            assert result_brute == result_fast == None
        
if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    for fn in (linear_search, binary_search):
        check_search(fn)
    check_two_sum()
    print("OK")
