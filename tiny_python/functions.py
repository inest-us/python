add = lambda x, y: x + y 
print(add(4, 5))

def add_n(x, n = 42): 
    return x + n

print(add_n(10)) # 52 
print(add_n(3, -10)) # -7

def add_many(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(add_many()) # 0
print(add_many(1)) # 1
print(add_many(1, 2, 3, 4, 5)) # 15

def add_kwargs(**kwargs):
    result = 0
    for key in kwargs:
        result += kwargs[key]
    return result

print(add_kwargs(x = 1, y = 2, z = 3)) # 6
print(add_kwargs()) # 0

def add_all(* args, ** kwargs):
    """ Add all arguments"""
    result = 0
    for num in args + tuple(kwargs.values()):
        result += num
    return result

sizes = (2, 4.5)
named_sizes = {"this": 3, "that": 1}
print(add_all(* sizes)) #6.5
print(add_all(sizes[0], sizes[1])) # 6.5 

print(add_all(** named_sizes)) # 4 
print(add_all(this = 3, that = 1)) # 4 

#You can also combine * and ** on invocation:
print(add_all(* sizes, ** named_sizes)) # 10.5

