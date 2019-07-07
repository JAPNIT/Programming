global hash_table,hash_size

hash_size = 30
hash_table = [None for i in range(hash_size)]

def hash_value(s):
    hash_val = 0
    for i in range(len(s)):
        hash_val += i * ord(s[i])
    return hash_val % hash_size

def insert(s):
    hash_val = hash_value(s)
    for i in range(hash_size):
        if hash_table[(hash_val+i)%hash_size] == None:
            hash_table[(hash_val+i)%hash_size] = s
            break

def search(s):
    hash_val = hash_value(s)
    for i in range(hash_size):
        if hash_table[(hash_val+i)%hash_size] == s:
            return (hash_val+i)%hash_size
    return None

def delete(s):
    index = search(s)
    if index != None:
        hash_table[index] = None
    else:
        print("element doesn't exist")
        
    
