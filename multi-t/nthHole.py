

def nthHole(nums, n):
    if len(nums) < 2:
        return None
    l = len(nums)
    last = l-1
    next = l-2
    # last-next+1 represents how many holes
    while (nums[last] - nums[next] - 1) < n:
        n -= (nums[last]-nums[next]-1)
        last -= 1
        next -= 1
    return nums[last] - n


if __name__ == '__main__':
    nums = [2,3,4,6,9]
    n = 3
    print(nthHole(nums, n))  # 5
    nums = [2, 8]  # 3
    n = 5
    print(nthHole(nums, n))
    nums = [2, 9]
    n = 11
    print(nthHole(nums, n))
    nums = [2, 3, 4, 6, 9]
    n = 3
    print(nthHole(nums, n))
