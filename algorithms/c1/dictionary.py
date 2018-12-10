capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals) # {'Wisconsin': 'Madison', 'Iowa': 'DesMoines'}

# We can manipulate a dictionary by accessing a value via its key or by adding another key-value pair. 
# The syntax for access looks much like a sequence access 
# except that instead of using the index of the item we use the key value. To add a new value is similar.

print(capitals['Iowa']) # DesMoines
capitals['Utah']='SaltLakeCity'
print(capitals) # {'Iowa': 'DesMoines', 'Wisconsin': 'Madison', 'Utah': 'SaltLakeCity'}

capitals['California']='Sacramento'
print(len(capitals)) # 4

for k in capitals:
    print(capitals[k], " is the capital of ", k)

phone_ext={'david':1410, 'brad':1137}
print(phone_ext)  # {'brad': 1137, 'david': 1410}
print(phone_ext.keys()) # dict_keys(['brad', 'david'])
print(list(phone_ext.keys())) # ['brad', 'david']

print("brad" in phone_ext) # True
print(1137 in phone_ext) # False : 1137 is not a key in phone_ext

print(phone_ext.values()) # dict_values([1137, 1410])
print(list(phone_ext.values())) # [1137, 1410]

print(phone_ext.items()) # dict_items([('brad', 1137), ('david', 1410)])
print(list(phone_ext.items())) # [('brad', 1137), ('david', 1410)]

print(phone_ext.get("kent")) # None
print(phone_ext.get("kent","NO ENTRY")) # 'NO ENTRY'
del phone_ext["david"]
print(phone_ext) # {'brad': 1137}