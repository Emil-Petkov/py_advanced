unique_cars = set()

for _ in range(int(input())):
    current_car = input().split(", ")
    command = current_car[0]
    car_number = current_car[1]

    if command == "IN":
        unique_cars.add(car_number)
    elif command == "OUT":
        unique_cars.remove(car_number)

if unique_cars:
    [print(car_number) for car_number in unique_cars]

else:
    print("Parking Lot is Empty")

    
