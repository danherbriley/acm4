def check(string, n, k, i):
    char = string[i]
    i += k
    while i < n:
        if string[i] != char and string[i] != "?":
            if char == "?":
                char = string[i]
            else:
                return False
        i += k
    return char


def bitstring(n, k, string):
    counts = {"1": 0, "0": 0, "?": 0}
    for i in range(k):
        char = check(string, n, k, i)
        if char:
            counts[char] += 1
        else:
            print("NO")
            return
    if (
        counts["1"] > counts["0"] + counts["?"]
        or counts["0"] > counts["1"] + counts["?"]
    ):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = [int(x) for x in input().split()]
        string = input()
        bitstring(n, k, string)
