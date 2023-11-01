import time


def get_best_leg(start_leg: int, start_pos: int, end_pos: int):
    distance = abs(end_pos - start_pos)
    if start_leg > distance:
        time.sleep(10)
        return -1
    elif start_leg == distance:
        return start_leg
    else:
        best = (100_000, 100_000_000)
        for i in range(start_leg, distance):
            if distance % i == 0:
                if i + distance / i < best[0] + best[1]:
                    best = (i, distance / i)
        if best[1] == 100_000_000:
            time.sleep(10)
        return best[0]


def solve(dest_x: int, dest_y: int):
    moves = 0
    x = y = 0
    leg = 1

    if abs(dest_x - dest_y) < min(dest_x, dest_y):
        new_leg = get_best_leg(leg, 0, dest_x)
        moves += (new_leg - leg)
        leg = new_leg



if __name__ == '__main__':
    for _ in range(int(input())):
        a, b = [int(x) for x in input().split()]
        solve(a, b)
