# Create variable 'x'
# Accept user input as a string and convert all characters to lowercase
x = str(raw_input().lower())

# Create variable 'y'
# Convert user inputted string ('x') to a list, separating each character, and remove all duplicate characters with the function
y = list(set(x))

# Including the space character (' '), count the length of our unique list ('y') and print results
if len(y) == 27:
    print 'pangram'
else:
    print 'not pangram'
