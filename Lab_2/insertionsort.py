def insertion_sort(arr, n):
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input())
arr = [int(x) for x in input().split()]
insertion_sort(arr, n)
print(*arr)
