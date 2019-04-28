from collections import namedtuple 
Member = namedtuple('Member', 'name, instrument, birth_year') 
member3 = Member(' George', 'Guitar', 1943) 

#We can access members by position or name (name allows us to be more explicit): 
print(member3[0]) #'George'
print(member3.name) #'George'

