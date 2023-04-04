expression = input()

opening_bracket_index = []

for i in range(len(expression)):
    ch = expression[i]
    if ch == "(":
        opening_bracket_index.append(i)
    elif ch == ")":
        open_bracket = opening_bracket_index.pop()
        closed_bracket = i + 1

        print(expression[open_bracket:closed_bracket])
