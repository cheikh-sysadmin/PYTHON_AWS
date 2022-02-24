import csv
import copy
"""
dictionnaire=[]
with open('car_fleet.csv') as csvFile:
    read=csv.reader(csvFile)
    head=list(read)
    header=head[0]
#print(header)
head.pop(0) #pour supprimer la premiére ligne
#print(head)
for row in head:
    zipp=zip(header,row)
    dictionnaire.append(dict(zipp))
for dict in dictionnaire:
   print(dict)
"""
myInventoryList=[]
myVehicle = {
          "vin" : "<empty>",
          "make" : "<empty>" ,
          "model" : "<empty>" ,
          "year" : 0,
          "range" : 0,
          "topSpeed" : 0,
          "zeroSixty" : 0.0,
          "mileage" : 0
        }


with open('car_fleet.csv') as csvFile:  
      csvReader = csv.reader(csvFile, delimiter=',')  
      lineCount = 0  
      for row in csvReader:  
        if lineCount == 0:  
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
      print(f'Processed {lineCount} lines.') 





