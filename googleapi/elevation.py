import urllib3
import json

class elevation(object):
    def __init__(self, auth, location):
        location = tuple(location)
        instance = urllib3.PoolManager()
        elevationRequest = instance.request("GET", f"https://maps.googleapis.com/maps/api/elevation/json?locations={location[0]},{location[1]}&key={auth}")
        self.elevationInfo = elevationRequest.data

    def elevationParsed(self, formatting=False):
        elevationFromSeaLevel = json.loads(self.elevationInfo.decode())["results"][0]
        elevationDumped = json.dumps(elevationFromSeaLevel)
        height = json.loads(elevationDumped)["elevation"]

        elevationLocationDumped = json.dumps(elevationFromSeaLevel)
        elevationCleaned = json.loads(elevationLocationDumped)["location"]
        elevationResolution = json.loads(elevationLocationDumped)["resolution"]
        elevationCleanedDumped = json.dumps(elevationCleaned)

        elevationLat = json.loads(elevationCleanedDumped)["lat"]
        elevationLng = json.loads(elevationCleanedDumped)["lng"]

        parsed = {"elevation": height, "resolution": elevationResolution, "lat": elevationLat,"lng": elevationLng}

        if formatting is False:
            return parsed   

        return json.dumps(parsed, indent=4)

    def status(self):
        elevationStatus = json.loads(self.elevationInfo.decode())["status"]
        return elevationStatus
