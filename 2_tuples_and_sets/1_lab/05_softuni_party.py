def is_vip(number):
    return number[0].isdigit()


vip = set()
regular = set()

type_reservation = int(input())

for _ in range(type_reservation):
    type_reservation = input()

    if is_vip(type_reservation):
        vip.add(type_reservation)
    else:
        regular.add(type_reservation)

while True:
    number = input()
    if number == "END":
        break

    if is_vip(number):
        vip.remove(number)
    else:
        regular.remove(number)

print(len(vip) + len(regular))
[print(number) for number in sorted(vip)]
[print(number) for number in sorted(regular)]
