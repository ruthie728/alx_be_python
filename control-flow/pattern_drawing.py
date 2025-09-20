size = int(input("Enter the size of the pattern: "))
current_row = 0

while current_row < size:
    for current_column in range(size):
        print("*", end="")
    print()
    current_row += 1