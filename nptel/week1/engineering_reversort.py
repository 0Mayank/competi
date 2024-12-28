from reversort import reversort


def construct(N, C, M):
    # Construct an array with elements from M..N
    # which, when reversorted, incures a cost of C.
    # Precondition: C is an attanaible cost.

    if N == 1:
        return [M]
    elif C - 1 >= N - 2 and C - 1 <= (N * (N - 1) / 2) - 1:
        # if array of size N - 1 can be constructed with cost C - 1,
        # construct that array and add min to start, to get array of
        # size N and const C.
        return [M] + construct(N - 1, C - 1, M + 1)
    else:
        # if C is not in that range, it must be in range,
        # [N * (N - 1) / 2 + 1, N * (N + 1) / 2 - 1]. So, we have
        # to cut cost so that cost of the sub array - 1 lies in above range
        delta = int(C - N * (N - 1) / 2 + 1)
        arr = [M] + construct(N - 1, C - delta, M + 1)

        # can atmost add N cost, which is also max delta can be
        # reversing first delta elements adds delta cost
        return arr[:delta][::-1] + arr[delta:]


if __name__ == "__main__":
    T = int(input())
    for case in range(1, T + 1):
        N, C = list(map(int, input().split()))

        if C < N - 1 or C > N * (N + 1) / 2 - 1:
            print(f"Case #{case}: IMPOSSIBLE")
        else:
            A = construct(N, C, 1)
            print(f"Case #{case}: {reversort(A)}")
