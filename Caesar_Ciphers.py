'''
## Understanding Caesar Ciphers

### Difficulty Level: Easy

### Instructions
You've been hired to help a robot design a welcome banner using only letters and ASCII codes.
Your task is to write a function that:
Takes a word as input (e.g., "HELLO").

Converts each letter into its **ASCII value** using ord().

Then, **shifts** each ASCII value by +1 and prints the new character using chr().
**Input**:  "DOG"
**Output**: "EPH"  # 'D' → 68 → 69 → 'E', and so on
**Extension**: Can you recover the initial message?
'''

word = input("Enter a word: ")

shifted_chars = []
for c in word:
    if c.isalpha():
        ascii_val = ord(c)
        shifted_val = ascii_val + 1
        shifted_char = chr(shifted_val)
        shifted_chars.append(shifted_char)
    else:
        shifted_chars.append(c)

shifted = ''.join(shifted_chars)

original_chars = []
for c in shifted:
    if c.isalpha():
        ascii_val = ord(c)
        unshifted_val = ascii_val - 1
        unshifted_char = chr(unshifted_val)
        original_chars.append(unshifted_char)
    else:
        original_chars.append(c)

original = ''.join(original_chars)

print("Shifted : ", shifted)
print("Original: ", original)
