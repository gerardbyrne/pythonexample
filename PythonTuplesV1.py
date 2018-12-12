# Program Description:     Python Tuple Data Structure
# Author:                             Gerry Byrne
# Date of creation:             15/06/2015

print('');
myNames = ('Gerry', 1990, 'David', 2000, 'Dwyer', 2010);
print(myNames);

print('');
print('Using an iteration to print all list items');

# Display numbers in the array.
for theName in myNames:
    print(theName);

print('');
print('The number of items in the tuple is: %d' % len(myNames));

myClaimValues = (2000, 3000, 5000, 1500, 1900, 1000);

print('');
print('The maximum value in the tuple is: %d' % max(myClaimValues));

print('');
print('The minimum value in the tuple is: %d' % min(myClaimValues));

print('');
print('The sorted tuple in ascending order is: ' , sorted(myClaimValues));

print('');
print('The sorted tuple in descending order is: ' , sorted(myClaimValues, reverse=True));

myNames1 = ('Gerry', 1990, 'David', 2000, 'Dwyer', 2010);
myNames2 = ('Gerry', 1990, 'David', 2000, 'Dwyer', 2010);

print('');
print("The comparison of the tuples says: %d" % cmp(myNames1, myNames2));
