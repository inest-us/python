instruments = {
    'Paul': 'Bass',
    'John': 'Guitar'
}

instruments['George'] = 'Guitar'
print('Ringo' in instruments) # False

for name in instruments:
    print('{} - {}'.format(name, instruments[name]))