from functools import cache


def manhatten_distance(p1: (int, int), p2: (int, int)) -> int:
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def change_in_1_cycle(dir_map, S: list) -> (int, int):

    @cache
    def change(S: list):
        x, y = 0, 0
        for dir in S:
            change = dir_map[dir]
            x += change[0]
            y += change[1]
        return (x, y)

    return change(S)


def change_in_k_days(k, dir_map, S: list) -> (int, int):
    dx, dy = change_in_1_cycle(dir_map, S)
    dx *= k // len(S)
    dy *= k // len(S)

    k = k % len(S)

    for dir in S[:k]:
        change = dir_map[dir]
        dx += change[0]
        dy += change[1]

    return (dx, dy)


def calculate_final_pos(k: int, x1: int, y1: int, dir_map, S: list) -> int:
    dx, dy = change_in_k_days(k, dir_map, S)
    return (x1 + dx, y1 + dy)


def search_min_k(x1: int, y1: int, x2: int, y2: int, dir_map, S: list) -> int:
    maxk = manhatten_distance((x1, y1), (x2, y2))
    left, right = 0, maxk + 1

    while left < right:
        k = (left + right) // 2
        x3, y3 = calculate_final_pos(k, x1, y1, dir_map, S)
        if manhatten_distance((x3, y3), (x2, y2)) <= k:
            right = k
        else:
            left = k + 1

    if left >= maxk + 1:
        return -1
    else:
        return right


if __name__ == "__main__":
    dir_map = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0),
               'R': (0, 1), 'N': (0, 0)}
    # Start
    x1, y1 = list(map(int, input().split()))
    # Destination
    x2, y2 = list(map(int, input().split()))

    # Length of weather forecast
    n = int(input())

    # Weather forecast
    S = input()

    print(search_min_k(x1, y1, x2, y2, dir_map, S))
