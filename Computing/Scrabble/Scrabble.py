import random
global piles,board,current_player,row_1,col_1,row_2,col_2,board_temp,score_board,words,pile_temp

def refill_pile(pile): #refills player's pile after their turn
    global letters
    new = 7 - len(pile)
    for i in range(new):
        pile.append(letters[i])
    letters = letters[new:]
    return pile
    
def score_word(premium_score): #scores every word made in accordance with the premium tiles
    points = { "e":1,"a":1,"i":1,"o":1,"n":1,"r":1,"t":1,"l":1,"s":1,"u":1,"d":2,"g":2,"b":3,"c":3,"m":3,"p":3,
              "f":4,"h":4,"v":4,"w":4,"y":4,"k":5,"j":8,"x":8, "q":1,"z":1}
    
    for w in words:
        word_score = 0
        flag = ''
        for x in w:
            bonus = premium_score[x]
            if bonus == "X":
                word_score += (points[x] * 3)
                print("WOOHOO! You got a Triple Letter Bonus!")
            elif bonus == "O":
                word_score += (points[x] * 2)
                print("WOOHOO! You got a Double Letter Bonus!")
            elif bonus == "T":
                word_score += points[x]
                flag = "T"
            elif bonus == "D":
                word_score += points[x]
                flag ="D"
            else:
                word_score += points[x]
    
        if flag == "T":
            score_board[current_player] += (word_score*3)
            print("WOOHOO! You got a Triple Word Bonus!")
        elif flag == "D":
            score_board[current_player] += (word_score*2)
            print("WOOHOO! You got a Double Word Bonus!")
        else:
            score_board[current_player] += word_score
        print("The word " +  str(w) + " got you " + str(word_score) +" points")
        print("\n")
           
def validity_check(premium_score):#checks the validity of all the words
    for w in words:
        start_letter=w[0]
        file_name = start_letter.upper() + " Words.csv"
        with open(file_name, 'r', encoding="utf-8") as file:
            file = file.read().splitlines()
            if w not in file:
                print( w + " is not a valid word")
                raise ZeroDivisionError #raise relevant error
                return 0
    score_word(premium_score)

def premium_tiles():#prints premium tiles on the board
    board[0][0] = "T"
    board[7][0] = "T"
    board[14][0] = "T"
    board[0][7] = "T"
    board[14][7] = "T"
    board[0][14] = "T"
    board[7][14] = "T"
    board[14][14] = "T"

    board[3][0] = "X"
    board[11][0] = "X"
    board[3][14] = "X"
    board[11][14] = "X"
    
    board[6][2] = "X"
    board[8][2] = "X"
    board[6][12] = "X"
    board[8][12] = "X"

    board[0][3] = "X"
    board[7][3] = "X"
    board[14][3] = "X"
    board[0][11] = "X"
    board[7][11] = "X"
    board[14][11] = "X"

    board[5][1] = "O"
    board[9][1] = "O"
    board[5][13] = "O"
    board[9][13] = "O"
    
    board[1][5] = "O"
    board[5][5] = "O"
    board[9][5] = "O"
    board[13][5] = "O"
    board[1][9] = "O"
    board[5][9] = "O"
    board[9][9] = "O"
    board[13][9] = "O"

    for i,j in zip(range(14,-1,-1), range(14,-1,-1)):
        if board[i][j] == ".":
            board[i][j] = "D"
    for i,j in zip(range(0,15,1), range(14,-1,-1)):
        if board[i][j] == ".":
            board[i][j] = "D"
    
            
def words_separate(premium_score):#makes a list "words" to store all the words made by the player
    global premium,words
    if col_1 == col_2:

        #Getting the vertical word
        row_temp = row_1
        word=""
        while row_temp >= 0:
            if board[row_temp][col_1] in premium:
                break
            row_temp -= 1
        row_temp += 1 
        while board[row_temp][col_1] not in premium:
            word += board[row_temp][col_1]
            row_temp+=1
        words.append(word)

        #Getting the horizontal words
        for i in range(row_1,row_2):
            col_temp = col_1
            word = ""
            while col_temp >= 0:
                if board[i][col_temp]  in premium:
                    break
                col_temp -= 1
            col_temp += 1

            while board[i][col_temp] in premium:
                word += board[i][col_temp]
                col_temp += 1
            words.append(word)

    if row_1 == row_2:

        #Getting the horizontal word
        col_temp = col_1
        word = ""
        while col_temp >= 0:
            if board[row_1][col_temp] in premium:
                break
            col_temp -= 1
        col_temp += 1

        while board[row_1][col_temp] not in premium:
            word += board[row_1][col_temp]
            col_temp += 1
        words.append(word)

        #Getting the vertical words
        for i in range(col_1,col_2):
            row_temp = row_1
            word=""
            while row_temp >= 0:
                if board[row_temp][i] in premium:
                    break
                row_temp -= 1
            row_temp += 1 
            while board[row_temp][i] not in premium:
                word += board[row_temp][i]
                row_temp+=1
            words.append(word)
    temp = []
    for i in words:
        if len(i) > 1:
            temp.append(i)
    words = [i for i in temp]

    validity_check(premium_score)
            
    
def place_board(word_input):#places the word on the board
    global premium
    premium_score = {}
    pile_temp = piles[current_player][:]
    for alpha in word_input:
        if alpha not in pile_temp:
            raise NameError 
            return 0
        pile_temp.remove(alpha) 

    if row_1 >= 15 or row_2 >= 15 or col_1 >= 15 or col_2 >= 15:
        raise IndexError
    
    #Placement of word
    count = 0
    if row_1 == row_2:
        for i in range(col_1,col_2):
            if board[row_1][i] in premium:
                premium_score[word_input[count]] = board[row_1][i]
            board[row_1][i] = word_input[count]
            count +=1

    if col_1 == col_2:
        for i in range(row_1,row_2):
            if board[i][col_1] in premium:
                premium_score[word_input[count]] = board[i][col_1]
            board[i][col_1] = word_input[count]
            count +=1
    words_separate(premium_score)
    return pile_temp
        

def print_board(board): #prints board
    
    for i in range(15):
        for j in range(15):
            print(board[i][j], end= " ")
        print("\n")
    print("T: Triple word, D:Double word, X: Triple Letter, O: Double Letter")
    print("\n")


#Main Program
print("Welcome! Let's play SCRABBLE!")
choice = input("Type play to start playing and exit to quit: ")

if choice == "play":
    no_players = int(input("Enter the number of players: "))

    #letters for the pile
    letters = "a" * 9 + "b" * 2 + "c" * 2 + "d" * 4 + "e" * 12 + "f" * 2 + "g" * 3+ "h" * 2 + "i" * 9 + "j" + "k" + "l" * 4 + "m" * 2 + "n" * 6 + "o" * 8+ "p" * 2 + "q" * 1 + "r" * 6 + "s" * 4 + "t" * 6 + "u" * 4 + "v" * 2 + "w" * 2+"x" * 1 + "y" *2 + "z" * 1
    letters = list(letters)
    random.shuffle(letters)

    #making letter piles and storing player's names
    current_player = 0
    players = []
    piles = [[],[],[],[]]
    score_board = [0,0,0,0]
    for i in range(no_players):
        p = input("Player number " + str(i+1) + ": ")
        players.append(p)
        
        piles[i] = letters[:7]
        letters = letters[7:]

    #Getting the board ready    
    premium = [".","T","D","O","X"]
    board = [["." for i in range(15)] for i in range(15)]
    premium_tiles()
    print("\n")
    print_board(board)
    
    while len(letters)>7:

        #Instructions
        print("It is " + players[current_player] +"'s turn!")
        print(players[current_player] + "'s rack: ")
        print(piles[current_player])
        print("\n")
        
        flag = True
        words=[]

        play = input("Type play to make a word, type exchange to exchange your tiles and type exit to quit: ")
        
        if play == "play":
            while flag:
                
                #Inputs for the word
                length = int(input("Enter the length of the word: "))
                print("\n")
                row_1 = int(input("Enter the start row(0-14): "))
                col_1 = int(input("Enter the start col(0-14): "))
                print("\n")
                print("For the end row/col just add the length of the word to the initial row/col")
                row_2 = int(input("Enter the end row(0-14): "))
                col_2 = int(input("Enter the end col(0-14): "))
                print("\n")
                word_input = input("Enter the word: ")
                
                try:
                    pile_temp=place_board(word_input)
                    flag = False
                    
                except ZeroDivisionError: #Word is not valid or the position is occupied
                    flag = True
                    words=[]
                    if row_1 == row_2:
                        for i in range(col_1,col_2):
                            board[row_1][i] = "."

                    if col_1 == col_2:
                        for i in range(row_1,row_2):
                            board[i][col_1] = "."

                except NameError:#Letter is not in the player's rack
                    print("Letter not in pile")
                    flag = True
                    words=[]

                except IndexError:#Invalid row or col 
                    print("Enter valid row and col")
                    flag = True
                    words = []
    
            print_board(board)

            piles[current_player] = refill_pile(pile_temp)
            
        elif play == "exchange":
            new = int(input("How many tiles do you want to exchange? "))
            for i in range(new):
                temp = piles[current_player][i]
                piles[current_player][i] = letters[i]
                letters[i] = temp

        else:
            print("Bye Bye! See you later!")
            break
        
        print("Your new rack is: ")
        print(piles[current_player])
        print("\n")

        print("~~ SCOREBOARD ~~")
        for i in range(no_players):
            print(players[i] + " : " + str(score_board[i]) )
        print("\n")
        
        #Changing player
        current_player = (current_player + 1) % no_players

        
        
        
    


