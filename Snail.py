def snail(array):
    size = len(array)
    arr = []
    y, x, dy, dx = 0, -1, 0, 1
    def ok(y, x):
        return y<size and x<size and y>=0 and x>=0 and array[y][x]!=[]
    if not array[0]:
        return arr
    while 1:
        if ok(y+dy, x+dx):
            y += dy
            x += dx
            arr.append(array[y][x])
            array[y][x] = []
        else:
            dx, dy = dy*(2*dx-1), dx
            if not ok(y+dy, x+dx):
                break
    return arr
