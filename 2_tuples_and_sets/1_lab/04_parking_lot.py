n_iteration = int(input())

parking = set()

current_car = [input().split(", ") for _ in range(n_iteration)]
for command, reg_number in current_car: # unpacking # == current_car[0]
                                                    # == reg_number[1]

    if command == "IN":
        parking.add(reg_number)
    elif command == "OUT":
        parking.remove(reg_number)

if parking:
    [print(reg_number) for reg_number in parking]

else:
    print("Parking Lot is Empty")
