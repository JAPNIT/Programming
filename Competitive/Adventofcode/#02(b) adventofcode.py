ribbon=0
f = open('Day2(input).txt')
for line in f:
    l,w,h=map(int,line.split('x'))
    ribbon+=min(2*(l+w),2*(h+l),2*(h+w))
    ribbon+=l*w*h

   
  
print ribbon
