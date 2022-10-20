import json
import requests
import datetime

class RailTime:


    @staticmethod
    def rail_time_bg_km():

        today = datetime.date.today()
        date_today = today.strftime("%Y%m%d")

        presentDate = datetime.datetime.now()
        unix_timestamp = (int(datetime.datetime.timestamp(presentDate)*1000))
        TIME = today.strftime("%H%M")


        MOTZKIN = "1400"
        BAT_GALIM = "2200"

        url = requests.get("https://www.rail.co.il/apiinfo/api/Plan/GetRoutes?OId=%s&TId=%s&Date=%s&Hour=%s&isGoing=true&c=%s" % (BAT_GALIM,MOTZKIN,date_today,TIME,unix_timestamp))

        url_request = json.loads(url.content)

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

            # mass_routes.append("-----------------------------")
            mass_routes.append(" ")
            mass_routes.append("Date: " + aa)
            mass_routes.append("Est time: " + bb)


        routes_one = (str(mass_routes).replace("["," ").replace("]","").replace("'","").replace(",","\n"))


        return {"routes" : routes_one}

    @staticmethod
    def rail_time_km_bg():

        today = datetime.date.today()
        date_today = today.strftime("%Y%m%d")

        presentDate = datetime.datetime.now()
        unix_timestamp = (int(datetime.datetime.timestamp(presentDate) * 1000))
        TIME = today.strftime("%H%M")

        MOTZKIN = "1400"
        BAT_GALIM = "2200"

        url = requests.get(
            "https://www.rail.co.il/apiinfo/api/Plan/GetRoutes?OId=%s&TId=%s&Date=%s&Hour=%s&isGoing=true&c=%s" % (
            BAT_GALIM, MOTZKIN, date_today, TIME, unix_timestamp))

        url_request = json.loads(url.content)

        data = dict(url_request)
        api_response_type = []
        count = 0
        global routes_size

        for each in data["Data"]["Routes"]:
            if each["Train"]:
                count = + 1
                api_response_type.append(count)
                routes_size = (len(api_response_type))

        # Departure time
        mass_routes = []
        mass_time = []
        for x in range(0, routes_size):
            aa = str(url_request["Data"]["Routes"][x]["Train"][0]["DepartureTime"])
            bb = str(url_request["Data"]["Routes"][x]["EstTime"])

            mass_routes.append(" ")
            mass_routes.append("Date: " + aa)
            mass_routes.append("Est time: " + bb)

        routes_one = (str(mass_routes).replace("[", " ").replace("]", "").replace("'", "").replace(",", "\n"))

        return {"routes": routes_one}











