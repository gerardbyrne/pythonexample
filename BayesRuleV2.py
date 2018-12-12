# Program Description:     Python Data Arithmetic
# Author:                  Gerry Byrne
# Date of creation:        16/11/2017

'''
You are planning a picnic today, but the morning is cloudy

- 50% of all rainy days start off cloudy!
- But cloudy mornings are common (about 40% of days start cloudy)
- And this is usually a dry month (only 3 of 30 days tend to be rainy, or 10%)
- What is the chance of rain during the day?

We will use Rain to mean rain during the day, and Cloud to mean cloudy morning.

The chance of Rain given Cloud is written P(Rain|Cloud)

So let's put that in the formula:


P(Rain|Cloud) =	P(Rain) P(Cloud|Rain)   /   P(Cloud)

P(Rain) is Probability of Rain = 10%

P(Cloud|Rain) is Probability of Cloud, given that Rain happens = 50%

P(Cloud) is Probability of Cloud = 40%

P(Rain|Cloud)   =	0.1 x 0.5   /   0.4
	            = .125

Or a 12.5% chance of rain.

Think of the formula as

"AB AB AB" then remember to group it like: "AB = A BA / B"

P(A|B) =	P(A) P(B|A) /   P(B)

'''


print('')
print('')
print('Example - Picnic Weather')
probabilityOfRain = 0.1;
probabilityOfCloudWhenThereIsRain = 0.5;
probabilityOfCloud = 0.4;


probabilityOfRainWhenThereIsCloud =  (probabilityOfRain * probabilityOfCloudWhenThereIsRain) / probabilityOfCloud;

print('In this example ' + str(float(probabilityOfRainWhenThereIsCloud)) + ' is the chance of rain');

percentageOfFireWhenThereIsSmoke =  "{0:.1f}%".format(probabilityOfRainWhenThereIsCloud * 100);

print('In this example ' + percentageOfFireWhenThereIsSmoke + ' of the time we would expect rain');
