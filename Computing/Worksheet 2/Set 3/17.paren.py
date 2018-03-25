n = int(input("Enter the number: "))
def print_paren(n,left,right,s):
    if right == n:
        print(s)
        return 0
    if left < n:
        print_paren(n,left+1,right,s+"(")
    if right < left:
        print_paren(n,left,right+1,s+")")

print_paren(n,0,0,"")
