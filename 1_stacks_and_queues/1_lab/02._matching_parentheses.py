data = input()

open_bracket = []

for index in range(len(data)):
    ch = data[index]
    if ch == "(":
        open_bracket.append(index)

    elif ch == ")":
        open_index = open_bracket.pop()
        close_index = index + 1

        print(data[open_index:close_index])

        
