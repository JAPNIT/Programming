price,coin= map(int,input().split(" "))
num=1
while True:
    cost= price * num

    cost=str(cost)
    left=int(cost[-1])117 3
    

    if left==coin or left==0: 
        break
    num += 1

print (num)
    

        
    
