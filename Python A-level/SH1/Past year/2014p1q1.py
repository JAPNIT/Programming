f = open("jargon.txt","r").read()
f = list(f.split("\n"))
term = ""

while True:
    count = 0
    print("1.Exact Match")
    print("2.Start of the term")
    print("3.Within the term")

    choice = int(input("Enter your choice: "))
    term = input("Enter the term: ")

    if term == "XXX":
        break
    
    for i in f:
        if choice == 1:
            if term == i:
                count += 1
                print(i)
        elif choice == 2:
            index = 0
            if term == i[:len(term)]:
                count += 1
                print(i)
        else:
            if term in i and term != i[:len(term)]:
                count += 1
                print(i)
    print(str(count) + " matching term(s)")
    print()
