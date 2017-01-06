s_time1,s_time2,f_time1,f_time2,p_time=map(int,input().split(" "))

timeset=[]

timeset.append(max(s_time1,f_time1))
timeset.append(min(s_time2,f_time2))

time=(timeset[1]+1)-timeset[0]

if p_time >= timeset[0] and p_time <= timeset[1]:
    time -= 1
if time < 0:
    time=0

print(time)



        
