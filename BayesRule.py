# Program Description:     Python Data Arithmetic
# Author:                  Gerry Byrne
# Date of creation:        16/11/2017

# Example 1
# Suppose we have 2 people Chris and Sarah who both send emails
# By analysing their previous emails we can see that their word
# useage is as follows.

#              Chris     Sarah
# Love          0.1     0.5
# Deal          0.8     0.2
# Life          0.1     0.3

# Suppose now that an email has the words Life and Deal in it
# But we do not know who sent it. How can we find out?
# We could use Bayes rule.
# One key to understanding the essence of Bayes' theorem is to
# recognize that we are dealing with sequential events, whereby
# new additional information is obtained for a subsequent event,
# and that new information is used to revise the probability of
# the initial event. In this context, the terms prior probability
# and posterior probability are commonly used.


print('')
print('')
print('Example 1')
probabilityThatChrisUsesLove = 0.1;
probabilityThatChrisUsesDeal = 0.8;
probabilityThatChrisUsesLife = 0.1;

probabilityThatSarahUsesLove = 0.5;
probabilityThatSarahUsesDeal = 0.2;
probabilityThatSarahUsesLife = 0.3;

priorProbabilityOfChrisOrSarah =  0.5;


probabilityThatEmailWasFromChris = probabilityThatChrisUsesLife * probabilityThatChrisUsesDeal * priorProbabilityOfChrisOrSarah;
probabilityThatEmailWasFromSarah = probabilityThatSarahUsesLife * probabilityThatSarahUsesDeal * priorProbabilityOfChrisOrSarah;


totalOfProbabilities = probabilityThatEmailWasFromChris + probabilityThatEmailWasFromSarah;


posteriorProbabilityForChris = probabilityThatEmailWasFromChris / totalOfProbabilities;
posteriorProbabilityForSarah = probabilityThatEmailWasFromSarah / totalOfProbabilities;


totalOfPosteriorProbabilities = posteriorProbabilityForChris + posteriorProbabilityForSarah;


print('Posterior probability for Chris is ' + str(float(posteriorProbabilityForChris)));
print('Posterior probability for Sarah is ' + str(float(posteriorProbabilityForSarah)));

print('Posterior probability should add up to 1. The actual total is: ' + str(float(totalOfPosteriorProbabilities)));


print('')
print('')
print('Example 2')
# Example 2
# Suppose we have a second email with the words Love and Deal in it
# But we do not know who sent it. How can we find out?
# We could use Bayes rule.

probabilityThatEmailWasFromChris = probabilityThatChrisUsesLove * probabilityThatChrisUsesDeal * priorProbabilityOfChrisOrSarah;
probabilityThatEmailWasFromSarah = probabilityThatSarahUsesLove * probabilityThatSarahUsesDeal * priorProbabilityOfChrisOrSarah;


totalOfProbabilities = probabilityThatEmailWasFromChris + probabilityThatEmailWasFromSarah;


posteriorProbabilityForChris = probabilityThatEmailWasFromChris / totalOfProbabilities;
posteriorProbabilityForSarah = probabilityThatEmailWasFromSarah / totalOfProbabilities;


totalOfPosteriorProbabilities = posteriorProbabilityForChris + posteriorProbabilityForSarah;


print('Posterior probability for Chris is ' + str(float(posteriorProbabilityForChris)));
print('Posterior probability for Sarah is ' + str(float(posteriorProbabilityForSarah)));

print('Posterior probability should add up to 1. The actual total is: ' + str(float(totalOfPosteriorProbabilities)));