# Problem 79
# Sort dictionary by keys

data = {"b": 2, "a": 1, "d": 4, "c": 3}

# sorted() sorts dictionary items by key by default
sorted_dict = dict(sorted(data.items()))

print("Dictionary sorted by keys:", sorted_dict)