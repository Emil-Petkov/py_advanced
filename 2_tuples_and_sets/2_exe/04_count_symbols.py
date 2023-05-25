text = input()

dict = {}

for el in text:
    if el not in dict:
        dict[el] = 0
    dict[el] += 1

for k in sorted(dict):
    print(f"{k}: {dict[k]} time/s")
