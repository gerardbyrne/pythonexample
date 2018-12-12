# Program Description:     Python Array Data Structure
# Author:                             Gerry Byrne
# Date of creation:             15/06/2015 

from array import *

print('');

myScores = array('i',[10,20,30,40]);
print(myScores);
print('Inserting a member at index 2 - the third item or member');
myScores.insert(2,25);

# Display numbers in the array.
for theScore in myScores:
    print(theScore);


print('');
print('Appending a member - that is at the end of the array');
myScores.append(90);

# Display numbers in the array.
for theScore in myScores:
    print(theScore);


print('');
print('Removing the member 30');
myScores.remove(30);

# Display numbers in the array.
for theScore in myScores:
    print(theScore);

print('');
print('The number of items in the array is: ', len(myScores));

mySalaries = array([20000,30000,40000,50000], type = UInt32);
print(mySalaries[0]);
print(mySalaries[1]);

# Display numbers in the array.
for theSalaries in mySalaries:
    print(theSalaries);
