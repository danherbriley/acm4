

class BitSet:
    value: int

    def __init__(self, value):
        self.value = value

    def add(self, value):
        self.value += value


def determine_result(dominoes: list, idx: int, first: BitSet, second: BitSet) -> bool:
    if idx >= len(dominoes):
        return True

    a, b = dominoes[idx]
    if a == b:
        return False

    # a = a - 1
    # b = b - 1
    a_shifted = (1 << a)
    b_shifted = (1 << b)
    if first.value & a_shifted == a_shifted or first.value & b_shifted == b_shifted:
        if second.value & a_shifted == a_shifted or second.value & b_shifted == b_shifted:
            return False
        second.add(a_shifted + b_shifted)
        return determine_result(dominoes, idx + 1, first, second)
    elif second.value & a_shifted == a_shifted or second.value & b_shifted == b_shifted:
        first.add(a_shifted + b_shifted)
        return determine_result(dominoes, idx + 1, first, second)
    else:
        # a, b both not in first or second sets
        first_value = first.value
        second_value = second.value
        return determine_result(dominoes, idx + 1, BitSet(first_value + a_shifted + b_shifted), second) \
            or determine_result(dominoes, idx + 1, first, BitSet(second_value + a_shifted + b_shifted))


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        dominoes = []
        is_possible = True
        for _ in range(n):
            aa, bb = tuple(int(x) for x in input().split())
            if aa == bb:
                is_possible = False
            dominoes.append((aa, bb))
        if not is_possible:
            print("NO")
            continue

        good_result = determine_result(dominoes, 0,  BitSet(0), BitSet(0))
        if good_result:
            print("YES")
        else:
            print("NO")

