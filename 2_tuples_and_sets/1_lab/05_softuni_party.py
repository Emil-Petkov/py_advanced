def is_vip(guest):
    return guest[0].isdigit()

n_people = int(input())

vip_set = set()
regular_set = set()

for _ in range(n_people):
    reservation = input()

    if is_vip(reservation):
        vip_set.add(reservation)
    else:
        regular_set.add(reservation)


while True:
    guest = input()
    if guest == "END":
        break

    if is_vip(guest):
        vip_set.remove(guest)
    else:
        regular_set.remove(guest)

print(len(vip_set) + len(regular_set))
[print(guest) for guest in sorted(vip_set)]
[print(guest) for guest in sorted(regular_set)]

