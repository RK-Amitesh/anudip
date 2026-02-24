# Problem 65
# Find mode of a list

# Taking input from user
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Check if list is empty
if len(numbers) == 0:
    print("List is empty. Cannot find mode.")

else:
    # Create dictionary to store frequency
    frequency = {}

    # Count occurrences
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find maximum frequency
    max_frequency = max(frequency.values())

    # Find all elements with max frequency
    modes = []

    for key, value in frequency.items():
        if value == max_frequency:
            modes.append(key)

    print("Mode(s):", modes)
    print("Frequency:", max_frequency)