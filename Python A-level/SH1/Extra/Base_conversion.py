def index(a,n):
    for i in range(len(a)):
        if a[i] == n:
            return i
    return None

def denary_to_k(n,k):
    digit_map = "0123456789abcedf"
    base_k = ""
    while n > 0:
        val = n%k
        n = n//k
        base_k = digit_map[val] + base_k
    print(base_k)

def k_to_denary(n,k):
    digit_map = "0123456789abcdef"
    denary = 0
    power = len(n) - 1
    for i in range(len(n)):
        val = index(digit_map,n[i])
        print(val,power)
        denary += val * (pow(k,power))
        power -= 1
    print(denary)
                   
