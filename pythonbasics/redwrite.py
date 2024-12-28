file = open('../test.txt') #read all the content of file
# print(file.read())
# print(file.read(5))
# print(file.readline())
# print(file.readline())

# print line by line using readline

# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()
# when you will use readlines instud of readline , list will be created

# print(file.readlines())

# loop to get line by line text
for line in file.readlines():
    print(line)


file.close()
