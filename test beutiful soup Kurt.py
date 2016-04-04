import requests
from bs4 import BeautifulSoup



#soup = BeautifulSoup(r.content)
#links = soup.find_all("a")

#for link in links:
#    print "<a href='%s'>%s</a>" %(link.get("href"), link.text

r = requests.get("http://www.flightstats.com/go/FlightStatus/flightStatusByAirport.do?airportCode=SJU&airportQueryType=0")
txt = r.text
print(txt)
