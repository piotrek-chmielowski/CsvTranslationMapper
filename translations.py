#!/usr/bin/python3

# This script reads translations stored in CSV format and prints them to the stdout in Android strings.xml format.
# CSV file format: key, en, pl, ua, pt

import csv

lang_names = ["en", "pl", "ua", "ru", "pt"]

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


for lang, words in zip(lang_names, langs[1:]):
    print (lang)
    for key, word in zip(langs[0], words):
        print ("<string name=\"{}\">{}</string>".format(key, word))
