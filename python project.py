items = ["apple", "banana", "apple", "orange", "banana", "apple"]

freq_map = {}

for item in items:
    if item in freq_map:
        freq_map[item] += 1
    else:
        freq_map[item] = 1

for key, value in freq_map.items():
    print(f"{key}: {value}")
