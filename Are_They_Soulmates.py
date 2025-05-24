'''
## Are They Soulmates?

### Difficulty Level: Medium

### Instructions
You are given names of two people (your function inputs). Your task is to determine if their relationship is “magical.” A magical bond exists if the string formed by combining both names (ignoring spaces and cases- account for these using appropriate python functions) reads the same forwards and backwards.
**Example**:
 Input: "Ann" and "Anna" → Output: “Magical!”
 ("annanna" reversed is the same)
'''

def magical(name1, name2):
    name1.replace(" ", "")
    name2.replace(" ", "")
    str = name1.lower() + name2.lower()

    rev = str[::-1]
    if str == rev:
        print("Magical!")
    else:
        print("Not magical :C")