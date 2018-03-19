# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    naive_bayes.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerard <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/18 10:39:09 by dgerard           #+#    #+#              #
#    Updated: 2018/03/18 19:17:24 by dgerard          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3

import csv
import random
import math

def summarize(dataset):
    summaries = [(get_mean(attribute), get_stdev(attribute)) for attribute in zip(*dataset)]
    #zip() takes lists, and reorganizes the elements by "column" or subindex instead of by "row" or index
    #ie IF parameter lists = a=['cat', 'dog'] b=['aloof','floof'] THEN result lists = [('cat', 'aloof'), ('dog', 'floof)]
    del summaries[-1]
    return summaries

def get_mean(numbers):
    return sum(numbers)/float(len(numbers))
    #sum(iterable, start) returns the sum of all items from the given iterable, start is zero if not given

def get_stdev(numbers):
    average = get_mean(numbers)
    variance = sum([pow(x - average, 2) for x in numbers]) / float(len(numbers)-1)
    return math.sqrt(variance)
    #stdev = sqrt(sum of(each value in data set - mean of all values in data set)^2 / the number of values in the dataset)

def separate_by_class(dataset):
    separados = {}
    #declare separados as an empty dictionary, a data type that is like a list but has keys instead of index, like php array
    for i in range(len(dataset)):
        data_line = dataset[i]
        #set data_line as equal to each line of the dataset as you iterate through dataset
        if (data_line[-1] not in separados):
            #in python, negative array indexes means you are counting from the right instead of left
            #so, in this case, the last attribute of data_line
            separados[data_line[-1]] = []
        #if the last element in the dataset line is not in the separated data array, create a list element with key of the last element of the array 
        separados[data_line[-1]].append(data_line)
        #add the data_line to to the separated data dictionary under the key of the last element of the line
        #last element is the value you are sorting instances by
    return separados

def split_data(dataset, split_ratio):
    train_size = int(len(dataset) * split_ratio)
    train_set = []
    copy = list(dataset)
    while len(train_set) < train_size:
        index = random.randrange(len(copy))
        #randrange(start, stop, step) returns a randomly generated number aligned w/ params
        train_set.append(copy.pop(index))
        #list.append(elem) adds elem to the end of the list
        #list.pop(index) removes and returns the element at the given index
    return [train_set, copy] 

def load_csv_data(filename):
    lines = csv.reader(open(filename, "rt"))
    #csv.reader returns a reader object which will iterate over the lines of the given csv file.
    dataset = list(lines)
    #list() converts an iterable into a list.
    for i in range(len(dataset)):
        #range is actually a function that returns a returns a sequence
        #if passed one parameter, starts from zero, uses parameter as stop
        #if passed two parameters, start & stop; three parameters, start, stop, & step
        dataset[i] = [float(x) for x in dataset[i]]
        #converting into float int
    return dataset

def main():
##first test main   
    #filename = "diabetes_data.csv"
    #dataset = load_csv_data(filename)
    #print ('{0} data file loaded with {1}'.format(filename, len(dataset)))
    ##w/ new string formatting, the brackets & characters within them (format fields) are replaced
    ##w/ objects passed into str.format() method, num in bracket can be used to refer to position
##second test main
    #dataset = [[1], [2], [3], [4], [5]]
    #split_ratio = 0.67
    ##split_ratio is what percent of the data will go into the train dataset, vs the test dataset
    ##this is common ration for testing alg. on dataset
    #train, test = split_data(dataset, split_ratio)
    #print ('there are {0} total rows. {1} are being used for training data and {2} are being used for testing'.format(len(dataset), train, test))
##third test main
    #dataset = [[1,20,1], [2,21,0], [3,22,1]]
    #separated = separate_by_class(dataset)
    #print('separated instances: {0}'.format(separated))
##fourth test main
    #numbers = [1, 2, 3, 4, 5]
    #print('Summary of list {0}: mean={1}, stdev={2}'.format(numbers, get_mean(numbers), get_stdev(numbers)))
##fifth test main


main()
