def fast_pow(x, p):
    # if power is negrative
    if p < 0:
        # change power to positive
        p = -p
        # change x to 1/x
        x = 1. / x
    # creating temp value = x
    temp = x
    t = 1
    # while p != 0
    while p:
        # if p / 2 == integer
        if p % 2:
            t *= temp
        temp *= temp
        p //= 2
    return t

print(fast_pow(15, 85))
