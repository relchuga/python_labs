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

