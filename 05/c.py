if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]

    if n > m:
        print(0)
    else:
        product = 1
        for i in range(n):
            for j in range(i + 1, n):
                product = (product * abs(nums[i] - nums[j])) % m
        print(product)
