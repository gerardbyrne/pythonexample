# Program Description:     Python Data For Diabetes Example
# Author:                  Gerry Byrne
# Date of creation:        16/11/2017
# Reference:	https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
# Example
'''
    The Naive Bayes algorithm is an intuitive method that uses the
    probabilities of each attribute belonging to each class to make a prediction.
    It is the supervised learning approach you would come up with if you wanted
    to model a predictive modeling problem probabilistically.

    Naive bayes simplifies the calculation of probabilities by assuming that the
    probability of each attribute belonging to a given class value is independent
    of all other attributes. This is a strong assumption but results in a fast and effective method.

    The probability of a class value given a value of an attribute is called the conditional probability.
    By multiplying the conditional probabilities together for each attribute for a given class value,
    we have a probability of a data instance belonging to that class.

    To make a prediction we can calculate probabilities of the instance belonging to each class and select
    the class value with the highest probability.

    Naive bases is often described using categorical data because it is easy to describe and calculate using ratios.
    A more useful version of the algorithm for our purposes supports numeric attributes and assumes the values of
    each numerical attribute are normally distributed (fall somewhere on a bell curve).
    Again, this is a strong assumption, but still gives robust results.

    THE PROBLEM DEFINITION

    Predict the Onset of Diabetes

    The test problem we will use in this tutorial is the Pima Indians Diabetes problem.

    This problem is comprised of 768 observations of medical details for Pima indians patents.

    The records describe instantaneous measurements taken from the patient such as their age, the number of times
    pregnant and blood workup.

    All patients are women aged 21 or older.

    All attributes are numeric, and their units vary from attribute to attribute.

    Each record has a class value that indicates whether the patient suffered an onset of diabetes within 5 years
    of when the measurements were taken (1) or not (0).

    This is a standard dataset that has been studied a lot in machine learning literature.

    A good prediction accuracy is 70%-76%.

    Below is a sample from the pima-indians.data.csv file to get a sense of the data we will be working with.

    6,148,72,35,0,33.6,0.627,50,1
    1,85,66,29,0,26.6,0.351,31,0
    8,183,64,0,0,23.3,0.672,32,1
    1,89,66,23,94,28.1,0.167,21,0
    0,137,40,35,168,43.1,2.288,33,1

    Naive Bayes Algorithm Tutorial

    This tutorial is broken down into the following steps:

    Handle Data:        Load the data from CSV file and split it into training and test datasets.
    Summarize Data:     summarize the properties in the training dataset so that we can calculate probabilities and make predictions.
    Make a Prediction:  Use the summaries of the dataset to generate a single prediction.
    Make Predictions:   Generate predictions given a test dataset and a summarized training dataset.
    Evaluate Accuracy:  Evaluate the accuracy of predictions made for a test dataset as the percentage correct out of all predictions made.
    Tie it Together:    Use all of the code elements to present a complete and standalone implementation of the Naive Bayes algorithm.
'''

###################################################################
#                    1. Handle Data                               #
# The first thing we need to do is load our data file.
# The data is in CSV format without a header line or any quotes.
# We can open the file with the open function and read the data
# lines using the reader function in the csv module.

# We also need to convert the attributes that were loaded as
# strings into numbers that we can work with them.
# The code below is the loadCsv() function that is usesd for
# loading the Pima indians dataset.
#
###################################################################

import csv
def loadCsv(filename):
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

filename = 'pima-indians-diabetes.csv'
dataset = loadCsv(filename)
print('Loaded data file', filename, 'with ' , len(dataset))


###################################################################
# Next we need to split the data into a training dataset that
# Naive Bayes can use to make predictions and a test dataset that
# we can use to evaluate the accuracy of the model.
# We need to split the data set randomly into train and datasets
# with a ratio of 67% train and 33% test (this is a common ratio
# for testing an algorithm on a dataset).Below is the
# splitDataset() function that will split a given dataset
# into a given split ratio.
###################################################################

import random
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

###################################################################
# We can test this out by defining a mock dataset with 5
# instances, split it into training and testing datasets and
# print them out to see which data instances ended up where.
###################################################################

dataset = [[1], [2], [3], [4], [5]]
splitRatio = 0.67
train, test = splitDataset(dataset, splitRatio)
print('Split ',  len(dataset), 'rows into train with ',train, 'and test with ', test)


###################################################################
#                 2. Summarise Data                               #
# The Naive Bayes model is comprised of a summary of the data in
# the training dataset. This summary is then used when making
# predictions.
# The summary of the training data collected involves the mean
# and the standard deviation for each attribute, by class value.
# For example, if there are two class values and 7 numerical
# attributes, then we need a mean and standard deviation for
# each attribute (7) and class value (2) combination,
# that is 14 attribute summaries.
#
# These are required when making predictions to calculate the
# probability of specific attribute values belonging to each
# class value.We can break the preparation of this summary data
# down into the following sub-tasks:
# 	Separate Data By Class
# 	Calculate Mean
# 	Calculate Standard Deviation
# 	Summarize Dataset
# 	Summarize Attributes By Class
# 	Separate Data By Class
#
# The first task is to separate the training dataset instances
# by class value so that we can calculate statistics for each
# class. We can do that by creating a map of each class value
# to a list of instances that belong to that class and sort
# the entire dataset of instances into the appropriate lists.
#
# The separateByClass() function below achieves this.
#
###################################################################


def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated

dataset = [[1,20,1], [2,21,0], [3,22,1]]
separated = separateByClass(dataset)
print('Separated instances: ', separated)


###################################################################
# CALCULATE MEAN
# We need to calculate the mean of each attribute for a class value.
# The mean is the central middle or central tendency of the data,
# and we will use it as the middle of our gaussian distribution
# when calculating probabilities.
#
# We also need to calculate the standard deviation of each attribute
# for a class value. The standard deviation describes the variation
# of spread of the data, and we will use it to characterise the
# expected spread of each attribute in our Gaussian distribution
# when calculating probabilities.
#
# The standard deviation is calculated as the square root of the
# variance. The variance is calculated as the average of the
# squared differences for each attribute value from the mean.
# Note we are using the N-1 method, which subtracts 1 from the
# number of attribute values when calculating the variance.
###################################################################


import math
def mean(numbers):
	return sum(numbers)/float(len(numbers))

def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

numbers = [1,2,3,4,5]
print('Summary of ', numbers, 'mean= ', mean(numbers), 'stdev = ', stdev(numbers))


###################################################################
# SUMMARISE DATASET
# Now we have the tools to summarize a dataset. For a given list of
# instances (for a class value) we can calculate the mean and the
# standard deviation for each attribute.The zip function groups
# the values for each attribute across our data instances into
# their own lists so that we can compute the mean and standard
# deviation values for the attribute.
###################################################################

def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries

'''
We can test this summarize() function with some test data that shows 
markedly different mean and standard deviation values for the first 
and second data attributes.
'''

dataset = [[1,20,0], [2,21,1], [3,22,0]]
summary = summarize(dataset)
print('Attribute summaries: ', summary)

'''
Summarize Attributes By Class

We can pull it all together by first separating our training dataset 
into instances grouped by class. Then calculate the summaries for 
each attribute.
'''

def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.items():
		summaries[classValue] = summarize(instances)
	return summaries

'''
We can test this summarizeByClass() function with a small test dataset
'''

dataset = [[1,20,1], [2,21,0], [3,22,1], [4,22,0]]
summary = summarizeByClass(dataset)
print('Summary by class value: ', summary)