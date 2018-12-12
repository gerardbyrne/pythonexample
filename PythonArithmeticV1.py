# Program Description:     Python Data Arithmetic
# Author:                           Gerry Byrne
# Date of creation:             15/06/2015 

import math;

print('');
numberOne = input('Enter the first number:  ');

print('');
numberTwo = input('Enter the second number:  ');

answer = int(numberOne) // int(numberTwo);

print('');
print('Number one is ' + numberOne + ' whilst number two is ' + numberTwo + ' and the total is ' + str(int(numberOne) + int(numberTwo)));
print(answer);

answer = math.sqrt(int(numberOne));

print('');
print('The square root of Number one gives a value of:  ', answer);

answer /= 10;

print('');
print('The square root of Number one plus 10 gives a value of:  ', answer);
