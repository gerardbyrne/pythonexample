# Program Description:     Python Data Arithmetic
# Author:                  Gerry Byrne
# Date of creation:        16/11/2017

'''
Bayes’ Theorem is a way of finding a probability when we know certain other probabilities.

The formula is:

P(A|B) =	P(A) P(B|A)/    P(B)

It tells us how often A happens given that B happens, written P(A|B),
when we know how often B happens given that A happens, written P(B|A) ,
and how likely A and B are on their own.

- P(A|B) is "Probability of A given B", the probability of A given that B happens
- P(A) is Probability of A
- P(B|A) is "Probability of B given A", the probability of B given that A happens
- P(B) is Probability of B


Example
When P(Fire) means how often there is fire and P(Smoke) means how often we see smoke, then:

P(Fire|Smoke) means how often there is fire when we see smoke.

P(Smoke|Fire) means how often we see smoke when there is fire.


Example
If dangerous fires are rare (1%) but smoke is fairly common (10%)
and 90% of dangerous fires make smoke then:

P(Fire|Smoke)   =	P(Fire) P(Smoke|Fire) / P(Smoke)
                =	1% x 90%	/  10%
                =   9%

In this case 9% of the time expect smoke to mean a dangerous fire.
'''


print('')
print('')
print('Example - Fire and Smoke')
probabilityOfFire = 0.01;
probabilityOfSmokeWhenThereIsAFire = 0.9;
probabilityOfSmoke = 0.1;


probabilityOfFireWhenThereIsSmoke =  (probabilityOfFire * probabilityOfSmokeWhenThereIsAFire) / probabilityOfSmoke;

print('In this example ' + str(float(probabilityOfFireWhenThereIsSmoke)) + ' of the time we would expect smoke to mean a dangerous fire');

percentageOfFireWhenThereIsSmoke =  "{0:.0f}%".format(probabilityOfFireWhenThereIsSmoke * 100);

print('In this example ' + percentageOfFireWhenThereIsSmoke + ' of the time we would expect smoke to mean a dangerous fire');
