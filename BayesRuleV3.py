# Program Description:     Python Data Arithmetic
# Author:                  Gerry Byrne
# Date of creation:        16/11/2017

'''
One of the famous uses for Bayes Theorem is False Positives and False Negatives.

For these we have two possible cases for "A", such as Pass/Fail (or Yes/No etc)

Example:
            Allergy or Not?

A person tells the doctor they are itchy and are not sure if it an allergy.

    There is a test for Allergy to Cats, but this test is not always right:

        For people that really do have the allergy, the test says "Yes" 80% of the time

        For people that do not have the allergy, the test says "Yes" 10% of the time ("false positive")

    If 1% of the population have the allergy, and the persons test says "Yes", what are the chances
    the pesron really has the allergy?

We want to know the chance of having the allergy when test says "Yes", written P(Allergy|Yes)

Let's get our formula:

P(Allergy|Yes) =	P(Allergy) P(Yes|Allergy)   / P(Yes)

    - P(Allergy) is Probability of Allergy = 1%
    - P(Yes|Allergy) is Probability of test saying "Yes" for people with allergy = 80%
    - P(Yes) is Probability of test saying "Yes" (to anyone) = ??%

Unfortunately we do not what the general chance of the test saying "Yes" is but we can
calculate it by adding up those with and those without the allergy:

    - 1% have the allergy, and the test says "Yes" to 80% of them
    - 99% do not have the allergy and the test says "Yes" to 10% of them

Adding that up we get:

    P(Yes)  = (1% × 80%) + (99% × 10%)
            = 10.7%

Which means that about 10.7% of the population will get a "Yes" result.

So now we can complete our formula:

P(Allergy|Yes)  =	P(Allergy) P(Yes|Allergy)   / P(Yes)
P(Allergy|Yes)  =	    (1%      ×   80%)	   /   10.7
                =   7.48%

P(Allergy|Yes) = about 7%

This is the same result we got on False Positives and False Negatives.

In fact we can write a special version of the Bayes' formula just for things like this:

P(A|B) =	P(A)P(B|A) / P(A)P(B|A) + P(not A)P(B|not A)

'''

https://www.mathsisfun.com/data/bayes-theorem.html


print('')
print('')
print('Example - Allery or not!')

probabilityOfAllergy                    = 0.1;
probabilityOfYesWhenThereIsAnAllergy    = 0.8;
probabilityOfCloud = 0.4;

probabilityOfNotAllergy                 = 0.1;
probabilityOfYesWhenNotAlergy           = 0.2;


probabilityOfYes =  (probabilityOfAllergy * probabilityOfYesWhenThereIsAnAllergy) + (probabilityOfAllergy * probabilityOfYesWhenThereIsAnAllergy) + (probabilityOfNotAllergy * probabilityOfYesWhenNotAlergy);


probabilityOfAllergyWhenThereIsYes =  (probabilityOfAllergy * probabilityOfYesWhenThereIsAnAllergy) / (probabilityOfAllergy * probabilityOfYesWhenThereIsAnAllergy) + (probabilityOfNotAllergy * probabilityOfYesWhenNotAlergy);

print('In this example ' + str(float(probabilityOfAllergyWhenThereIsYes)) + ' is the chance of an allergy when saying yes');

percentageOfFireWhenThereIsSmoke =  "{0:.1f}%".format(probabilityOfAllergyWhenThereIsYes * 100);

print('In this example ' + percentageOfFireWhenThereIsSmoke + ' of the time we would expect rain');
