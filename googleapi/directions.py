import urllib.parse
import urllib3
import json

class directions(object):
    mode_methods = ["walking", "driving", "transit"]

    def __init__(self, auth, origin, destination, departure="now", mode="driving"):
        if mode not in mode_methods:
            raise ValueError(f"Mode method: {mode} not a valid method")

        instance = urllib3.PoolManager()
        optionsDest = {"destination": destination}
        parsedDest = urllib.parse.urlencode(optionsDest)

        directionsRequest = instance.request("GET", f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&{parsedDest}&departure_time={departure}&mode={mode}&key={auth}")
        self.directionInfo = directionsRequest.data

    def json(self, formatting=False):
        waypointPlaceIdTable = json.loads(self.directionInfo.decode())["geocoded_waypoints"]
        waypointPlaceId = json.dumps(waypointPlaceIdTable[0])
        waypointPlaceId2 = json.loads(waypointPlaceId)["place_id"]

        waypointPlaceIdLocation = json.dumps(waypointPlaceIdTable[1])
        waypointPlaceIdLocation2 = json.loads(waypointPlaceIdLocation)["place_id"]

        waypointTypes = json.dumps(waypointPlaceIdTable[0])
        waypointDesc = json.loads(waypointTypes)["types"]

        waypointDecsTypes2 = json.dumps(waypointPlaceIdTable[1])
        waypointDesc2 = json.loads(waypointDecsTypes2)["types"]

        parsed = {"origin_placeId": waypointPlaceId2,
                "origin_commonTags": waypointDesc,
                "dest_placeId": waypointPlaceIdLocation2,
                "dest_commonTags": waypointDesc2}

        if formatting is False:
            return parsed
        return json.dumps(parsed, indent=4)

    def routeJson(self, formating=False):
        try:

            routesTable = json.loads(self.directionInfo.decode())["routes"][0]
            routesTableArg = json.dumps(routesTable)
            routesTableBounds = json.loads(routesTableArg)["bounds"]

            routesTableBoundsFormat = json.dumps(routesTableBounds, indent=4)
            routesTableCopyrights = json.loads(routesTableArg)["copyrights"]

            routesTableLegs = json.loads(routesTableArg)["legs"][0]
            routesTableLegs2 = json.dumps(routesTableLegs)
            routesTableLegs3 = json.loads(routesTableLegs2)["distance"]
            routesTableLegsFormat = json.dumps(routesTableLegs3, indent=4)

            routesDuration = json.loads(routesTableArg)["legs"][0]
            routesDuration2 = json.dumps(routesDuration)
            routesDuration3 = json.loads(routesDuration2)["duration"]["text"]
            routesDuration4 = json.loads(routesDuration2)["duration"]["value"]

            routesDistance = json.dumps(routesDuration)
            routesDistance2 = json.loads(routesDistance)["distance"]["text"]

            routesStartAddress = json.loads(routesTableArg)["legs"][0]
            routesStartAddress2 = json.dumps(routesStartAddress)
            routesStartAddress3 = json.loads(routesStartAddress2)["start_address"]

            routesStartLocation = json.loads(routesTableArg)["legs"][0]
            routesStartLocation2 = json.dumps(routesStartLocation)
            routesStartLocationLat = json.loads(routesStartLocation2)["start_location"]["lat"]
            routesStartLocationLng = json.loads(routesStartLocation2)["start_location"]["lng"]

            routesEndLocationLat = json.loads(routesStartLocation2)["end_location"]["lat"]
            routesEndLocationLng = json.loads(routesStartLocation2)["end_location"]["lng"]

            routesEndAddress = json.loads(routesStartLocation2)["end_address"]
            parsed = {"start_address": routesStartAddress3,
                      "end_address":routesEndAddress,
                      "start_location": [routesStartLocationLat,
                       routesStartLocationLng],
                      "end_location": [routesEndLocationLat,
                       routesEndLocationLng],
                      "distance": [routesDuration3,
                       routesDistance2]}

            if formating is False:
                return parsed
            return json.dumps(parsed, indent=4)

        except IndexError:
            return None

    def status(self):
        directionStatus = json.loads(self.directionInfo.decode())["status"]
        return directionStatus
