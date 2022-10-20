import json
import requests
import datetime

today = datetime.date.today()
date_today = today.strftime("%Y%m%d")

presentDate = datetime.datetime.now()
unix_timestamp = (int(datetime.datetime.timestamp(presentDate)*1000))
MOTZKIN = "1400"
BAT_GALIM = "2200"
time = today.strftime("%H%M")

url = requests.get("https://www.rail.co.il/apiinfo/api/Plan/GetRoutes?OId=%s&TId=%s&Date=%s&Hour=%s&isGoing=true&c=%s" % (BAT_GALIM,MOTZKIN,date_today,time,unix_timestamp))

url_request = json.loads(url.content)
routes = str((url_request["Data"]["Routes"]))

data = dict(url_request)
api_response_type = []
count = 0
global routes_size

for each in data["Data"]["Routes"]:
    if each["Train"]:
        count =+ 1
        api_response_type.append(count)
        routes_size =(len(api_response_type))

# Departure time
mass_routes = []
mass_time = []
for x in range(0,routes_size):
    aa = str(url_request["Data"]["Routes"][x]["Train"][0]["DepartureTime"])
    bb = str(url_request["Data"]["Routes"][x]["EstTime"])

    mass_routes.append(aa + bb)

    routes_one = (str(mass_routes).replace("["," ").replace("]","").replace("'","").replace(",","\n"))
    routes_two = (str(mass_time).replace("[", " ").replace("]", "").replace("'", "").replace(",", "\n"))

    print(aa,"Estimate time: " + bb)











