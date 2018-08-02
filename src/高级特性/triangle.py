def triangle(line):
    L = 0
    while L < line:
        myList = [x for x in range(L)]
        L += 1
        yield myList

def makeTriangle(line):
    g = triangle(line)
    while True:
        try:
            x = next(g)
            print(x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break

makeTriangle(7)