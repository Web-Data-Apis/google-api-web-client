import urllib3
import urllib.parse
import re
import json

class places(object):
    def __init__(self, auth, place):
        instance = urllib3.PoolManager()
        quotedParams = urllib.parse.quote(place)
        placeRequest = instance.request("GET", f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={quotedParams}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={auth}")
        self._placesInfo = placeRequest.data

    def placesParsed(self, formatting=False):
        placesCleaned = json.loads(self._placesInfo.decode())["candidates"][0]
        placesDumped = json.dumps(placesCleaned)

        formattedAddress = json.loads(placesDumped)["formatted_address"]
        placesGeometry = json.loads(placesDumped)["geometry"]
        placesGeoDumped = json.dumps(placesGeometry)

        placesLocation = json.loads(placesGeoDumped)["location"] 
        placesLoDumped = json.dumps(placesLocation)
        
        if "opening_hours" in placesDumped:
            openingHours = json.loads(placesDumped)["opening_hours"]
            openingDumped = json.dumps(openingHours)
            openNow = json.loads(openingDumped)["open_now"]

        else:
            openNow = None

        mapsPhotos = json.loads(placesDumped)["photos"]
        mapsPhotosDumped = json.dumps(mapsPhotos)

        mapsItems = json.loads(mapsPhotosDumped)[0]
        mapsItemsDumped = json.dumps(mapsItems)
        mapsUrlRaw = json.loads(mapsItemsDumped)["html_attributions"][0]

        mapsUrlParsed = mapsUrlRaw.replace('<a href="', "")
        urlReplace = re.sub(">.*?</a>", "", mapsUrlParsed).replace('"', "")

        if "rating" in placesDumped:
            ratingScore = json.loads(placesDumped)["rating"]

        else:
            ratingScore = None
        placesName = json.loads(placesDumped)["name"]
        placesLat = json.loads(placesLoDumped)["lat"]
        placesLng = json.loads(placesLoDumped)["lng"]

        parsed = {"name": placesName, "open": openNow, "rating": ratingScore, "address": formattedAddress.split(", "), "contrib_url": urlReplace, "contrib_lat": placesLat, "contrib_lng": placesLng}

        if formatting is False:
            return parsed
        return json.dumps(parsed, indent=4)

    def status(self):
        placesStatus = json.loads(self._placesInfo.decode())["status"]
        return placesStatus
