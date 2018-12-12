# Program Description:     Python Data Conversions
# Author:                             Gerry Byrne
# Date of creation:             15/06/2015

import locale;
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' );

years = 24;
months = 10;
premium = 19.99
ontarget = False;
targetamount = 1000.00;

paidin = ((years * 12) + months) * premium;

print('The total amount that will be paid by the policy holder is £  ', locale.currency(paidin));
print('');

if (paidin >= targetamount):
       ontarget = True;
if (paidin < targetamount):
      ontarget = False;


# Using escape sequences
# So \n means a new line
# So \t means a tab indentation
print('\nIs your policy on target?\t\t\t\t  ' + str(ontarget));

# Using \\ to say print exactly what comes next.
# So \\n means print exactly \n
# So \\t means print exactly \t
print('\\nIs your policy on target?\\t\\t\\t\\t  ' + str(ontarget));
print('');
input('Press any key');

