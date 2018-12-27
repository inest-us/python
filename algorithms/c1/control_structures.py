counter = 1
while counter <= 5:
    print("Hello, world")
    counter = counter + 1

print("------------------------------")
for item in [1,3,6,2,5]:
    print(item)

print("------------------------------")
for item in range(5):
    print(item ** 2)

print("------------------------------")
word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)