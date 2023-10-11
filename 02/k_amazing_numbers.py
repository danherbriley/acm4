

def solve(n):
    num_info = {}  # dict[val, tuple[last_idx, max_blank, blank_to_end]]
    for idx, val in enumerate(input().split()):
        val = int(val)
        if val not in num_info:
            num_info[val] = (idx, idx + 1, n - idx)
        else:
            blank = idx - num_info[val][0]
            num_info[val] = (idx, max(blank, num_info[val][1]), n - idx)

    best_vals = {}
    for val, info in num_info.items():
        k = max(info[1], info[2])
        if k not in best_vals or best_vals[k] > val:
            best_vals[k] = val

    smallest_val = 10_000_000
    for i in range(n):
        best_val = best_vals.get(i + 1, -1)
        if best_val >= smallest_val or (best_val == -1 and smallest_val != 10_000_000):
            best_val = smallest_val
        elif best_val != -1:
            smallest_val = best_val

        if i != n - 1:
            print(best_val, end=" ")
        else:
            print(best_val)


if __name__ == '__main__':
    for _ in range(int(input())):
        nn = int(input())
        solve(nn)
