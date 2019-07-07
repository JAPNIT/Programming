global stack_size
stack_size = 5
global stack
stack = [None for i in range(stack_size)]
global top
top = -1

def isEmpty():
    global top
    if top == -1:
        return True
    return False

def isFull():
    global top
    if top == stack_size-1:
        return True
    return False

def push(data):
    global top
    if not isFull():
        top += 1
        stack[top] = data

        
    else:
        print("Full")

def pop():
    global top
    if not isEmpty():
        stack[top] = None
        top -= 1
    else:
        print("Empty")
    
    
push(3)
push(9)
push(3)
push(9)
push(3)
push(9)
pop()






