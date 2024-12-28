class DisjoinSet:
    def __init__(self, num_sets: int):
        num_sets += 1  # 1-based indexing
        # initially sets are invalid
        self._pointers = [0 for i in range(num_sets)]
        # height of all trees are zero
        self._rank = [-1 for _ in range(num_sets)]
        # sizes of individual sets are 1
        self._set_size = [0 for _ in range(num_sets)]
        # The number of sets
        self.num_sets = 0

        # for this problem
        self._set_sum = [0 for i in range(num_sets)]

    def find_set(self, i: int) -> int:
        if self._pointers[i] == i:
            return i

        self._pointers[i] = self.find_set(self._pointers[i])
        return self._pointers[i]

    def is_same_set(self, i: int, j: int) -> bool:
        return self.find_set(i) == self.find_set(j)

    def union_set(self, i: int, j: int):
        if self.is_same_set(i, j):
            return

        x = self.find_set(i)
        y = self.find_set(j)

        # Union by Rank
        if self._rank[x] > self._rank[y]:
            x, y = y, x

        self._pointers[x] = y

        if self._rank[x] == self._rank[y]:
            self._rank[y] += 1

        self._set_size[y] += self._set_size[x]
        self._set_sum[y] += self._set_sum[x]
        self.num_sets -= 1

    def size_of_set(self, i: int) -> int:
        return self._set_size[self.find_set(i)]

    def make_set(self, i: int, x: int):
        self._pointers[i] = i
        self._rank[i] = 0
        self._set_size[i] = 1
        self.num_sets += 1

        self._set_sum[i] = x

    def sum_of_set(self, i: int) -> int:
        return self._set_sum[self.find_set(i)]


if __name__ == "__main__":
    n = int(input())
    # elements of the input array
    arr = [0] + list(map(int, input().split()))
    # reversed sequence
    sequence = list(map(int, input().split()))[::-1]

    state = [0 for _ in range(n+1)]

    dsu = DisjoinSet(n)
    # To track answers, last answer is always zero
    ans = [0]
    current_max = 0

    for x in sequence:
        state[x] = 1
        dsu.make_set(x, arr[x])

        if x - 1 > 0 and state[x-1]:
            dsu.union_set(x - 1, x)
        if x + 1 < n + 1 and state[x+1]:
            dsu.union_set(x, x + 1)

        current_max = max(dsu.sum_of_set(x), current_max)
        ans.append(current_max)

    # the sum of whole array is not required
    ans.pop()
    print(" ".join(map(str, ans[::-1])))
