# Лабораторная работа №2
## Задание №1
1) Назначаем  внутри фунции переменные и сравниваем их значения со значениями элементов списка
2) Удаляем дубликаты с помощью множества. Проходим по элементам полученного списка, если текущий элемент больше следующего, меняем их местами. Таким образом список будет отсортирован.
3) Создаём новый список, прибавляем к нему списки внутри данного.
```python
def min_max(nums: list[float | int]) -> tuple[float | int,float | int]:
    if not nums:
        raise ValueError("Пустой список")
    max_nums = min_nums = nums[0]
    for list_element in nums[1:]:
        if min_nums > list_element:
            min_nums = list_element
        if max_nums < list_element:
            max_nums = list_element
    return min_nums, max_nums

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = list(set(nums))
    len_list = len(unique_nums)
    for i in range(len_list-1):
        swap = False
        for j in range(len_list - 1 - i):
            if unique_nums[j] > unique_nums[j+1]:
                unique_nums[j], unique_nums[j+1] = unique_nums[j+1], unique_nums[j]
                swap = True
        if not swap:
            break
    return unique_nums

def flatten(mat: list[list | tuple]) -> list:
    res_lst = []
    for i in mat:
        if type(i) != list and type(i) != tuple:
            raise TypeError('строка не строка строк матрицы')
        res_lst += i
    return res_lst
```
![Результат min_max](/images/lab02/01_1.png)

![Результат unique_sorted](/images/lab02/01_2.png)

![Результат flatten](/images/lab02/01_3.png)
## Задание №2
0) Создадим отдельную функцию is_rectangle для проверки матриц на прямоугольность.
1) Для транспонирования создаем новую матрицу, строки исходной матрицы становятся её столбцами.
2) Для подсчёта сумм строк создаём список, в который отправляем сумму элементов каждого списка внутри исходного.
3) Для подсчёта сумм столбцов также создаём новый список, имеющий длину, равную количеству столбцов, и в соответствующие ячейки записываем значения сумм j-ых элементов строки.
```python
def is_rectangle(matrix):
    ln_str = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != ln_str:
            return False
    return True
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not is_rectangle(mat):
        raise ValueError("Рваная матрица")
    new_mat = [[0 for i in range(len(mat))] for y in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            new_mat[j][i] = mat[i][j]
    return new_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not is_rectangle(mat):
            raise ValueError("Рваная матрица")
    sums = []
    for i in mat:
        sums.append(sum(i))
    return sums

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not is_rectangle(mat):
                raise ValueError("Рваная матрица")
    sums = [0 for i in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
             sums[j] += mat[i][j]
    return sums
```
![Результат transpose](/images/lab02/02_1.png)
![Результат row_sums](/images/lab02/02_2.png)
![Результат col_sums](/images/lab02/02_3.png)
## Задание №3
Распаковываем кортеж в переменные fio, group, gpa, а затем преобразовываем каждую из них согласно заданию.
```python
def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3:
        raise ValueError("Нужно ввести 3 данных")
    fio, group, gpa = rec
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("gpa должен быть в диапазоне от 0.0 до 5.0")
    words = fio.strip().split()
    if len(words) > 2:
        norm_fio = words[0].capitalize() + ' ' + '.'.join(name.upper()[0] for name in words[1:]) + '.'
    else:
        norm_fio = words[0].capitalize() + ' ' + words[1].upper()[0] + '.'
    group = group.strip()
    norm_gpa = f'{gpa:.2f}'
    return f'{norm_fio}, гр. {group}, GPA {norm_gpa}'
```
![Вывод функции format_record](/images\lab02\03.png)

