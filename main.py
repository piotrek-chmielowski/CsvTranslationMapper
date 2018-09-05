#!/usr/bin/python3
import unittest
import csv

NUM_OF_LANGS = 5

new = [[], [], [], [], []]

with open('t.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in reader:
        key = row[0]
        if key and not key.startswith("//"):
            for i, translation in enumerate(row[1:]):
                new[i].append(translation)


print(new)
