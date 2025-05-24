'''
## Nested Loops

### Difficulty Level: Medium

### Instructions

```
1
1 2
1 2 3
1 2 3 4
```

Try to write a code that prints out the above pattern. Think of how having a loop inside another loop can achieve this.
'''

for i in range(4):
    for j in range(i+1):
        j+=1
        print(j, end = " ")
    print()