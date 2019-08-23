def selection_sort(arr, n):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


n = int(input())
arr = [int(x) for x in input().split()]
selection_sort(arr, n)
print(*arr)
