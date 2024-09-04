

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("WELCOME TO THE CAESAR CIPHER")

'''-------ENCODE FUNCTION---------'''
def encrypt(text, shift):
    cipher = ""
    for char in code:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            cipher = cipher + alphabet[new_position]
            if new_position > 25:
                new_position = new_position - 26
        else:
            print("invalid text")
    return cipher


'''-------DECODE FUNCTION---------'''
def decrypt(text, shift):
    cipher = ""
    for char in code:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - shift
            cipher = cipher + alphabet[new_position]
            if new_position < 0:
                new_position = new_position + 26
        else:
            print("invalid text")
    return cipher


'''-------USER INPUT--------'''
text = input("Type your message:\n").lower()
code = []
for letters in text:
    code.append(letters)



'''------SHIFT VALUE------'''
shift = int(input("Type the shift number:\n"))
if shift < 0:
    shift = shift * -1



'''--------ENCRYPT OR DECRYPT---------'''
todo = input("Type 'encode' to encrypt, type 'decode' to decrypt.\n")
if todo == "encode":
    print(encrypt(text, shift))
elif todo == "decode":
    print(decrypt(text, shift))




