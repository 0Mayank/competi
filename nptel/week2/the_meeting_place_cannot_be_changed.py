EPSILON = 10e-6


def intersection_range(a1: (int, int), a2: (int, int)):
    if a1[1] < a2[0] or a2[1] < a1[0]:
        return None

    return (max(a1[0], a2[0]), min(a1[1], a2[1]))


def all_ranges_intersect(t: int, pos: list, velocity: list):
    range_ = (0, float('inf'))
    for (p, v) in zip(pos, velocity):
        cur_range = (p - v * t, p + v * t)
        range_ = intersection_range(range_, cur_range)
        if not range_:
            return False

    return True


def all_ranges_intersect_alternate(t: int, pos: list, velocity: list):
    rightmost_left_edge = max(
        [pos[i] - velocity[i] * t for i in range(len(pos))])
    leftmost_right_edge = min(
        [pos[i] + velocity[i] * t for i in range(len(pos))])

    return rightmost_left_edge <= leftmost_right_edge


def min_time_to_meet(pos: list, v: list, precision: int):
    left, right = 0, 1e9

    while (right - left) > precision:
        m = (right + left) / 2
        if all_ranges_intersect_alternate(m, pos, v):
            right = m
        else:
            left = m

    return m


if __name__ == "__main__":
    N = int(input())

    pos = list(map(int, input().split()))
    velocity = list(map(int, input().split()))

    print(round(min_time_to_meet(pos, velocity, EPSILON), 6))
