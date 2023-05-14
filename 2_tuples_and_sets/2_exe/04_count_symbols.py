text = [x for x in input()]

counter = {}

for el in text:
    if el not in counter:
        counter[el] = 0
    counter[el] += 1

for ch, count in sorted(counter.items()):
    print(f"{ch}: {count} time/s")
