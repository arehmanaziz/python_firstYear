# save variables in file, then use open function to call them,
# open(a, b)
# a = path of the file,
# b = read "r" -OR- write "w"
# path = F:\Programing\Python Work\University Work\save variables\demo.txt
# it will give us an error b/c value after TAB "/" represents a special character like, /n means new line, /t space
# so, we have to give DOUBLE TAB "//".

f = open('/save variables/demo.txt', "w")

# write now our txt file is empty, to write something in it, we will use write method
f.write("Last session is in progress.\n")
# Last session is in progress.
# now our file contain this line

f.write("Second statement is being written.\n")
# Second statement is being written.


# write character does not write on new lines like print function.
#  to do that we have to enter new line character or change it using notepad or other software.
f.write("This should be the third line.")
# This should be the third line.




# these line are logically written in txt file, but operating system does not save this one by one in hard disk
# b/c it's slower process. So, OS saves it in a place in RAM, called "BUFFER".The minimum size of BUFFER is 512 bytes.
# The size of BUFFER can be bigger, depending on the OS you're using. and when it has the data of that size or in case
# of IntelliJ or VS Code, when we run the code, it writes it on the file.
# it also write it when we use the close method [.close()] to close the file.


f.close()
# always close files after using


g = open('/save variables/demo.txt', "r")
print(g.read(10))
# Last session
# now it will read next 10 characters
print(g.read(10))
# on is in p
# now it will read next 10 characters
print(g.read(10))
# rogressSec
print(g.read(50))
# ond statement is being writtenThis should be the t
print(g.read())
# if we don't give a value in read(), it will read the line from where it has to read till the end.
# hird line.
g.close()
g = open('/save variables/demo.txt', "r")
print(g.read())
# we have reopen the file. read() has an internal pointer and saves how much it has read and start reading from where it has left
# Last session is in progressSecond statement is being writtenThis should be the third line.

# it reads from the pointer till the end of the line.
print(g.readline())
# Last session is in progress.
# Second statement is being written.
# This should be the third line.
g.close()
g = open('/save variables/demo.txt', "r")

print(g.readline(10)) # it will behave like g.read(10) bcz there is no. b/w parenthesis
# Last sessi

g.close()
g = open('/save variables/demo.txt', "r")

print(g.readlines())
# it will print every line as an element of a list.
# ['Last session is in progress.\n', 'Second statement is being written.\n', 'This should be the third line.']

# we can also save all these methods in a variable
g.close()
g = open('/save variables/demo.txt', "r")



a = g.readlines()
g.close()
g = open('/save variables/demo.txt', "r")
b = g.read(10)
c = g.readline()
print(a, b, c, sep = "\n")
# ['Last session is in progress.\n', 'Second statement is being written.\n', 'This should be the third line.']
# Last sessi
# on is in progress.

# a is a list
print(type(a))
for i in a:
    b = i.split(" ")  # w.r.t space
    print(b)
# <class 'list'>
# ['Last', 'session', 'is', 'in', 'progress.\n']
# ['Second', 'statement', 'is', 'being', 'written.\n']
# ['This', 'should', 'be', 'the', 'third', 'line.']

# for i in a:
#     b = i.split(",")  w.r.t ","
#     print(b)
# ['Last session is in progress.\n']
# ['Second statement is being written.\n']
# ['This should be the third line.']


# we can also open csv format files
# s = open('F:\\Programing\\Python Work\\University Work\\save variables\\demo 2.csv', "r")
# print(s.read())
# print(s.readlines())
# s.close()

# we can also open html files (b/c they are pure text files) by copying the webpage and open into notepad.

# we want to write csc file in html file. so we have to open both files

h = """
<html>
<head>
</head>
<body>
<table>
<tr><td>x</td> <td>y</td></tr>
</table>
</body>
</html>
"""

a = open('/save variables/abc.html', "w")
b = open('/save variables/demo 2.csv', "r")

c = b.readlines()
for i in c[1:]:
    z = i.split(",")
    x = int(z[0])
    y = int(z[1])
    print(x, y)
    a.write("<tr><td>{0}</td> <td>{1}</td></tr>".format(x,y))