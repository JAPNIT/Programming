def nicecheck(word):
    
    repeat,forb=0,0

    vowel=(word.count("a")+word.count("e")+word.count("i")+word.count("o")+
           word.count("u"))
  
    if vowel>=3:
        for i in xrange(1,len(word)-1):
            if word[i]==word[i-1]:
                repeat=1
                break
    if repeat==1:
        for s in ['ab', 'cd', 'pq', 'xy']:
            if s in word:
                break
            else:
                forb=1
          
    if forb==1 and repeat==1 and vowel>=3:
        return True
    else:
        return False

f=open("Day5(input).txt")
nicestrings=0
for word in f:
    
    if nicecheck(word.strip()):
        nicestrings+=1

print nicestrings



         
                    
            
