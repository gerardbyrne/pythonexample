# Program Description:     Python Data Conversions
# Author:                             Gerry Byrne
# Date of creation:             15/06/2015 

import sys;	

days = 365;      # 365 days in a year. Let's not worry about leap years
hours = 24;      # 24 hours in a day
minutes = 60;  # 60 minutes in an hour
seconds = 60;  # 60 seconds in a minute



yearseconds = days * hours * minutes * seconds;

print('The number of seconds in a year are: ' + (yearseconds));
print('');

input('Press any key');
