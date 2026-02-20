class Solution:
    def pancakeSort(self, arr):
        res = []
        n = len(arr)

        for size in range(n, 1, -1):
            idx = arr.index(size)

            if idx == size - 1:
                continue

            if idx != 0:
                res.append(idx + 1)
                arr[:idx + 1] = reversed(arr[:idx + 1])

            res.append(size)
            arr[:size] = reversed(arr[:size])

        return res