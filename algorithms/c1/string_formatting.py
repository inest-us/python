print("Hello") # Hello
print("Hello","World") # Hello World
print("Hello","World", sep="***") # Hello***World
print("Hello","World", end="***") # Hello World***
print("Hello", end="***"); print("World") # Hello***World

name = "Tom"
age = 20
print("%s is %d years old." % (name, age))

price = 24
item = "banana"
print("The %s costs %d cents"%(item,price)) #The banana costs 24 cents
print("The %+10s costs %5.2f cents"%(item,price)) #The     banana costs 24.00 cents
print("The %+10s costs %10.2f cents"%(item,price)) #The     banana costs      24.00 cents

item_dict = {"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents"%item_dict) #The banana costs    24.0 cents