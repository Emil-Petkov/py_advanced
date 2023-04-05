data = input().split()

rev = []

for num in range(len(data)):
    l_el = data.pop()
    rev.append(l_el)

print(' '.join(rev))

# print(' '.join(reversed([num for num in input().split()])))
#
#
# data = input().split()
# rev = reversed(data)
# print(' '.join(rev))
#
#
# data = input().split()
# print(' '.join(data[::-1]))
