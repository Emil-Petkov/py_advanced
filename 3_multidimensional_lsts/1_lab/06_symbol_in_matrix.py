matrix = [[el for el in input()] for _ in range(int(input()))]

searched_element = input()

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == searched_element:
            print(f"({row}, {col})")
            exit()
else:
    print(f"{searched_element} does not occur in the matrix")
    exit()
