def str_to_int(s):
    num, power = 0, len(s)-1
    for dig in s:
        num += (ord(dig)-48) * 10**power
        power -= 1
    return num

def int_to_str(num):
    if num == 0:
        return '0'
    s = ''
    while num > 0:
        dig = num%10
        num //= 10
        s = chr(dig+48) + s
    return s

def multiply(num1, num2):
    num1, num2 = str_to_int(num1), str_to_int(num2)
    return int_to_str(num1*num2)

prod = multiply('123','456')
print(prod, type(prod))
