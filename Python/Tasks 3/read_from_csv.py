import csv

csv_file = open('trees.csv')
csv_reader = csv.reader(csv_file, delimiter=',')


# Skip first row if it only contains the column headers
next(csv_reader)
max_height = 0

for row in csv_reader:
    Index, Girth, Height, Volume = row
    if int(Height) > max_height:
        max_height = int(Height)

print("Heighest tree was {} feet high.".format(max_height))

csv_file = open('trees.csv')
csv_reader2 = csv.reader(csv_file, delimiter=',')
next(csv_reader2)
max_volume = 0

for row in csv_reader2:
    Index, Girth, Height, Volume = row
    if float(Volume) > max_volume:
        max_volume = float(Volume)

print("The tree with the largest volume has a volume of {} ft^3 ".format(max_volume))

csv_file.close()