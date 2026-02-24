# Problem 80
# Sort dictionary by values

data = {"a": 4, "b": 2, "c": 1, "d": 3}

# key=lambda item: item[1] → sort by value (second element)
sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))

print("Dictionary sorted by values:", sorted_dict)