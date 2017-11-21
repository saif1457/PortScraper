#Important Python packages
import urllib.parse
import requests
import urllib.request, json

#Everywhere that has v_ is a choice variable. I called it what it is for clarity, and added v_ to show you it can be changed

#File Operations
v_filename = "tutorial.csv"       #make a new file called tutorial.csv
v_f = open(v_filename,"a")          #open file, "a" means append (add the data to the end of this file if it already exists)
v_headers = "title,longitude\n"       #the col headers in csv
v_f.write(v_headers)         #write them ol' headers

#API Feed (in this case it is a .json feed from USGS
v_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson' 
v_json_data = requests.get(v_url).json()                #use requests to 'get' the .json data

for v_x in range (0,(len(v_json_data["features"]))): #this loops through all the earthquakes (len gives number of earthquakes)
        v_title = str(v_json_data['features'][v_x]['properties']['place']) #specifically looking in features, properties, place 
        v_Qlongitude = str(str(v_json_data['features'][v_x]['geometry']['coordinates']).split('[')[1].split(',')[0])
        #think of this like a file system, and the above is drawing the filepath
        
        #print the title and the longitude so we know it worked
        print('Title: ' + v_title)
        print('Longitude:' + v_Qlongitude)

        v_f.write(v_title + "," +v_Qlongitude + "\n")   #write this info into the .csv from earlier


v_f.close()        #closing the file saves it at the end of the operation, otherwise nothing would happen
