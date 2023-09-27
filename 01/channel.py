
def determine_result(n: int, a: int, q: int, line: str):
    is_possible = (a + line.count("+") >= n)
    is_guaranteed = False
    if a >= n:
        is_guaranteed = True
    elif is_possible:
        plus_count = 0
        minus_count = 0
        for notif in line:
            if notif == "+":
                plus_count += 1
            elif notif == "-":
                minus_count += 1
            else:
                print("CMON MAN")

            if a + plus_count - minus_count >= n:
                is_guaranteed = True
                break

    if not is_possible:
        print("NO")
    elif is_possible and not is_guaranteed:
        print("MAYBE")
    elif is_possible and is_guaranteed:
        print("YES")
    else:
        print("WHAT")


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        n, a, q = [int(x) for x in input().split()]
        line = input()
        determine_result(n, a, q, line)
