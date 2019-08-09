import csv

sightingsByProv = {
   'BC': 0,
   'AB': 0,
   'SK': 0,
   'MB': 0,
   'ON': 0,
   'QC': 0,
   'NFLD': 0,
   'NS': 0,
   'PEI': 0,
   'NB': 0,
   'YK': 0,
   'NT': 0,
   'NU': 0
}
ufo_data_file = open('ufo-data.csv', 'r') # this tells python to open the file
ufo_reader = csv.DictReader(ufo_data_file)
for sighting in ufo_reader:
   prov = sighting['Province']
   # Merge the same province with different province codes
   if prov == 'PE' or prov == 'PI':
       prov = 'PEI'
   if prov == 'NF' or prov == 'NL':
       prov = 'NFLD'
   if prov == 'PQ':
       prov = 'QC'
   if prov == 'YT':
       prov = 'YK'
   sightingsByProv[prov] = sightingsByProv[prov] + 1

ufo_data_file.close()  # close it
for key, value in sorted(sightingsByProv.items(), key=lambda item: item[1], reverse=True):
   print("There were {} sightings in {}".format(value, key))
