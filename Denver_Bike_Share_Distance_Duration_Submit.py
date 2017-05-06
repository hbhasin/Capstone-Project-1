# make sure there is a connection to Google's server
import requests
try:
  response = requests.get('http://www.google.com')
except:
  print('Can\'t connect to Google\'s server')
  raw_input('Press any key to exit.')
  quit()

# use the Google Maps API
import googlemaps
import json
import csv

with open('Denver_Bike_Kiosks_Details.csv', 'r') as f:
    reader = csv.reader(f)
    Bike_list = list(reader)
f.close()
result1 = []
result2 = []
result = []

with open("Denver_Bike_Kiosks_Distances_Durations.csv", "w", newline='') as f:
  writer = csv.writer(f)
  colNames = ["CheckoutStation", "CheckoutStationLatitude", "CheckoutStationLongitude",
      "ReturnStation", "ReturnStationLatitude", "ReturnStationLongitude",
      "Distance_Checkout_Return", "Duration_Checkout_Return",
      "Distance_Return_Checkout", "Duration_Return_Checkout", "Average_Distance",
      "Average_Duration"]
  writer.writerow(colNames)
  for StationRow in Bike_list[1:7921]:
    origins = StationRow[1] + "," + StationRow[2]
    destinations = StationRow[4] + "," + StationRow[5]
    gmaps = googlemaps.Client(key='provide your key here')
    matrix = gmaps.distance_matrix(origins, destinations, mode="bicycling", units="imperial", avoid="highways")
    print(matrix)
    cycling_distance = matrix['rows'][0]['elements'][0]['distance']['value']
    cycling_time = matrix['rows'][0]['elements'][0]['duration']['value']
    #print(cycling_distance*0.0006213,cycling_time/60)
    #print(StationRow)
    result1 = StationRow + [format(cycling_distance*0.0006213, '.2f'), format(cycling_time/60,'2f')]
    #print(result1)
    origins = StationRow[4] + "," + StationRow[5]
    destinations = StationRow[1] + "," + StationRow[2]
    matrix = gmaps.distance_matrix(origins, destinations, mode="bicycling", units="imperial", avoid="highways")
    print(matrix)
    cycling_distance = matrix['rows'][0]['elements'][0]['distance']['value']
    cycling_time = matrix['rows'][0]['elements'][0]['duration']['value']
    #print(cycling_distance*0.0006213,cycling_time/60)
    result2 = [format(cycling_distance*0.0006213, '.2f'), format(cycling_time/60,'2f')]
    result = result1 + result2
    print(result)
    writer.writerow(result)
  f.close()
