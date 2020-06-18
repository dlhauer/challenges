def powerfulIntegers(x, y, bound):
    i = 0
    x_set = set()
    if x == 1:
        x_set.add(1)
    else:
        while x**i < bound:
            x_set.add(x**i)
            i += 1
    j = 0
    y_set = set()
    if y == 1:
        y_set.add(1)
    else:
        while y**j < bound:
            y_set.add(y**j)
            j += 1
    res = set()
    for x_pow in x_set:
        for y_pow in y_set:
            if x_pow+y_pow <= bound:
                res.add(x_pow+y_pow)
    
    return list(res)

print(powerfulIntegers(2,1,10))
