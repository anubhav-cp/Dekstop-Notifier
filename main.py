import requests
import datetime
import time
from plyer import notification

covidData = None

try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")

except:
    print("Pleasen Try Again")

if covidData != None:
    data = covidData.json()['Success']

    while True:
        notification.notify(
            title = f"Covid Stats on {datetime.date.today()}",
            message = f"Total Cases: {data['cases']}\nToday Cases: {data['todayCases']}\nToday Deaths: {data['todayDeaths']}\nTotal Active: {data['active']}",
            app_icon = None,
            timeout = 10
        )
        time.sleep(60*60)




