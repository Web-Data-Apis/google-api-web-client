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

    def json(self, formatting=False):
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

        parsed = {"name": placesName,
                  "open": openNow,
                  "rating": ratingScore,
                  "address": formattedAddress.split(", "),
                  "contrib_url": urlReplace,
                  "contrib_lat": placesLat,
                  "contrib_lng": placesLng}

        if formatting is False:
            return parsed
        return json.dumps(parsed, indent=4)

    def name(self):
        nameCleaned = json.loads(self._placesInfo.decode())["candidates"][0]
        nameDumped = json.dumps(nameCleaned)

        placeName = json.loads(nameDumped)["name"]
        return placeName

    def address(self):
        addressCleaned = json.loads(self._placesInfo.decode())["candidates"][0]
        addressDumped = json.dumps(addressCleaned)

        addressList = json.loads(addressDumped)["formatted_address"].split(", ")
        return addressList

    def openNow(self):
        openingCleaned = json.loads(self._placesInfo.decode())["candidates"][0]
        openingDumped = json.dumps(openingCleaned)
        if "opening_hours" in openingCleaned:
            openingHours = json.loads(openingDumped)["opening_hours"]
            openingHoursDumped = json.dumps(openingHours)

            isOpen = json.loads(openingHoursDumped)["open_now"]
            return isOpen

        else:
            isOpen = None

    def photo(self, auth, download=False):
        photosInstance = urllib3.PoolManager()

        photosCleaned = json.loads(self._placesInfo.decode())["candidates"][0]
        photosDumped = json.dumps(photosCleaned)

        photosJson = json.loads(photosDumped)["photos"][0]
        photosJsonDumped = json.dumps(photosJson)

        photosReference = json.loads(photosJsonDumped)["photo_reference"]
        
        photosWidth = json.loads(photosJsonDumped)["width"]
        photosUrl = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={photosWidth}&photoreference={photosReference}&key={auth}"

        if download is True:
            photosRequest = photosInstance.request("GET", photosUrl)

            with open("photoreference.jpg", "wb") as download_image:
                download_image.write(photosRequest.data)
        
        return photosUrl

    def rating(self):
        ratingCleaned = json.loads(self._placesInfo.decode())["candidates"][0]
        ratingDumped = json.dumps(ratingCleaned)

        if "rating" in ratingDumped:
            rating = json.loads(ratingDumped)["rating"]

            return float(rating)

        else:
            rating = None

    def cordinate(self):
        cordinateCleaned = json.loads(self._placesInfo.decode())["candidates"][0]
        cordinateDumped = json.dumps(cordinateCleaned)
    
        geo = json.loads(cordinateDumped)["geometry"]
        geoDumped = json.dumps(geo)

        cords = json.loads(geoDumped)["location"]
        cordsDumped = json.dumps(cords)

        latitude = json.loads(cordsDumped)["lat"]
        longitude = json.loads(cordsDumped)["lng"]

        return (latitude, longitude)

    def status(self):
        placesStatus = json.loads(self._placesInfo.decode())["status"]
        return placesStatus