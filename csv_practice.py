import csv

# method one 
with open('mushrooms.csv', newline='') as csvfile:
    traits = csv.reader(csvfile)
# method two
file = open('mushrooms.csv') 
# creates file variable and sets it to the opened file  that open() returned
type(file)
# the type of the file is “_io.TextIOWrapper” which is a file object that open() returned

# now that the file is opened you need to read it
csvreader = csv.reader(file)

# extract the field names by creating an empty list called header
# use the next method to obtain the header
# .next() returns the current row and moves to the next row

header = []
header = next(csvreader)

# extract the data by creating a empty list and iterate it through the csvreader object and append it to the row
rows = []
for row in csvreader:
    rows.append(row)
file.close()