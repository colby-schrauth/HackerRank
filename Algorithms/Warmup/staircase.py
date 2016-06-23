size = input()

for i in xrange(size):
    new_size = i + 1
    if new_size == size:
        print '#' * new_size
    else:
        print ' ' * (size - new_size) + ('#' * new_size)
