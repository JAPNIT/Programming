def d2k(n,k):
    mapping = "0123456789abcdefg"
    s = ""
    while n> 0:
        s = mapping[n%k] + s
        n //= k
    return s

def index(a):
    mapping = "0123456789abcdef"
    for i in range(len(mapping)):
        if a == mapping[i]:
            return i
def k2d(s,k):
    n = 0
    power = len(s) - 1
    for i in range(len(s)):
        n += index(s[i]) * pow(k,power)
        power -= 1
    return n
