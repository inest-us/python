my_list = [1,3,True,6.5]
print(my_list) # [1,3,True,6.5]

my_list = [0] * 6
print(my_list) # [0, 0, 0, 0, 0, 0]

my_list = [1,2,3,4]
# The variable A holds a collection of three references to the original list called my_list. 
# Note that a change to one element of my_list shows up in all three occurrences in A.
A = [my_list]*3 
print(A) # [[1,2,3,4], [1,2,3,4], [1,2,3,4]]

my_list[2]=45
print(A) # [[1,2,45,4], [1,2,45,4], [1,2,45,4]]