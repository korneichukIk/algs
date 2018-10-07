#[ % % % ]                 [ % % ]
#[ % % % ]     [ 1 % ]     [ % % ]
#[ 7 8 9 ]   * [ 3 % ]  =  [ x % ]
#[ % % % ]     [ 5 % ]     [ % % ]
#
# x = 7*1 + 8*3 + 9*5 = 76


def matrix_mult(X, Y):
    result = []
    temp = []

    # main cycle amount of X cols
    for i in range(len(X)):
        # inside cycle #1 amount of Y rows
        for j in range(len(Y[0])):
            sum = 0
            # inside cycle #2 amount of X rows
            for k in range(len(Y)):
                sum += X[i][k] * Y[k][j]
            temp.append(sum)
        result.append(temp)
        temp = []
    return result

X = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
Y = [[1,2],[3,4],[5,6]]

print(matrix_mult(X, Y))
