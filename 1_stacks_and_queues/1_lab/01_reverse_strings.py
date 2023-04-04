text = "hello"

lst_stack = []

for el in text:
    lst_stack.append(el)

reverse_text = ""

while lst_stack:
    reverse_text += lst_stack.pop()

print(reverse_text)