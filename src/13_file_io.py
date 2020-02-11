"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('/Users/mr.ball/Documents/coding/lambda/python/python-intro/Intro-Python-I/src/foo.txt') as f:
    read_data = f.read()
    print(read_data)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
c = open('bar.txt', 'w+')
for i in range(3):
    c.write("Added MORE TEXT WOOOOOAAAH\n ")
c.close()
r = open('/Users/mr.ball/Documents/coding/lambda/python/python-intro/Intro-Python-I/bar.txt', 'r')
print(r.read())


# YOUR CODE HERE
