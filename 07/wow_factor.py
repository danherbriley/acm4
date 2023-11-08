

def solve(vov_str):
    wow_str = ""
    k = 0
    for char in vov_str:
        if char == "o":
            if k > 1:
                wow_str += (k - 1) * "w"
            k = 0
            wow_str += 'o'
        else:
            k += 1
    if k > 1:
        wow_str += (k - 1) * "w"

    counters = None
    for idx, char in enumerate(wow_str):
        if not counters:
            if char == "w":
                counters = (1, 0, 0)
            else:
                counters = (0, 0, 0)
        else:
            if char == "w":
                counters = (counters[0] + 1,
                            counters[1],
                            counters[1] + counters[2]
                            )
            else:
                counters = (counters[0],
                            counters[1] + counters[0],
                            counters[2]
                            )

    res = counters[2] if counters else 0
    print(res)


if __name__ == '__main__':
    solve(input())
