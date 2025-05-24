'''
## Invariants

### Difficulty Level: Hard

### Instructions
Understand what invariants are and identify the invariants of the very basic algorithms we are writing in the class. You can find the algorithms from the notebooks or challenge cards.

##################################################################################################################################

MY RESEARCH:
Invariants in programming are conditions or properties that are guaranteed to be true throughout a program's execution, especially during specific phases like loop iterations or class object lifetimes. They help with code correctness, debugging, and reasoning about program behavior.

For example, kindly look at the program below:
'''

### START OF PROGRAM
Japan= ["Japan", "Sushi", "Anime", "Tokyo", "Ramen", "Shinjuku", "Manga", "Tokusatsu", "Kyoto", "Hirohiko Araki", "Rumiko Takahashi", "Shinjuku", "Samurai"]

comments = ["The samurai were so cool.","I think sushi tastes very bad.", "I hate dancing.","Tokyo must be a fun","Anime is my life I swear."]

for word in Japan:
    Japan = [word.lower()]

for comment in comments:
    comment_lower = comment.lower()
    matched_keywords = []
    for kw in Japan:
        if kw in comment_lower:
            matched_keywords.append(kw)
    
    print(f"Comment: {comment}")

    if matched_keywords:
        print("Refers to Japan")
    else:
        print("Does not refer to Japan")
### END OF CODE

'''
In this code, I think that *Japan* is an invaraint because it is never modified, a new array is created for the modified elements. Then *japan_keywords* is also an invariant because it stays constant during the checking period. *comments* is another one which is constant throughout. *comment_lower* too for the same reason. So in short we have 4 invariants:
1. Japan
2. japan_keywords
3. comments
4. comment_lower 

SOURCES: https://docs.oracle.com/cd/E19455-01/806-5257/guide-6/
'''