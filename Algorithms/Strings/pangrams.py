x = str(raw_input().lower())
y = list(set(x))

if len(y) == 27:
    print 'pangram'
else:
    print 'not pangram'
