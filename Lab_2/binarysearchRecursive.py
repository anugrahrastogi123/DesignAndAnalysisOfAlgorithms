def binarysearchrecursive(arr, start, end, k):
    if start > end:
        return -1
    mid = (start+end)//2
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return binarysearchrecursive(arr, start, mid-1, k)
    else:
        return binarysearchrecursive(arr, mid+1, end, k)


arr = [int(x) for x in input().split()]
k = int(input())
index = binarysearchrecursive(arr, 0, len(arr)-1, k)
print(index)
