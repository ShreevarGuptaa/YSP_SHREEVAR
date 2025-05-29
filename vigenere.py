def vigenere(message, word):
    message = message.replace(" ", "")
    encrypt = []
    word = (word * ((len(message) // len(word)) + 1))[0:len(message)]

    for i in range(len(message)):
        char = message[i]
        key_char = word[i]

        if char.isupper():
            encrypted_char = chr(((ord(char) + ord(key_char) - 130) % 26) + 65)
        elif char.islower():
            encrypted_char = chr(((ord(char) + ord(key_char) - 194) % 26) + 97)
        else:
            encrypted_char = char
        encrypt.append(encrypted_char)

    return "".join(encrypt)
    
message = input("Enter the message. ")
word = input("Enter the word. ")
print(vigenere(message, word))