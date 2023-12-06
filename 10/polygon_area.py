

def calculate_polygon_area(cords: list) -> int:
    x = 0
    for i in range(len(cords) - 1):
        x += (cords[i][0]*cords[i + 1][1] - cords[i + 1][0]*cords[i][1])
    return round(abs(x / 2))

if __name__ == "__main__":
    n = int(input())
    cords = []
    for _ in range(n):
        cords.append([int(x) for x in input().split()])
    
    print(calculate_polygon_area(cords))
