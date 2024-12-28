def sortable_by_trouble_sort(arr: list):
    even = arr[0::2]
    odd = arr[1::2]

    even.sort()
    odd.sort()

    res = []
    for i in range(len(arr)):
        if i % 2 == 0:
            res.append(even[i//2])
        else:
            res.append(odd[i//2])

    sorted = True
    for i in range(len(arr) - 1):
        if res[i] > res[i+1]:
            sorted = False
            break

    return sorted


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    if sortable_by_trouble_sort(arr):
        print("OK")
    else:
        print("-1")
