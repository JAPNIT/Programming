def get_hash(my_string):
    total = 0
    for i in range(len(my_string)):
        total += i*ord(my_string[i])
    return total
Loans = [None for i in range(97)]
HT1 = [None for i in range(97)] #book title 
HT2 = [None for i in range(97)] #person borrowing

def insert(book_title, person_borrowing):
    hash_title = get_hash(book_title) % 97
    hash_person = get_hash(person_borrowing) % 97
    index = -1
    
    for i in range(len(Loan)):
        if Loan[i] == None:
            Loan[i] = [book_title,person_borrowing]
            index = i

    for i in range(97):
        temp = (hash_title + i) % 97
        if HT1[temp] == None:
            HT1[temp] = index
            break

    for i in range(97):
        temp = (hash_person + i) % 97
        if HT2[temp] == None:
            HT2[temp] = index
            break

    
    

    
