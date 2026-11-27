def bubble_sort(nums):
    new_nums = nums[:]
    len_list = len(new_nums)
    for i in range(len_list-1):
        swap = False
        for j in range(len_list - 1 - i):
            if new_nums[j] > new_nums[j+1]:
                new_nums[j], new_nums[j+1] = new_nums[j+1], new_nums[j]
                swap = True
        if not swap:
            break
    return new_nums

def insertion_sort(nums):
    n = len(nums)
    new_nums = nums[:]
    for i in range(1, n):
        key = new_nums[i]
        j = i - 1
        while j >= 0 and new_nums[j] > key:
            new_nums[j + 1] = new_nums[j]
            j -= 1
        new_nums[j + 1] = key
    return new_nums

def selection_sort(nums):
    new_nums = nums[:]
    n = len(new_nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if new_nums[j] < new_nums[min_idx]:
                min_idx = j
        new_nums[i], new_nums[min_idx] = new_nums[min_idx], new_nums[i]
    return new_nums
