# Generate all the permutations from a list of numbers [1, 2, 3] N times
import itertools

totalBags = 2
items = ['apple', 'computer', 'gun', 'dildo']
for combination in itertools.product(list(range(totalBags + 1)), repeat = len(items)):
    bagsContent = [0] * totalBags
    for element in combination:
        bagsContent[element]
    print(combination)
