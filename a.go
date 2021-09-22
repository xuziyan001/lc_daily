

func sort(l []int,target int) int {
    return sortDivide(l, 0, len(l)-1, target)
}

func sortDivide(l []int, start, end, target int) int {
    if end < start {
        return -1
    }
    mid = (start + end) / 2
    if l[mid] > target {
      end = mid - 1
    } else if l[mid] < target {
      start = mid + 1
    } else {
      return mid
    }
    return sortDivide(l, start, end, target)
}