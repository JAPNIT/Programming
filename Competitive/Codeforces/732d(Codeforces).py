n,s=map(int,input().split(" "))
days=list(map(int,input().split(" ")))
subject=list(map(int,input().split(" ")))
counter=0
day_count=0

subject.sort()
prepare_time=sum(subject)

if prepare_time < n:    
    for i in range(n):
        if len(subject)==0:
            break
        if days[i]== 0 and subject[counter] > 0:
            subject[counter] -= 1
            day_count+=1
        elif days[i]== 0 and subject[counter] == 0:
            for i in range(counter,s):
                if subject[i] == 0:
                    counter +=1
                else:
                    counter = i
                    break
            subject[counter] -= 1
            day_count+=1
        elif days[i] > 0 and 0 in subject:
            day_count+=1
            for x in range(days[i]):
                if 0 in subject:
                    subject.remove(0)
                    counter=0               
                else:
                    break
        else:
            day_count += 1
            if subject[counter] != 0:
                    subject[counter] -= 1
            elif subject[counter] == 0 :
                for i in range(counter,s):
                    if subject[i] == 0:
                        counter +=1
                    else:
                        counter = i
                        break
                subject[counter] -= 1
                day_count+=1
              
else:
    day_count = -1
print (day_count)
       
    
            
