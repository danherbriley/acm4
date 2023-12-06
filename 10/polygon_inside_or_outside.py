
def get_x_intersect(cord1: tuple, cord2: tuple, y: int):
    if cord1[1] == cord2[1]:
        return cord1[1] == y
    
    if min(cord1[1], cord2[1]) < y <= max(cord1[1], cord2[1]):
        dist_y = cord2[1] - cord1[1]
        dist_x = cord2[0] - cord1[0]
        return cord1[0] + (y - cord1[1]) * dist_x / dist_y

    return False

def inside_or_outside(cords: list, qx: int, qy: int):
    is_inside = False
    intersections = 0

    last_x_intersection = -1000000000000000
    for idx in range(len(cords)):
        x_intersect = get_x_intersect(cords[idx], cords[idx - 1], qy)
        if x_intersect is True:
            is_inside = True
            break
        elif x_intersect is not False:
            if x_intersect >= qx:
                if x_intersect == qx and last_x_intersection == qx:
                    continue
                intersections += 1
                last_x_intersection = qx
    else:
        is_inside = (intersections % 2 == 1)

    if is_inside:
        print("D")
    else:
        print("F")


if __name__ == '__main__':
    n, q = [int(x) for x in input().split()]
    cords = []
    tmp = 0
    for idx, str_val in enumerate(input().split()):
        if idx % 2 == 0:
            tmp = int(str_val)
        else:
            cords.append((tmp, int(str_val)))
    
    for _ in range(q):
        qx, qy = [int(x) for x in input().split()]
        inside_or_outside(cords, qx, qy)
