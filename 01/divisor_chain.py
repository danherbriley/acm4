import math


def find_divisor(n):
    shifts = 0
    while not (n & 1):
        n >>= 1
        if n == 1:
            return 2**shifts
        shifts += 1
    return 2**shifts


def reduce(n, nums):
    if n == 1:
        nums.append(str(n))
        return
    else:
        nums.append(str(n))
        reduce(n - find_divisor(n), nums)
        return


def divisor_chain(n):
    nums = []
    reduce(n, nums)
    print(len(nums))
    for num in nums:
        print(num, end=" ")
    print()


if __name__ == "__main__":
    lines = int(input())
    for i in range(lines):
        divisor_chain(int(input()))
