


distance_dict = {
    '99': 3,
    '98': 5,
    '96': 1}

sort_distances = sorted(distance_dict.items(), key=lambda item: item[1])

print(int(sort_distances[0][0]))