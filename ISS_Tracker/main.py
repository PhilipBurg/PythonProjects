import json
import turtle
import requests
import time
import webbrowser
import geocoder 

url = "http://api.open-notify.org/astros.json"
response = requests.get(url, timeout=30)
result = response.json()
file = open("iss.txt", "w")
file.write("At this moment there are " + str(result["number"]) + " astronatus on the ISS: \n\n")

people = result["people"]
for p in people:
    file.write(p['name'] + " - is on board" + "\n")

#print the long. and lat.
g = geocoder.ip('me')
file.write("\n The current location [lat / long] is: " + str(g.latlng) + "\n")
file.close()
webbrowser.open("iss.txt")

# world in turtle module
screen = turtle.Screen()
screen.setup(1900, 1000)
screen.setworldcoordinates(-180,-90,180,90)

#load image of world map
screen.bgpic("map.png")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

counter = 0 

while True:
    # load current status of ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    result = response.json()

    #Extract ISS location
    location = result["iss_position"]
    lat = float(location['latitude'])
    lon = float(location['longitude'])


    # Update ISS location on the map
    iss.goto(lon, lat)

    print(f"ISS Position: Latitude: {lat}, Longitude: {lon}")

    # Set refreshing rate for 5 seconds
    time.sleep(5)