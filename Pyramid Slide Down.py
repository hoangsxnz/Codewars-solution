def longest_slide_down(pyramid):
    T = [[0 for j in range(len(pyramid[i]))] for i in range(len(pyramid))]
    T[0][0] = pyramid[0][0]
    for i in range(1, len(pyramid)):
        for j in range(len(pyramid[i])):
            if j > 0 and j < len(pyramid[i])-1:
                T[i][j] = max(T[i][j], T[i-1][j] + pyramid[i][j], T[i-1][j-1] + pyramid[i][j])
            elif j == 0:
                T[i][j] = max(T[i][j], T[i-1][j] + pyramid[i][j])
            elif  j == len(pyramid[i])-1:
                T[i][j] = max(T[i][j], T[i-1][j-1] + pyramid[i][j])
    return max(T[len(pyramid)-1])
