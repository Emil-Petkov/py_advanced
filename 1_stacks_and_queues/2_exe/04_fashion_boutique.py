clothe_in_box = list(map(int, input().split()))
rack_capacity = int(input())

total_capacity = rack_capacity
count_rack = 1


while clothe_in_box:

    piece_of_clothing = clothe_in_box[-1]
    if piece_of_clothing > total_capacity:
        count_rack += 1
        total_capacity = rack_capacity

    else:
        total_capacity -= piece_of_clothing
        clothe_in_box.pop()

print(count_rack)
