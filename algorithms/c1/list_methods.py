my_list = [1024, 3, True, 6.5]
my_list.append(False)
print(my_list) # [1024, 3, True, 6.5, False]

my_list.insert(2,4.5)
print(my_list) # [1024, 3, 4.5, True, 6.5, False]

# pop will default to the end of the list but can also remove and return a specific item
print(my_list.pop()) # False
print(my_list) # [1024, 3, 4.5, True, 6.5]
print(my_list.pop(1)) # 3
print(my_list) # [1024, 4.5, True, 6.5]

my_list.pop(2)
print(my_list) # [1024, 4.5, 6.5]
my_list.sort() 
print(my_list) # [4.5, 6.5, 1024]

my_list.reverse()
print(my_list) # [1024, 6.5, 4.5]
print(my_list.count(6.5)) # 1
print(my_list.index(4.5)) # 2

my_list.remove(6.5) 
print(my_list) # [1024, 4.5]
del my_list[0]
print(my_list) # [4.5]

print ((54).__add__(21))