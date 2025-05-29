'''
## The Cult of Pattern

### Difficulty Level: Hard

### Instructions
You have just found a coded ritual pattern in an old manuscript. If you print it exactly for n = 5, it reveals the hidden symbol of an ancient cult.
The pattern looks like:

```
*       *
 *     * 
  *   *  
   * *   
    *    
   * *   
  *   *  
 *     * 
*       *
```

**Challenge:**
1. Recreate this by coding using loops.

2. Then, refactor your code into 2 or more functions — because the pattern is symmetrical. Can you figure out the best way to break it up?

> Note: If you don't understand something, look up what it means.

##################################################################################################################################

I had to look up some stuff because I did not understand a few words. After that this is my solution.

##################################################################################################################################
'''

#Part 1
n = 5
size = 2 * n - 1

for i in range(size):
    for j in range(size):
        if j == i or j == size - 1 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Part 2
def print_line(i, size):
    line = ""
    for j in range(size):
        if j == i or j == size - 1 - i:
            line += "*"
        else:
            line += " "
    print(line)

def print_pattern(n):
    size = 2 * n - 1
    # Top half
    for i in range(n):
        print_line(i, size)
    # Bottom half (mirrored)
    for i in range(n - 2, -1, -1):
        print_line(i, size)
