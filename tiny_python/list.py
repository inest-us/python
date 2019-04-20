people = ['Paul', 'John', 'George']
people.append('Ringo')
print('Yoko' in people) #False

for i, name in enumerate(people, 1):
    print('{} - {}'.format(i, name))

print(people[0]) #Paul
print(people[-1]) #len(people) - 1 => Ringgo

print(people[1:2]) #['John']
print(people[:1]) #implicit start at 0 => ['Paul']
print(people[1:]) #['John', 'George', 'Ringo']
print(people[::2])#take every other item ['Paul', 'George']
print(people[::-1]) #reverse sequence
