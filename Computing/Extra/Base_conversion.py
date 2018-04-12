def base_10_to_base_k(n,k):
    digit_map = "0123456789abcedefghijklmnopqrstuvwxyz"
    base_k = ""
    while n != 0:
        val = n%k
        base_k += digit_map[val]
        n = n//2
    print(base_k[::-1])

def base_k_to_base_10(n,k):
    l = len(str(n)) -1 
    base_10 = 0
    for i in range(len(str(n))):
        val = str(n)[l]
        base_10 += int(val) * (k**i)
        l -= 1
    print(base_10)
    
base_10_to_base_k(124,2)
base_k_to_base_10(22,16)
