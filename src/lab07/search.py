def linear_search(nums, x) -> int:
    """Индекс первого вхождения x или -1.
 
    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    linear_search([], 1) -> -1
    """
    for index in range(len(nums)):
        if nums[index] == x:
            return index
    return -1

def binary_search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            summ = nums[i] + nums[j]
            if summ == target:
                return i, j

def two_sum_fast(nums, target) -> tuple[int, int] | None:
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i

