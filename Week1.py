#String Methods
myString = "Hello"
myLength = len(myString)

myString2 = 1000
myString3 = str(myString2)
myLength2 =len(myString3)

#Date and Time
today = datetime.now()
print today

print "Length of  %s my string:  , %s" %(myLength, myLength2)

#Loops
name = "sklgsthgkjsjksg"
print("*********" + name[-4] + name[-3] + name[-2] + name[-1])
counter = 0
while counter < 16:
    print name[counter]
    counter = counter + 1

name = "kelly"
count = 0
for letter in name:
    count = count + 1
    print("count is now: " + str(count))
print(count)


