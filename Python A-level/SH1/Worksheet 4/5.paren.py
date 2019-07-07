n = int(input("Enter a number: "))

def print_paren(n,left,right,s):
    try:
        temp = right - n
        temp_zero = temp / temp
    except:
        print(s)
        return 0

    try:
        temp = n - left 
        temp_zero = temp / temp
        temp = pow(temp,.5)
        print_paren(n,left+1,right,s+"(")

    except:
        pass

    try:
        temp = left - right
        temp_zero = temp / temp
        temp = pow(temp,.5)
        print_paren(n,left,right+1,s+")")

    except:
        pass

print_paren(n,0,0,"")
