import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from urllib.request import Request, urlopen
import time
import warnings
warnings.filterwarnings("ignore")



def main():

   allData = dict()

   # Site 1
   URL = "https://support.researchautism.org/Static/find-an-event"
   allData["ResearchAutism"] = dict()
   page = requests.get(URL)
   soup = BeautifulSoup(page.content, "html.parser")
   events = soup.find_all("div", class_="cardMiddle")

   for event in events:

       name = event.find(class_="name").text
       date = event.find(class_="cardTitle").text.strip()
       url = event.find(class_="name")["href"]
       allData["ResearchAutism"][name] = [date, url]

   #Site 2
   URL ="https://act.autismspeaks.org/site/SPageNavigator/speaks_walk_allevents.html"
   allData["AutismSpeaks"] = dict()
   options = webdriver.ChromeOptions()
   options.add_argument('headless')
   capa = DesiredCapabilities.CHROME
   capa["pageLoadStrategy"] = "none"
   driver = webdriver.Chrome(executable_path='/Users/GeorgeKyrollos/PycharmProjects/pythonProject/chromedriver', chrome_options=options, desired_capabilities=capa)
   driver.set_window_size(1440, 900)
   driver.get(URL)
   time.sleep(5)

   plain_text = driver.page_source
   soup = BeautifulSoup(plain_text)
   events = soup.find_all("div", class_="as-walk-list")
   print(events)
   for event in events:
       locationDate = event.find(class_="location-date").text.split("-")
       name = locationDate[0].strip()
       date = locationDate[1].strip()


       newsLink = event.find(class_="location-date")
       url = newsLink.find_all('a', href=True)[0]["href"]


       allData["AutismSpeaks"][name] = [date, url]
   print(allData["AutismSpeaks"])



   #Site #3
   URL = "https://iacc.hhs.gov/meetings/autism-events/"
   allData["iacc"] = dict()
   page = requests.get(URL)
   soup = BeautifulSoup(page.content, "html.parser")
   events = soup.find_all("div", class_="news-front-container")

   for event in events:
       name = event.find(class_="news-link").text
       date = event.find(class_="news-date").text.strip()
       newsLink = event.find(class_="news-link")
       url = newsLink.find_all('a', href=True)[0]["href"]
       allData["iacc"][name] = [date, url]






   #site 5
   URL = "https://www.autismnj.org/events/"
   allData["AutismNJ"] = dict()
   URL = "https://act.autismspeaks.org/site/SPageNavigator/speaks_walk_allevents.html"
   allData["AutismSpeaks"] = dict()
   options = webdriver.ChromeOptions()
   options.add_argument('headless')
   capa = DesiredCapabilities.CHROME
   capa["pageLoadStrategy"] = "none"
   driver = webdriver.Chrome(executable_path='/Users/GeorgeKyrollos/PycharmProjects/pythonProject/chromedriver',
                             chrome_options=options, desired_capabilities=capa)
   driver.set_window_size(1440, 900)
   driver.get(URL)
   time.sleep(5)

   plain_text = driver.page_source
   soup = BeautifulSoup(plain_text)

   events = soup.find_all("div", class_="links-featured__wrap")
   for event in events:
       name = event.find(class_="title title--tertiary").text
       date = event.find(class_="meta events").text.strip()
       url = event.find(class_="brief_text")["href"]
       allData["AutismNJ"][name] = [date, url]



   #print(allData)
   with open('newFile.txt', 'w') as file:
       file.write(json.dumps(allData))

   # date
   # url
   # name
   #



main()

