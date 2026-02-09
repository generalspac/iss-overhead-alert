import requests
import datetime
import mail_sender
from dotenv import load_dotenv
import os

load_dotenv()  # loading the .env file


##my position
MY_LAT=os.getenv("MY_LAT")
MY_LONG=os.getenv("MY_LONG")
my_position={
"lat":MY_LAT,
"lng":MY_LONG
}
recipient_name=os.getenv("RECIPIENT_NAME")
recipient_email=os.getenv("RECIPIENT_ADDR")
while True:
#######time
    time=datetime.datetime.now().strftime("%H:%M:%S")
    time_split=time.split(":")
    time_in_sec=int(time_split[0])*3600+int(time_split[1])*60+int(time_split[2])
    ###sunrise and sunset  of my position
    request1=requests.get(url="https://api.sunrise-sunset.org/json" ,params=my_position)
    request1.raise_for_status()
    sunrise_sunset=request1.json()
    sunrise=sunrise_sunset['results']['sunrise']
    sunset=sunrise_sunset['results']['sunset']
    ###iss data
    request=requests.get(url="http://api.open-notify.org/iss-now.json")
    request.raise_for_status()
    data=request.json()
    iss_lat=data['iss_position']['latitude']
    iss_long=data['iss_position']['longitude']

    ##########let's send the mail before sunrise and after sunset
    time_set=int(sunset.split(":")[0])+12
    min_set=int((sunset.split(":")[1]))
    sec_set=int((sunset.split(":")[2])[:2])
    time_rise=int(sunrise.split(":")[0])
    min_rise=int(sunrise.split(":")[1])
    sec_rise=int((sunrise.split(":")[2])[:2])
    if ((time_in_sec >= time_set*3600+min_set*60+sec_set) and time_in_sec<=0) or (time_in_sec>0 and time_in_sec<time_rise*3600+min_rise*60+sec_rise):
        if int(MY_LAT)==int(iss_lat) and int(MY_LONG)==int(iss_long):

            mail_sender.send_mail(name,name=recipient_email)
