def solve(setv: set, n: int):
    if len(setv) == 1:
        return 0
    if len(setv) == 2:
        return 1
    base = setv.pop()
    results = set()
    for vertex in setv:
        vectorsm: tuple = (vertex[0] - base[0], vertex[1] - base[1])
        vectordt: tuple = (-vectorsm[0], -vectorsm[1])
        for vtx in setv:
            smv = (vtx[0] + vectorsm[0], vtx[1] + vectorsm[1])
            dtv = (vtx[0] + vectordt[0], vtx[1] + vectordt[1])
            if smv not in setv and dtv not in setv:
                break
        else:
            if vectordt not in results and vectorsm not in results:
                results.add(vectorsm)

    return len(results)

        

if __name__ == "__main__":
    n = int(input())
    vertices = set()
    for i in range(n):
        x,y = [int(x) for x in input().split()]
        vertices.add((x,y))
    print(solve(vertices, n) * 2)