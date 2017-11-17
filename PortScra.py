#------------------------------------------------PortScraper1.0--------------------------------------------------------
#Webscaping tool that iterates over the website assuming increments of 1, but can easily be adapted to any requirements

#Packages required
import bs4
import re
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

#File Operations
filename = "ports.csv"       #make a new file called ports.csv
f = open(filename,"a")          #open file, "a" means append (add the data to the end of this file if it already exists)
headers = "port_name, port_country, latitude, longitude, Vessels_in_port, Expected_Arrivals\n"       #the col headers in csv
f.write(headers)         #write them ol' headers

#Target Website ('http:www.target.com/')
base_url = 'http://www.marinetraffic.com/en/ais/details/ports/' #this is a website about ports

#Scaping operation
for x in range(1,10):          #iterate over as many websites as needed by changing page number
    try:
        real_url = base_url + str(x)

        req = Request(real_url, headers={'User-Agent': 'Mozilla/5.0'})        #get around the 403 "access forbidden" error

        webpage = urlopen(req).read()
        page_soup=soup(webpage,"html.parser")

        #port names
        port = page_soup.findAll("h1",{"class":"font-220 no-margin"})
        port_name = port[0].text.strip()

        #port country
        port_loc = page_soup("span",{"class":"font-120"})       #find the info location in the html
        port_country = port_loc[0].text.split("Country: ")[1].split(" (")[0]        #scrape that yt

        #port locations, scraping the rest of the info
        port_info = page_soup("div",{"class":"bg-info bg-light padding-10 radius-4 text-left"})
        text = port_info[0].text.strip()
        latitude = text.split("Longitude: \n")[1].split("°")[0]
        longitude = text.split("° / ")[1].split("°\n")[0]
        Vessels_in_port = text.split("Vessels in Port: \n")[1].split("\n")[0]
        Expected_Arrivals = text.split("Expected Arrivals: \n")[1].split("'")[0]

    except Exception:       #on occasion there is nothing at a particular webpage
        print ("didnt work")
        pass        #pass means the code continues in this instance


    #Printing req info (for peace of mind that it worked)
    print ("Port name: " + port_name)
    print("Port country:  "+ port_country)
    print ("lat: " + latitude)
    print("long:  "+longitude)
    print("vessels in port " + Vessels_in_port)
    print("expected arrivals " + Expected_Arrivals)
    print ("Print: " + str(x))

    #Write to csv file
    f.write(port_name + "," + port_country + "," + latitude+ "," + longitude + "," + Vessels_in_port + "," + Expected_Arrivals + "\n")

f.close()        #closing the file saves it at the end of the operation, otherwise nothing would happen

#-------------------------------------------your ports just got scraped son---------------------------------------------
#------------------------------------------------PortScraper1.0---------------------------------------------------------

#----------------------------------------------Saif Bhatti Nov2017------------------------------------------------------
