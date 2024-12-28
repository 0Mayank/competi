
if __name__ == "__main__":
    inp = input().split()
    # S is string with input states, - and +
    S = inp[0]
    # K is the size of oversized pancake flipper
    K = int(inp[1])

    N = len(S)
    obsolete_flips = [0 for _ in range(N)]

    answer = 0

    for j in range(N - K + 1):
        state = S[j]
        obsolete_flips[j] += obsolete_flips[j-1]

        times_flipped = answer - obsolete_flips[j]

        if ((state == "+" and times_flipped % 2 == 1) or
                (state == "-" and times_flipped % 2 == 0)):
            answer += 1
            # mark it as obsolete flip for the out of range pancake
            if j < N - K:
                obsolete_flips[j+K] += 1
            # next K pancake will not have that flip marked as obsolete,
            # so when we calculate the flip it will count extra flip
            # compared to the rest of the pancakes

    for j in range(N - K + 1, N):
        obsolete_flips[j] += obsolete_flips[j-1]
        times_flipped = answer - obsolete_flips[j]
        state = S[j]
        if ((state == "+" and times_flipped % 2 == 1) or
                (state == "-" and times_flipped % 2 == 0)):
            answer = "IMPOSSIBLE"
            break

    print(answer)
