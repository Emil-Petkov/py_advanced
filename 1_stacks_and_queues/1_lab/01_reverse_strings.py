text = input()

stack = []

for el in text:
    stack.append(el)

reverse_text = ""

while stack:
    reverse_text += stack.pop()

print(reverse_text)


# stack = list(input())
#
# while stack:
#    el = stack.pop()
#    print(el, end="")
