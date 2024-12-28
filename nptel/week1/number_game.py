import math

phi = (1 + 5**0.5) / 2

if __name__ == "__main__":
    T = int(input())
    for case in range(1, T+1):
        A1, A2, B1, B2 = list(map(int, input().split()))

        ans = 0

        for b in range(B1, B2+1):
            # all positions which satisfy
            # max(a, b) >= phi * min(a, b) are winning
            # a >= phi * b if a > b
            # b >= phi * a if b > a
            # a <= b / phi
            # a <= (phi - 1) * b
            if A1 > phi * b or A2 <= (phi - 1) * b:
                ans += (A2 - A1 + 1)
            else:
                ans += max(0, A2 - math.floor(phi * b))
                ans += max(0, math.floor((phi - 1) * b) - (A1 - 1))

        print(f"Case #{case}: {ans}")
