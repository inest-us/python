# A list comprehension allows you to easily create a list based on some processing or selection criteria
sq_list = []
for x in range(1, 11):
    sq_list.append(x * x)
print(sq_list)  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("Using a list comprehension, we can do this in one step as")
sq_list = [x * x for x in range(1, 11)]
print(sq_list) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

sq_list = [x * x for x in range(1, 11) if x % 2 != 0]
print(sq_list) #[1, 9, 25, 49, 81]

print([ch.upper() for ch in 'comprehension' if ch not in 'aeiou'])
#['C', 'M', 'P', 'R', 'H', 'N', 'S', 'N']