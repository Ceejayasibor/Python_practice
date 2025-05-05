def add_all(t):
    total = 0
    for i in t:
        if isinstance(i, list):
            total += add_all(i)
        else:
            total += i
    return total

t = [1, 2, [8, 36, 21], 33, [3,65,35]]
print(add_all(t))
