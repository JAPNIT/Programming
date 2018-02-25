p1 = input("Player1? ")
p2 = input("Player2? ")

def assigning_no(choice):
    if choice == "rock":
        return 0
    elif choice == "spock":
        return 1
    elif choice == "paper":
        return 2
    elif choice == "lizard":
        return 3
    elif choice == "scissors":
        return 4

p1 = assigning_no(p1)
p2 = assigning_no(p2)

if (p1+2) % 5 == p2 or (p1+1) % 5 == p2:
    print ("Player 2 wins")
elif p1 == p2:
    print ("It's a tie!")
else:
    print ("Player 1 wins")
