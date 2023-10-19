from itertools import permutations


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, min(int(x ** 1/2) + 1, x - 1)):
        if x % i == 0:
            return False
    return True


def get_permutations(n):
    return permutations(range(1, n + 1))


def count_primality(n, perm):
    primality = 0
    for i in range(n):
        for j in range(i, n):
            diff = set(range(1, n + 1)).difference(perm[i:j+1])
            # print(diff)
            minimum = min(diff) if diff else n + 1
            if is_prime(minimum):
                primality += 1
    return primality


def solve(n, test_primality = -1):
    best = 0, []
    for permutation in get_permutations(n):
        primality = count_primality(n, permutation)
        if primality > best[0]:
            best = (primality, permutation)
        if primality == test_primality:
            print(f"For {n = }: Primality = {primality}, permutation = {permutation}")
            break

    if test_primality == -1:
        print(f"For {n = }: Primality = {best[0]}, permutation = {best[1]}")


if __name__ == '__main__':
    for _ in range(int(input())):
        nn = int(input())
        x = [-1, 1, 2, 3, 6, 8, 12, 15, 19, 24]
        solve(nn, x[nn])
