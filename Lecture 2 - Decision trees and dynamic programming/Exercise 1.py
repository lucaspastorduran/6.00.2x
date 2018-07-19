from Item import *

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i (binary shift lets the binary bit in pos 0)
            # if is 'par' last number is 0, if not is 1.
            # we are generatin binary numbers from 0 to 2**N
            if (i >> j) % 2 == 1:
                # if position j is '1', append item j
                combo.append(items[j])
        yield combo
        

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    # Choose element all the elements that will be in bag A
    combinations = 0
    for bag1_elem in powerSet(items):
        # Choose elements that will be in bag B from the remaining ones
        remaining_elem = list(set(items) - set(bag1_elem))
        print('For bag1 = {}. We have remaining elements: {}'.format(bag1_elem, remaining_elem))
        for bag2_elem in powerSet(remaining_elem):
            yield (bag1_elem, bag2_elem)
            combinations += 1
    print('Returned {} from {} combinations'.format(combinations, 3**len(items)))
    

def comboToString(Items_list):
    return str([str(objectInBag) for objectInBag in Items_list])

def printCombos(objects_combo):
    n = len(objects_combo)
    objects_str = ''
    for index, objectInBag in enumerate(objects_combo):
        objects_str += 'Bag {}: {}, '.format(index, comboToString(objectInBag))
    print(objects_str)
    

print('Testing powerSet for [1,2,3]:')
for number in powerSet([1,2,3]):
    print (number)

print('\nTesting yieldAllCombos for [1,2,3]:')
for combo in yieldAllCombos([1,2,3]):
    print(combo)

definedItems = buildItems()
print(definedItems)
print('\nTesting Item for: ', comboToString(definedItems))
for combo in yieldAllCombos(definedItems):
    printCombos(combo)

for N in [0, 2, 3]:
    bag_objects = buildRandomItems(N)
    print('\nTesting yieldAllCombos for {}:'.format(comboToString(bag_objects)))
    for objects_combo in yieldAllCombos(bag_objects):
        printCombos(objects_combo)
