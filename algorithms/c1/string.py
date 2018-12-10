my_name = "David"
print(my_name[3])

print(my_name*2) # 'DavidDavid'
print(len(my_name)) # 5

print(my_name.upper()) # 'DAVID'
print(my_name.center(10)) # ' David '
print(my_name.find('v')) # 2
print(my_name.split('v')) # ['Da', 'id']

# A major difference between lists and strings is that lists can be modified while strings cannot.
# This is referred to as mutability. Lists are mutable; strings are immutable.

my_list = [1, 3, True, 6.5]
my_list[0]=2**10
print(my_list) # [1024, 3, True, 6.5]

# my_name[0]='X'
# Traceback (most recent call last):
# File "<pyshell#84>", line 1, in <module>
# my_name[0]='X'
# TypeError: 'str' object does not support item assignment