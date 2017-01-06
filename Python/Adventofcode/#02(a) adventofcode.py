paper=0
f = open('Day2(input).txt')
for line in f:
    l,w,h=map(int,line.split('x'))
    paper+=2*l*w + 2*w*h + 2*h*l
    s=min(l*w,h*w,h*l)
    paper+=s
  
print paper
