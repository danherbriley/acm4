def pp(n):
    if n == 1:
        print("1")
        return
    if n == 2:
        print("1 2")
        return

    arr = n * [0]
    arr[(len(arr) - 1) // 2] = 1
    arr[0] = 2
    arr[-1] = 3

    num = 4
    ind = 0
    while True:
        if arr[ind] == 3:
            break
        elif arr[ind]:
            ind += 1
        else:
            arr[ind] = num
            ind += 1
            num += 1

    for num in arr:
        print(num, end=" ")
    print()


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        pp(n)
