#!/usr/bin/python3
import unittest
import csv


langs = [
    [],  # key
    [],
    [],
    [],
    [],
    []
]

with open('t.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in reader:
        key = row[0]
        if key and not key.startswith("//"):
            for i, translation in enumerate(row):
                langs[i].append(translation)

lang_names = ["en", "pl", "ua", "ru", "pt"]

for lang, words in zip(lang_names, langs):
    print (lang)
    for key, word in zip(langs[0], words):
        print ("<string name=\"{}\">{}</string>".format(key, word))
