from random import randint

for i in range(100):
    name = ""
    name = name + str(randint(0,9))
    name = name + ".txt"
    try:
        f = open(name,"r")
        data = f.read()
        f.close()

    except:
        pass

