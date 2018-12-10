# Tuples are very similar to lists in that they are heterogeneous sequences of data. 
# The difference is that a tuple is immutable, like a string. 
# A tuple cannot be changed. 
# Tuples are written as comma-delimited values enclosed in parentheses. 
my_tuple = (2,True,4.96)
print(my_tuple) # (2, True, 4.96)
print(len(my_tuple)) # 3
print(my_tuple[0]) # 2
print(my_tuple * 3) # (2, True, 4.96, 2, True, 4.96, 2, True, 4.96)
print(my_tuple[0:2]) # (2, True)

# my_tuple[1]=False
# Traceback (most recent call last):
# File "<pyshell#137>", line 1, in <module>
# my_tuple[1]=False
# TypeError: 'tuple' object does not support item assignment