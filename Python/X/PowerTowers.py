n,k=map(int,raw_input().split(' '))
first=map(int,raw_input().split(' '))
second=map(int,raw_input().split(' '))

first=first[::-1]
second=second[::-1]

while n!=1:
    f=first[1] ** first[0]
    first.pop(1)
    first.pop(0)
    first.insert(0,f)
    print f
    n=len(first)

while k!=1:
    s=second[1] ** second[0]
    second.pop(1)
    second.pop(0)
    second.insert(0,s)
    print s
    k=len(second)

if s>f:
    print "Second"
elif s==f:
    print "Equal"
else:
    print "First"
    
