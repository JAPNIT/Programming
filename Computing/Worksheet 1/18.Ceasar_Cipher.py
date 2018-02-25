text = input("Enter the text: ")
key = int(input("Enter the shift key: "))
encrypt = ''

for x in text:
    ascii_code = ord(x)
    
    if ascii_code < 97 and ascii_code >= 65:
        alpha_value = ascii_code - 65 # position of the letter 
        ascii_code = ((alpha_value + key) % 26) + 65 # applying the shift
        encrypt += chr(ascii_code)
    elif ascii_code >=  97:
        alpha_value = ascii_code - 97 # position of the letter
        ascii_code = ((alpha_value + key) % 26) + 97 # applying the shift
        encrypt += chr(ascii_code)
    else:
        encrypt += x

print (encrypt)
