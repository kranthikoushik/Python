import csv    
with open('file1.csv') as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')    
       
    for row in csv_reader:
         print(f'Column names are {", ".join(row)}') 
