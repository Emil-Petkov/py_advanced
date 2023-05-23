# numbers = input().split()
#
# numbers.reverse()
#
# print(" ".join(numbers))

######################################################

# print(" ".join(input().split()[::-1]))

######################################################

# from collections import deque

# numbers = input().split()

# reverse_numbers = deque()

# for num in numbers:
#     reverse_numbers.append(num)

# while reverse_numbers:
#     print(reverse_numbers.pop(), end=" ")

#####################################################

from collections import deque

numbers = deque(input().split())

while numbers:
    print(numbers.pop(), end=" ")

    
