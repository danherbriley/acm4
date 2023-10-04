def balanced(counts):
    return (
        counts["0"] + counts["?"] == counts["1"],
        counts["0"] == counts["1"] + counts["?"],
    )


def count(string, k):
    counts = {"1": 0, "0": 0}
    for i in range(k):
        counts[string[i]] += 1
    return counts["0"] == counts["1"]


def get_versions(string):
    if "?" not in string:
        return [string]
    i = string.find("?")

    return get_versions(string[:i] + "0" + string[i + 1 :]) + get_versions(
        string[:i] + "1" + string[i + 1 :]
    )


def bitstring(n, k, string):
    def rec(i, version):
        if not count(version, k):
            return False
        if i + k > n:
            return True
        version = version[1:] + string[i + k - 1]
        if "?" not in version:
            return rec(i + 1, version)
        else:
            versions = [version[:-1] + "0", version[:-1] + "1"]
            for v in versions:
                if rec(i + 1, v):
                    return True
            return False

    if "?" in string[:k]:
        versions = get_versions(string[:k])
    else:
        return rec(1, string[:k])

    for version in versions:
        if rec(1, version):
            return True

    return False


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = [int(x) for x in input().split()]
        string = input()
        if bitstring(n, k, string):
            print("YES")
        else:
            print("NO")
