digits = [0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9] 
digit_set = set( digits) # remove extra 1, 2, 5
print(len(digit_set)) # 10
print(9 in digit_set) #True

odd = {1, 3, 5, 7, 9}
prime = set([ 2, 3, 5, 7])
even = digit_set - odd
print(even) #set([ 0, 8, 2, 4, 6]) 
print(prime & even) # in intersection set([ 2]) 
print(odd | even) # in both set([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(even ^ prime) # not in both set([ 0, 3, 4, 5, 6, 7, 8])

