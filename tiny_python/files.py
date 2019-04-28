with open('./tiny_python/names.txt', 'w') as fout:
    fout.write('Paul\r\nJohn\n')
    fout.writelines(['Ringo\n', 'George\n'])

with open('./tiny_python/names.txt') as fin:
    for line in fin:
        print (repr(line))

