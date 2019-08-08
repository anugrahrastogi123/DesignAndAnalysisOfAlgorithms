def binarysearch(arr, element):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    return -1


arr = [int(x) for x in input().split()]
index = binarysearch(arr, 2)
print(index)
