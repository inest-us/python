# A set is an unordered collection of zero or more immutable Python data objects. 
# Sets do not allow duplicates and are written as comma-delimited values enclosed in curly braces. 
# The empty set is represented by set(). Sets are heterogeneous

my_set = {3,6,"cat",4.5,False}
print(my_set) # {False, 3, 4.5, 6, 'cat'}

# Eventhough sets are not considered to be sequential, they do support a few of the familiar
# operations presented earlier. T

print(len(my_set)) # 5
print(False in my_set) # True
print("dog" in my_set) # False

your_set = {99,3,100}
print(my_set.union(your_set)) # {False, 3, 4.5, 6, 99, 'cat', 100}
print(my_set | your_set) # {False, 3, 4.5, 6, 99, 'cat', 100}

print(my_set.intersection(your_set)) # {3}
print(my_set & your_set) # {3}

print(my_set.difference(your_set)) # {False, 4.5, 6, 'cat'}
print(my_set - your_set) # {False, 4.5, 6, 'cat'}
print({3,100}.issubset(your_set)) # True
print({3,100} <= your_set) # True

my_set.add("house")
print(my_set) # {False, 3, 4.5, 6, 'house', 'cat'}
my_set.remove(4.5)
print(my_set) # {False, 3, 6, 'house', 'cat'}
print(my_set.pop()) #False
print(my_set) # {3, 6, 'house', 'cat'}
my_set.clear()
print(my_set) # set()