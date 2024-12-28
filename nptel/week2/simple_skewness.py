from fractions import Fraction


def cumulative_sums(arr: list) -> list:
    res = [0]

    for v in arr:
        res.append(res[-1] + v)

    return res


def find_mean(cumulative_sums: list, median: int, K: int, N: int):
    sum = (cumulative_sums[median + 1] - cumulative_sums[median - K]
           + cumulative_sums[N] - cumulative_sums[N - K])

    return Fraction(sum, 2 * K + 1)


def solve(arr: list, N: int) -> list:
    arr.sort()
    cum = cumulative_sums(arr)
    answer = 0
    optimal_k = 0
    optimal_median = 0

    for median in range(N):
        # We want to pick K elements to the left of guess
        # and K elements from the end.
        k_range = min(median, N - median - 1)
        L, R = 0, k_range

        while (L < R):
            mid = (L + R) // 2

            # mid is the current k
            # should we increase k?

            K = mid + 1
            a = arr[N - K]
            b = arr[median - K]

            # No, K is an overestimate already
            if a + b / 2 <= (cum[median + 1] - cum[median - K]
                             + cum[N] - cum[N - K]) / (2 * K + 1):
                R = mid
            else:  # Yes, there's more potential for K
                L = mid + 1

        # When L == R, we have found K
        mean = find_mean(cum, median, L, N)
        skewness = mean - arr[median]
        if skewness > answer:
            answer = skewness
            optimal_k = L
            optimal_median = median

    return (arr[optimal_median - optimal_k: optimal_median + 1]
            + arr[N - optimal_k:])


if __name__ == "__main__":
    N = int(input())
    v = list(map(int, input().split()))

    ans = solve(v, N)
    print(len(ans))
    print(" ".join(map(str, ans)))
