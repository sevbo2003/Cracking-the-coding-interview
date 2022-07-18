class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            n = n & (n - 1)
            count += 1

        return count

    def solution2(self, n):
        n_bin = str(bin(n))[2:]  # Converting int to binary

        counter = 0
        for i in n_bin:
            if i == "1":
                counter += 1

        return counter
