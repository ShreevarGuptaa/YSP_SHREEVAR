'''
## 2-D Arrays Introduction

### Difficulty Level: Easy

### Instructions
Your classroom has 3 rows and 4 columns of seats. The seating arrangement is stored in a 2-D list:

seats = [
  ["Alice", "Bob", "Carol", "David"],
  ["Eve", "Frank", "Grace", "Heidi"],
  ["Ivan", "Judy", "Mallory", "Niaj"]
]

1. Print the name of the student sitting in the **2nd row, 3rd column**
2. Print all students in the **first row**
3. Print the **entire chart**, one row per line
4. Ask the user for a name and tell whether the student is **present** or **absent**

'''
seats = [
  ["Alice", "Bob", "Carol", "David"],
  ["Eve", "Frank", "Grace", "Heidi"],
  ["Ivan", "Judy", "Mallory", "Niaj"]
]

print("1.")
for i in range(len(seats)):
    for j in range(len(seats[i])):
        if i == 1 and j == 2:
            print(seats[i][j])

print("2.")
for i in range(len(seats)):
    for j in range(len(seats[i])):
        if i == 0:
            print(seats[i][j])

print("3.")
for i in range(len(seats)):
    for j in range(len(seats[i])):
        print(seats[i][j], end = " ")
    print()

print("4.")
name = input("Kindly enter a name to search for it among the people in the seats: ")
present = False

for i in range(len(seats)):
    for j in range(len(seats[i])):
        if name == seats[i][j]:
            present = True

if present:
    print(f"{name} is present.")
else:
    print(f"{name} is absent.")