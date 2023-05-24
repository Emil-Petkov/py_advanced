def check_brackets(check):
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    open_brackets = bracket_map.keys()

    stack = []

    for br in check:
        if br in open_brackets:
            stack.append(br)
        elif stack and br == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return "NO"

    return "YES"


print(check_brackets(input()))


##################################################################


# from collections import deque

# parenthesis = (deque(input()))
# open_parenthesis = deque()

# while parenthesis:
#     current_parenthesis = parenthesis.popleft()

#     if current_parenthesis in "{[(":
#         open_parenthesis.append(current_parenthesis)

#     elif not open_parenthesis:
#         print("NO")
#         break
#     else:
#         if f"{open_parenthesis.pop() + current_parenthesis}" not in '(){}[]':
#             print("NO")
#             break
# else:
#     print("YES")
