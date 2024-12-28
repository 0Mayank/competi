def min_pos(arr, start) -> int:
    minx = arr[start]
    ix = start
    for i in range(start, len(arr)):
        if arr[i] < minx:
            minx = arr[i]
            ix = i

    return ix


def reversort(arr) -> int:
    cost = 0
    for i in range(len(arr) - 1):
        j = min_pos(arr, i)
        arr[i:j+1] = reversed(arr[i:j+1])
        cost += (j - i) + 1

    return cost


if __name__ == "__main__":
    num_test_cases = int(input())
    for test_case in range(num_test_cases):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])

        cost = reversort(arr)

        print(f"Case #{test_case+1}: {cost}")
