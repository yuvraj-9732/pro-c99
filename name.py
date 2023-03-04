name = input("Enter your name: ")
rows = 10

# Print the top half of the star pattern
for i in range(rows):
    for j in range(rows - i):
        print("*", end="")
    for k in range(2 * i):
        print(" ", end="")
    for l in range(rows - i):
        print("*", end="")
    print()

# Print the name in the center row
print("*" * ((2 * rows - len(name) - 2) // 2) + " " + name + " " + "*" * ((2 * rows - len(name) - 2) // 2 + (2 * rows - len(name) - 2) % 2))

# Print the bottom half of the star pattern
for i in range(rows - 1, -1, -1):
    for j in range(rows - i):
        print("*", end="")
    for k in range(2 * i):
        print(" ", end="")
    for l in range(rows - i):
        print("*", end="")
    print()
