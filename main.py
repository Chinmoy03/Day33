import requests
from datetime import *


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# print(data)
parameters = {
    "lat":53.544388,
    "lon":-113.490929,
    "formatted":0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
time_now = datetime.now()
sunset_time = sunset.split("T")
sunset_hour = sunset_time[1].split(":")[0]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
print(sunrise_hour, sunset_hour, time_now.hour)


