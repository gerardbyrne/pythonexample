# Program Description:     Python Array Data Structure
# Author:                             Gerry Byrne
# Date of creation:             15/06/2015 

print('');

myNames = ['Gerry', 1990, 'David', 2000, 'Dwyer', 2010];

print('Inserting a member at index 2 - the third item or member');
myNames.insert(2,'Sujatha');


print('');
print('Using an iteration to print all list items');

# Display items in the list.
for theName in myNames:
    print(theName);

print('');
print('Appending a member - that is at the end of the list');
myNames.append('Sarah');

# Display items in the list.
for theName in myNames:
    print(theName);

print('');
print('Removing the member 2000');
myNames.remove(2000);

# Display items in the list.
for theName in myNames:
    print(theName);

print('');
print('Removing the member at index 1');
del myNames[1];

# Display items in the list.
for theName in myNames:
    print(theName);

print('');
print('The number of items in the list is: ', len(myNames));

myClaimValues = [2000, 3000, 5000, 1500, 1900, 1000];

print('');
print('The maximum value in the list is: ', max(myClaimValues));

print('');
print('The minimum value in the list is: ', min(myClaimValues));

print('');
list.sort(myClaimValues);
print('The sorted list is: ', myClaimValues);

print('');
list.reverse(myClaimValues);
print('The sorted list is: ', myClaimValues);
