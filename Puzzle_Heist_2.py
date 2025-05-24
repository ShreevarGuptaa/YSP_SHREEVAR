'''
## Puzzle Heist: Challenge 2

### Difficulty Level: Hard

### Instructions
Doing this challenge **requires** you to have done the Puzzle Heist: Challenge 1. If you have completed that, then write a python program for the entire puzzle that outputs the final 4-digit number.
'''

def digit_root(n):
    while n > 9:
        s = 0
        for d in str(n):
            s += int(d)
        n = s
    return n

def round1(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])

    letter = word[6]

    unique_vowels = set()
    for c in word:
        lower_c = c.lower()
        if lower_c in vowels:
            unique_vowels.add(lower_c)
    shift = len(unique_vowels)

    if letter.isupper():
        base = ord('A')
    else:
        base = ord('a')
    letter_pos = ord(letter) - base
    shifted_pos = (letter_pos + shift) % 26
    shifted_letter = chr(base + shifted_pos)

    unique_consonants = set()
    for c in word:
        lower_c = c.lower()
        if c.isalpha() and lower_c not in vowels:
            unique_consonants.add(lower_c)
    ascii_val = ord(shifted_letter) + len(unique_consonants)

    return digit_root(ascii_val)

def round2(sentence):
    sentence_clean = ""
    for ch in sentence:
        if ch not in [',', '.']:
            sentence_clean += ch
            
    words = sentence_clean.split()
    
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    m = 0
    for w in words:
        if len(w) < 5:
            m += 1

    n = 1
    for w in words:
        if len(w) > 5:
            n += 1

    nth_word = words[n-1]
    nth_word_reversed = ""
    for i in range(len(nth_word)-1, -1, -1):
        nth_word_reversed += nth_word[i]

    mth_word = words[m-1]
    mth_word_no_vowels = ""
    for ch in mth_word:
        if ch not in vowels:
            mth_word_no_vowels += ch

    combined = nth_word_reversed + mth_word_no_vowels

    return digit_root(len(combined))

def round3():
    grid = [
        ['T', 'R', 'A', 'C', 'E'],
        ['H', 'A', 'C', 'K', 'S'],
        ['O', 'N', 'L', 'I', 'N'],
        ['E', 'D', 'A', 'T', 'A'],
        ['P', 'A', 'S', 'S', 'W'],
        ['O', 'R', 'D', 'S', '!']
    ]
    coords = [(0,0), (1,2), (2,3), (3,1), (4,4), (5,0), (2,0), (3,3), (5,2)]
    
    letters = []
    for coord in coords:
        r, c = coord
        letters.append(grid[r][c])
    seq = ""
    for l in letters:
        seq += l
    
    rev_seq = ""
    for i in range(len(seq)-1, -1, -1):
        rev_seq += seq[i]
    
    vowels = set(['a','e','i','o','u','A','E','I','O','U'])
    unique_consonants = set()
    for ch in rev_seq:
        if ch.isalpha() and ch not in vowels:
            unique_consonants.add(ch.lower())
    
    count = len(unique_consonants)
    
    return digit_root(count)

def round4(sequence):
    positions = []
    for ch in sequence:
        pos = ord(ch.upper()) - ord('A') + 1
        positions.append(pos)
    
    last_pos = positions[-1]
    next_pos = last_pos + 3
    if next_pos > 26:
        next_pos = next_pos % 26
    
    next_letter = chr(next_pos - 1 + ord('A'))
    
    x = next_pos
    y = len(sequence)
    z = y % x
    
    return z

word1 = "mAkErSpAcE"
sentence2 = "Cyber security is a shared responsibility, not just an IT concern."
sequence4 = ['B', 'E', 'H', 'K', 'N']
    
d1 = round1(word1)
d2 = round2(sentence2)
d3 = round3()
d4 = round4(sequence4)
    
print(f"Final code: {d1}{d2}{d3}{d4}")