def is_power_of_2(n):
    return (n & (n - 1)) == 0


if __name__ == "__main__":
    N = int(input())

    if is_power_of_2(N):
        print("TAK")
    else:
        print("NIE")
