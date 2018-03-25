print("Enter exit if you wish to close")
file_op = open("rational.txt","w")
while True:
    n = input("Enter rational number: ")
    try:
        if n=="exit":
            raise NameError
        n = int(n)
        file_op.write(str(n) + '\n')
    except ValueError:
        print("Please enter a valid integral input.")
    except NameError:
        break
