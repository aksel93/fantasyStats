import csv
from html.parser import HTMLParser

team = input("Which team's stats do you want to view?")

csvfile = open(team +'.csv', newline='')

c = csv.reader(csvfile)

for row in c:
    print( row[1] + ", " + row[5])

csvfile.close()