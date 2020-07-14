def sequentialDigits(low, high):

    def getStart(length, low=None):
        if not low:
            low = 10**(length-1)
        starts = [int(''.join([str(num) for num in range(i, length+i)])) for i in range(1, 11-length)]
        greater_starts = [start for start in starts if start >= low]
        return greater_starts[0] if greater_starts else starts[-1] if starts else None

    res = []
    length = len(str(low))
    num = getStart(length, low)
    while num <= high:
        if num >= low
            res.append(num)
        if str(num)[-1] == '9':
            length += 1
            num = getStart(length)
            if not num:
                break
            continue
        adder = int('1'*length)
        num += adder

    return res

print(sequentialDigits(58983, 123456789))
