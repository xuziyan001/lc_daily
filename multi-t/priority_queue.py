class Item:
    def __init__(self, score, member):
        self.score = score
        self.member = member


class PriorQueue:

    def __init__(self):
      self.l = []

    def pop(self):
        if len(self.l) == 0:
            return None
        res = self.l[0]
        self.l = self.l[1:]
        return res.member

    def push(self, item):
        # 二分插入
        if len(self.l) == 0:
            self.l.append(item)
        else:
            first = 0
            last = len(self.l)-1
            mid = (first+last) // 2
            while True:
                if mid < len(self.l) - 1 and self.l[mid].score <= item.score <= self.l[mid+1].score:
                    self.l = self.l[:mid+1] + [item] + self.l[mid+1:]
                    break
                if self.l[mid].score <= item.score:
                    first = mid
                else:
                    last = mid
                mid = (first + last) // 2


def two_sum(nums, target):
    if len(nums) < 2:
        return []
    nums.sort()
    result = []
    for i in range(len(nums)-1):
        result.append(i)
        other = target-nums[i]
        if other <= nums[i]:
            # no answer cause every n>i will get the same result
            return []
        # search other from nums[i+1] to nums[-1] which is a sorted array, binary search
        start = i+1
        end = len(nums)-1
        mid = (start+end) // 2
        while start <= mid <= end:
            if nums[mid] == target:
                result.append(mid)
                return result
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        result = []  # pop if no "other" found


def two_sum(nums, target):
    m = dict()
    for index, each in enumerate(nums):
        m[each] = index
    for k in m.keys():
        if target / 2 == k:
            continue
        if target-k in m:
            return [m[k], m[target-k]]