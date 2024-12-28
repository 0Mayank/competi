class DisjoinSet:
    def __init__(self, num_sets: int):
        num_sets += 1  # 1-based indexing
        # N singleton sets, with everyone as their own parent
        self._pointers = [i for i in range(num_sets)]
        # height of all trees are zero
        self._rank = [0 for _ in range(num_sets)]
        # sizes of individual sets are 1
        self._set_size = [1 for _ in range(num_sets)]
        # The number of sets
        self.num_sets = num_sets - 1

    def find_set(self, i: int) -> int:
        if self._pointers[i] == i:
            return i

        self._pointers[i] = self.find_set(self._pointers[i])
        return self._pointers[i]

    def is_same_set(self, i: int, j: int) -> bool:
        return self.find_set(i) == self.find_set(j)

    def union_set(self, i: int, j: int) -> int:
        if self.is_same_set(i, j):
            return self.find_set(i)

        x = self.find_set(i)
        y = self.find_set(j)

        # Union by Rank
        if self._rank[x] > self._rank[y]:
            x, y = y, x

        self._pointers[x] = y

        if self._rank[x] == self._rank[y]:
            self._rank[y] += 1

        self._set_size[y] += self._set_size[x]
        self.num_sets -= 1

        return y

    def size_of_set(self, i: int) -> int:
        return self._set_size[self.find_set(i)]
