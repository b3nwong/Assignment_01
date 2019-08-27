import csv
with open('places.csv', newline='') as csvfile:
    travel_excel = csv.reader(csvfile)
    list_numb=0
    for row in travel_excel:
        list_numb+=1
        print("{}. {} in {} priority {} {}".format(list_numb,row[0],row[1],row[2],row[3]))