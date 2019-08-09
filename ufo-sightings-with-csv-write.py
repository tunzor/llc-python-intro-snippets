# 1. Number of sightings Canada-wide (all provinces) in 2013
# 2. Number of sightings in Toronto from 2014-2017
# 3. Number of sightings everywhere EXCEPT Winnipeg, MB
# 4. Number of sightings in the Maritime provinces (NS, NF, PI, NB) in
# the month of Feb
# Bonus: Which province had the most sightings overall? How many?

import csv   # import the `csv` library
ufo_data_file = open('ufo-data.csv', 'r') # open the file
ufo_data_dictionary_reader = csv.DictReader(ufo_data_file) # pass the file into `DictReader`

sightings_in_2015 = []

for sighting in ufo_data_dictionary_reader:
    if sighting['Year'] == '2015':
        # print(sighting['Location'])
        sightings_in_2015.append(sighting)

print("There have been " + str(len(sightings_in_2015)) + " in Canada in 2015")

with open('sightings-in-2015.csv', 'w') as outputFile:
    sightings_writer = csv.writer(outputFile)
    sightings_writer.writerow(['Location','Province','Month','Day','Year'])
    for row in sightings_in_2015:
        sightings_writer.writerow(row.values())

