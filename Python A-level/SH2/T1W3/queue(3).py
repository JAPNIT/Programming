global queue, size, head, tail
size = 5
queue = [None for i in range(5)]
head = 0
tail = 0

def isEmpty():
    global head, tail, queue
    if head == tail and queue[head] == None:
        return True
    return False

def isFull():
    global head, tail, queue
    if head == tail and queue[head] != None:
        return True
    return False

def enq(data):
    global size, queue, tail
    if not isFull():
        queue[tail] = data
        tail = (tail+1)%size
    else:
        print("full")

def deq():
    global size, queue, head
    if not isEmpty():
        queue[head] = None
        head = (head+1)%size
    else:
        print("Empty")

enq(9)
enq(10)
    

    
    
