
if __name__ == "__main__":
    N = int(input())  # Number of islands
    P = int(input())  # Number of pairs
    requests = []
    for _ in range(P):
        requests.append(list(map(int, input().split())))

    requests.sort(key=lambda x: x[1])

    ans = 0
    last_bridge_destroyed = -1  # Left point of bridge

    for req in requests:
        if last_bridge_destroyed >= req[0]:
            continue
        ans += 1
        last_bridge_destroyed = req[1] - 1

    print(ans)
