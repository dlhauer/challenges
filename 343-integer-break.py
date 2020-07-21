def integerBreak(n):
    if n < 4:
        return n-1
    factor, power = 2, 0
    for _ in range(2, n+1):
        res = factor * 3**power
        factor += 1
        if factor > 4:
            factor = 2
            power += 1
    return res
