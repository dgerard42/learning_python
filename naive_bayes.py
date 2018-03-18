# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    naive_bayes.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerard <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/18 10:39:09 by dgerard           #+#    #+#              #
#    Updated: 2018/03/18 12:20:21 by dgerard          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3

import csv
import random

def split_data(dataset, split_ratio):
    train_size = int(len(dataset) * split_ratio)
    train_set = []
    copy = list(dataset)
    while len(train_set) < train_size:
        index = random.randrange()
        #randrange(start, stop, step) returns a randomly generated number aligned w/ params

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
    filename = "diabetes_data.csv"
    dataset = load_csv_data(filename)
    print ('{0} data file loaded with {1}'.format(filename, len(dataset)))
    #w/ new string formatting, the brackets & characters within them (format fields) are replaced
    #w/ objects passed into str.format() method, num in bracket can be used to refer to position

main()
