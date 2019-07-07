# functions
# assignment
# operators
def add(a,b):
    try:
        return a+b
    except:
        a = variables[str(a)]
def sub(a,b):
    return a-b
def mod(a,b):
    return a%b
def div(a,b):
    return a / b
def int_div(a,b):
    return a//b
def pow(a,b):
    return a**b

def expression_calc(i):
    operators = ["+","-","/","//","**","*"]
    flag = False
    a=""
    b=""
    o =""
    for x in i:
        if x in operators:
            flag = True
            o+=x
        elif flag:
            b+=x
        else:
            a+=x
    print(a,b)
    if o == "+":
        return add(int(a),int(b))
    elif o == "-":
        return sub(int(a),int(b))
    elif o == "%":
        return mod(int(a),int(b))
    elif o == "/":
        return div(int(a),int(b))
    elif o == "//":
        return int_div(int(a),int(b))
    elif o == "**":
        return pow(int(a),int(b))
    else:
        return int(a)
    
    
def print_calc(i):
    print("inside")
    
variables = {}
while True:
    try:
        inp = input()
        variable = ""
        exp = ""
        flag = False
        if inp[:5] == "print":
            print_calc(inp[5:])
        else:
            for x in inp:
                if x == "=":
                    flag = True
                elif flag:
                    exp += x
                else:
                    variable += x
            variables[variable] = expression_calc(exp)

    except:
        break
        


print(variables)
