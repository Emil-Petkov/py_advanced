# firs_set = set()
# second_set = set()
#
# set_of_elements = [int(num) for num in input().split()]
#
# for el in range(set_of_elements[0]):
#     current_element = int(input())
#     firs_set.add(current_element)
#
# for el in range(set_of_elements[1]):
#     current_element = int(input())
#     second_set.add(current_element)
#
# print(*firs_set.intersection(second_set), sep="\n")


n_elements = [int(num) for num in input().split()]

first_set = set([int(input()) for _ in range(n_elements[0])])
second_set = set([int(input()) for _ in range(n_elements[1])])

print(*first_set.intersection(second_set), sep="\n")
