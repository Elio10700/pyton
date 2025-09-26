# Check the frequency of values in a given dictionary

test_dict = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
    "e": 2,
    "f": 1
}

# Create an empty dictionary to store frequency
freq = {}

for value in test_dict.values():
    freq[value] = freq.get(value, 0) + 1

print("The frequency of values is:", freq)
