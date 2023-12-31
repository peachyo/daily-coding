# O(logx + logy)
def gcd(x, y):
    if x > y:
        return gcd(y, x)
    elif x == 0:
        return y
    elif not x & 1 and not y & 1:  # x and y are even
        return gcd(x >> 1, y >> 1) << 1
    elif not x & 1 and y & 1:  # x is even, y is odd
        return gcd(x >> 1, y)
    elif x & 1 and not y & 1:  # x is odd, y is even
        return gcd(x, y >> 1)
    return gcd(x, y - x)  # both x and y are odd
