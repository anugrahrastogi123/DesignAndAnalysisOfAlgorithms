def linearsearch(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1


arr = [1, 2, 3, 4, 5]
ans = linearsearch(arr, 4)
print(ans)
k = int(input())
