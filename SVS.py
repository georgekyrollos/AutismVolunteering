from cgitb import reset
from datetime import *
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")

class Event:
    def __init__(self,name,url,date):
        self.name = name
        self.url = url
        self.date = date

    def passed(self):
        if date(int(self.date[0:4]),int(self.date[5:7]),int(self.date[8:10])) >= date.today(): # substring convert string to date type date(yyyy,mm,dd)
            return False
        return True

def formatDay(day):
    day = day.strip()
    if float(day) < 10 and day[0] != '0':
        return '0'+day
    return str(day)
def formatMonth(month):
    month = month.strip()
    if month.lower() == 'jan' or month.lower() == 'january':
        return '01'
    elif month.lower() == 'feb' or month.lower() == 'february':
        return '02'
    elif month.lower() == 'mar' or month.lower() == 'march':
        return '03'
    elif month.lower() == 'apr' or month.lower() == 'april':
        return '04'
    elif month.lower() == 'may':
        return '05'
    elif month.lower() == 'jun' or month.lower() == 'june':
        return '06'
    elif month.lower() == 'july':
        return '07'
    elif month.lower() == 'aug' or month.lower() == 'august':
        return '08'
    elif month.lower() == 'sep' or month.lower() == 'sept' or month.lower() == 'september':
        return '09'
    elif month.lower() == 'oct' or month.lower() == 'october':
        return '10'
    elif month.lower() == 'nov' or month.lower() == 'november':
        return '11'
    elif month.lower() == 'dec' or month.lower() == 'december':
        return '12'
    

def site1(events):
     URL = "https://support.researchautism.org/Static/find-an-event"
     try:
        elements = BeautifulSoup(requests.get(URL).content, "html.parser").find_all("div", class_="cardMiddle") 

        for event in elements:
            name = event.find(class_="name").text.strip() 
            
            name = name.replace("'","")
            year = name[0:4]
            name = name.replace(year,"").strip()
            

            date = event.find(class_="cardTitle").text.strip()
            month = date[0:3]
            day = formatDay(date.replace(month,"").strip())


            date = str(year)+"/"+str(formatMonth(month))+"/"+str(formatDay(day))
            url = event.find(class_="name")["href"]

            events.append(Event(name,url,date))

     except ValueError:
        print("Parsing error site 1"+ValueError)

     return events
def site2(events):
    URL = "https://www.teenlife.com/events/"
    try:
        elements = BeautifulSoup(requests.get(URL).content, "html.parser").find_all(
            "li", class_="mc-mc_upcoming_138 upcoming-event mc_teenlife-events future-event mc_primary_teenlife-events nonrecurring mc-3-hours mc-start-18-00 mc_rel_teenlifeevents mc_rel_boston")
        for event in elements:
            print(event)
    except ValueError:
        print("k")










    return events
def parseData():
    events = []
    
    events = site1(events)
    #events = site2(events)
    
    writeToFile(events)

def writeToFile(events): # Create Calendar with parsed events 
    try:
        f = open("events.js","w")  # overwrite old file
        
        f.write("$(document).ready(function() {$('#calendar').evoCalendar({ theme: 'Midnight Blue', calendarEvents: [\n")
        id = 0
        for event in events:
            if (not event.passed()):
                f.write("{id: '"+str(id)+"', name: '"+event.name+"', date:'"+event.date+"', description: 'location later', type:'"+event.url+"'},\n")
                id+=1
        f.write("]});$('#calendar').on('selectEvent', function(event,activeEvent) {window.open(activeEvent.type); })});")
    except ValueError:
        print("Error loading calendaer js: "+ValueError)
    finally:
        f.close()
   

parseData() 
#site2([])
