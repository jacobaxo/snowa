from bs4 import BeautifulSoup 
from requests import get
import requests
from tweepy import auth
import smtplib, ssl

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.0248&lon=-80.7586#.YzsEn3bMJD8")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")


today = forecast_items[0]
print(today.prettify())
img = today.find("img")
desc = img['title']
print(desc)
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]


tommorow = forecast_items[2]
print(tommorow.prettify())
img = tommorow.find("img")
desc = img['title']
print(desc)
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]

dayafter = forecast_items[4]
print(dayafter.prettify())
img = dayafter.find("img")
desc = img['title']
print(desc)
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]

dayafter2 = forecast_items[6]
print(dayafter2.prettify())
img = dayafter2.find("img")
desc = img['title']
print(desc)
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]

dayafter3 = forecast_items[8]
print(dayafter3.prettify())
img = dayafter3.find("img")
desc = img['title']
print(desc)
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]




#port = 587  # For starttls
#smtp_server = "smtp.gmail.com"
#sender_email = "mays_jacobj@student.mahoningctc.com"
#receiver_email = "jacobviolin5@gmail.com"
#password = ("password123")
#message = (today)(tommorow)(dayafter)(dayafter2)(dayafter3)

#context = ssl.create_default_context()
#with smtplib.SMTP(smtp_server, port) as server:
    #server.ehlo()  # Can be omitted
    #server.starttls(context=context)
    #server.ehlo()  # Can be omitted
    #server.login(sender_email, password)
    #server.sendmail(sender_email, receiver_email, message)