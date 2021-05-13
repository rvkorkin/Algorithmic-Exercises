from copy import copy


def compute_1d(books):
    return sum(books)

def compute_2d(books):
    books = sorted(books)[::-1]
    price = [[-1] * (books[1]+1) for _ in range(books[0]+1)]
    v = [0] * 3
    for i in range(books[0]+1):
        price[i][0] = i
    for j in range(books[1]+1):
        price[0][j] = j
    for i in range(1, books[0]+1):
        for j in range(1, books[1]+1):
            v[0] = price[i-1][j] + 1
            v[1] = price[i][j-1] + 1
            v[2] = price[i-1][j-1] + 2 * 0.95
            price[i][j] = min(v)
    return price

def compute_3d(books):
    books = sorted(books)[::-1]
    price = [[[-1] * (books[2]+1) for _ in range(books[1]+1)] for _ in range(books[0]+1)]
    v = [0] * 7
    for i in range(books[0]+1):
        for j in range(books[1]+1):
            price[i][j][0] = compute_2d([books[0], books[1]])[i][j]
    for i in range(books[0]+1):
        for k in range(books[2]+1):
            price[i][0][k] = compute_2d([books[0], books[2]])[i][k]
    for j in range(books[1]+1):
        for k in range(books[2]+1):
            price[0][j][k] = compute_2d([books[1], books[2]])[j][k]
    for i in range(1, books[0]+1):
        for j in range(1, books[1]+1):
            for k in range(1, books[2]+1):
                v[0] = price[i-1][j][k] + 1
                v[1] = price[i][j-1][k] + 1
                v[2] = price[i][j][k-1] + 1
                v[3] = price[i-1][j-1][k] + 2 * 0.95
                v[4] = price[i-1][j][k-1] + 2 * 0.95
                v[5] = price[i][j-1][k-1] + 2 * 0.95
                v[6] = price[i-1][j-1][k-1] + 3 * 0.9
                price[i][j][k] = min(v)
    return price

def compute_4d(books):
    books = sorted(books)[::-1]
    price = [[[[-1] * (books[3]+1) for _ in range(books[2]+1)] for _ in range(books[1]+1)] for _ in range(books[0]+1)]
    v = [0] * 15
    for i in range(books[0]+1):
        for j in range(books[1]+1):
            for k in range(books[2]+1):
                price[i][j][k][0] = compute_3d(books[:3])[i][j][k]
    for i in range(books[0]+1):
        for j in range(books[1]+1):
            for l in range(books[3]+1):
                price[i][j][0][l] = compute_3d(books[:2]+[books[3]])[i][j][l]
    for i in range(books[0]+1):
        for k in range(books[2]+1):
            for l in range(books[3]+1):
                price[i][0][k][l] = compute_3d([books[0]] + books[2:])[i][k][l]
    for j in range(books[1]+1):
        for k in range(books[2]+1):
            for l in range(books[3]+1):
                price[0][j][k][l] = compute_3d(books[1:])[j][k][l]
    for i in range(1, books[0]+1):
        for j in range(1, books[1]+1):
            for k in range(1, books[2]+1):
                for l in range(1, books[3]+1):
                    v[0] = price[i-1][j][k][l] + 1
                    v[1] = price[i][j-1][k][l] + 1
                    v[2] = price[i][j][k-1][l] + 1
                    v[3] = price[i][j][k][l-1] + 1
                    v[4] = price[i-1][j-1][k][l] + 2 * 0.95
                    v[5] = price[i-1][j][k-1][l] + 2 * 0.95
                    v[6] = price[i-1][j][k][l-1] + 2 * 0.95
                    v[7] = price[i][j-1][k-1][l] + 2 * 0.95
                    v[8] = price[i][j-1][k][l-1] + 2 * 0.95
                    v[9] = price[i][j][k-1][l-1] + 2 * 0.95
                    v[10] = price[i-1][j-1][k-1][l] + 3 * 0.9
                    v[11] = price[i-1][j-1][k][l-1] + 3 * 0.9
                    v[12] = price[i-1][j][k-1][l-1] + 3 * 0.9
                    v[13] = price[i][j-1][k-1][l-1] + 3 * 0.9
                    v[14] = price[i-1][j-1][k-1][l-1] + 4 * 0.8
                    price[i][j][k][l] = min(v)
    return price

def compute_5d(books):
    books = sorted(books)[::-1]
    price = [[[[[-1] * (books[4]+1) for _ in range(books[3]+1)] for _ in range(books[2]+1)] for _ in range(books[1]+1)] for _ in range(books[0]+1)]
    v = [0] * 31
    for i in range(books[0]+1):
        for j in range(books[1]+1):
            for k in range(books[2]+1):
                for l in range(books[3]+1):
                    price[i][j][k][l][0] = compute_4d(books[:4])[i][j][k][l]
    for i in range(books[0]+1):
        for j in range(books[1]+1):
            for k in range(books[2]+1):
                for m in range(books[4]+1):
                    price[i][j][k][0][m] = compute_4d(books[:3]+[books[4]])[i][j][k][m]
    for i in range(books[0]+1):
        for j in range(books[1]+1):
            for l in range(books[3]+1):
                for m in range(books[4]+1):
                    price[i][j][0][l][m] = compute_4d(books[:2]+books[3:])[i][j][l][m]
    for i in range(books[0]+1):
        for k in range(books[2]+1):
            for l in range(books[3]+1):
                for m in range(books[4]+1):
                    price[i][0][k][l][m] = compute_4d([books[0]]+books[2:])[i][k][l][m]
    for j in range(books[1]+1):
        for k in range(books[2]+1):
            for l in range(books[3]+1):
                for m in range(books[4]+1):
                    price[0][j][k][l][m] = compute_4d(books[1:])[j][k][l][m]
    for i in range(1, books[0]+1):
        for j in range(1, books[1]+1):
            for k in range(1, books[2]+1):
                for l in range(1, books[3]+1):
                    for m in range(1, books[4]+1):
                        v[0] = price[i-1][j][k][l][m] + 1
                        v[1] = price[i][j-1][k][l][m] + 1
                        v[2] = price[i][j][k-1][l][m] + 1
                        v[3] = price[i][j][k][l-1][m] + 1
                        v[4] = price[i][j][k][l][m-1] + 1
                        v[5] = price[i-1][j-1][k][l][m] + 2 * 0.95
                        v[6] = price[i-1][j][k-1][l][m] + 2 * 0.95
                        v[7] = price[i-1][j][k][l-1][m] + 2 * 0.95
                        v[8] = price[i-1][j][k][l][m-1] + 2 * 0.95
                        v[9] = price[i][j-1][k-1][l][m] + 2 * 0.95
                        v[10] = price[i][j-1][k][l-1][m] + 2 * 0.95
                        v[11] = price[i][j-1][k][l][m-1] + 2 * 0.95
                        v[12] = price[i][j][k-1][l-1][m] + 2 * 0.95
                        v[13] = price[i][j][k-1][l][m-1] + 2 * 0.95
                        v[14] = price[i][j][k][l-1][m-1] + 2 * 0.95
                        v[15] = price[i-1][j-1][k-1][l][m] + 3 * 0.9
                        v[16] = price[i-1][j-1][k][l-1][m] + 3 * 0.9
                        v[17] = price[i-1][j-1][k][l][m-1] + 3 * 0.9
                        v[18] = price[i-1][j][k-1][l-1][m] + 3 * 0.9
                        v[19] = price[i-1][j][k-1][l][m-1] + 3 * 0.9
                        v[20] = price[i-1][j][k][l-1][m-1] + 3 * 0.9
                        v[21] = price[i][j-1][k-1][l-1][m] + 3 * 0.9
                        v[22] = price[i][j-1][k-1][l][m-1] + 3 * 0.9
                        v[23] = price[i][j-1][k][l-1][m-1] + 3 * 0.9
                        v[24] = price[i][j][k-1][l-1][m-1] + 3 * 0.9
                        v[25] = price[i-1][j-1][k-1][l-1][m] + 4 * 0.8
                        v[26] = price[i-1][j-1][k-1][l][m-1] + 4 * 0.8
                        v[27] = price[i-1][j-1][k][l-1][m-1] + 4 * 0.8
                        v[28] = price[i-1][j][k-1][l-1][m-1] + 4 * 0.8
                        v[29] = price[i][j-1][k-1][l-1][m-1] + 4 * 0.8
                        v[30] = price[i-1][j-1][k-1][l-1][m-1] + 5 * 0.75
                        price[i][j][k][l][m] = min(v)
    return price

def total(arr):
    if len(arr) == 0:
        return 0
    books = [0] * max(arr)
    for el in arr:
        books[el-1] += 1
    if len(books) == 1:
        return round(compute_1d(books) * 800)
    elif len(books) == 2:
        return round(compute_2d(books)[-1][-1] * 800)
    elif len(books) == 3:
        return round(compute_3d(books)[-1][-1][-1] * 800)
    elif len(books) == 4:
        return round(compute_4d(books)[-1][-1][-1][-1] * 800)
    elif len(books) == 5:
        return round(compute_5d(books)[-1][-1][-1][-1][-1] * 800)
    else:
        return 'error'
