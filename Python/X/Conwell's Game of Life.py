s=raw_input()
cells=[]

for i in xrange(0,len(s)):
    if i == 0:
        if s[1]=="1" and s[len(s)-1]=="0":
            if s[i]=="0":
                cells.append(1)
            elif s[i]=="1":
                cells.append(0)
        elif s[1]=="0" and s[len(s)-1]=="1":
            if s[i]=="0":
                cells.append(1)
            elif s[i]=="1":
                cells.append(0)
        else:
            cells.append(int(s[i]))
    elif i==len(s)-1:
        if s[i-1]=="1" and s[0]=="0":
            if s[i]=="0":
                cells.append(1)
            elif s[i]=="1":
                cells.append(0)
        elif s[i-1]=="0" and s[0]=="1":
            if s[i]=="0":
                cells.append(1)
            elif s[i]=="1":
                cells.append(0)
        else:
            cells.append(int(s[i]))
    else:
        if s[i-1]=="1" and s[i+1]=="0":
            if s[i]=="0":
                cells.append(1)
            elif s[i]=="1":
                cells.append(0)
        elif s[i-1]=="0" and s[i+1]=="1":
            if s[i]=="0":
                cells.append(1)
            elif s[i]=="1":
                cells.append(0)
        else:
            cells.append(int(s[i]))
print cells  
        
        
