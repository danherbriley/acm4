

if __name__ == '__main__':
    sum = 0
    try:
        while True:
            line = input()
            if not line:
                break

            if line[0] == '|':
                sum += len(line) * 42
            else:
                comma = line.find(",")
                sum += int(line[0:comma]) * max(1, len(line) - comma - 2)

    except Exception:
        pass

    while sum % 10 != 0:
        sum += 1
    print(f"{sum},-")
