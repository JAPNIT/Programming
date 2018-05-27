a1=[16, 10, 13, 17, 11, 6, 4, 7, 18, 19, 2, 20, 12, 9, 1, 24, 22, 15, 8, 21, 23, 14, 5, 25, 3, 0]
a2=[22, 9, 1, 3, 17, 8, 23, 2, 6, 18, 16, 0, 25, 14, 4, 10, 19, 5, 21, 20, 24, 7, 13, 15, 12, 11]

start=[0,0]
c=raw_input()
m=""
n=0

#input - qlnt

for f in xrange(26):
    if m=="good":
            break
    for y in xrange(26):
        if m=="good":
            break
        start=[f,y]
        m="" 
        n=0
        l=len(c)
        aone=a1.index(start[0])
        atwo=a2.index(start[1])
            
        a1=a1[aone:]+a1[:aone]
        a2=a2[atwo:]+a2[:atwo]
            
        for i in xrange(26):
            if l==0:
                break
            for x in xrange(26):
                if l==0:
                    break
                shift=a2[i] + a1[x]
                pos=(ord(c[n])-96)-shift
                        
                if pos<0:
                    m=m+ chr(122-abs(pos))
                elif pos==0:
                    m=m+"z"
                else:
                    m=m+chr(ord(c[n])-shift)
                n+=1
                l-=1
        

print start
        

