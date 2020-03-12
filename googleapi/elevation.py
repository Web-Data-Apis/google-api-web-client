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
    
    def resolution(self):
        elevationResolutionCleaned = json.loads(self.elevationInfo.decode())["results"][0]
        resolutionDumped = json.dumps(elevationResolutionCleaned)

        elevationResolution = json.loads(resolutionDumped)["resolution"]
        return elevationResolution

    def cordinate(self):
        elevationCordinateCleaned = json.loads(self.elevationInfo.decode())["results"][0]
        cordinateDumped = json.dumps(elevationCordinateCleaned)

        cordinateJson = json.loads(cordinateDumped)["location"]
        cordinateJsonDumped = json.dumps(cordinateJson)

        latitude = json.loads(cordinateJsonDumped)["lat"]
        longitude = json.loads(cordinateJsonDumped)["lng"]

        return (latitude, longitude)

    def altitude(self):
        elevationAltitudeCleaned = json.loads(self.elevationInfo.decode())["results"][0]
        altitudeDumped = json.dumps(elevationAltitudeCleaned)

        altitudeHeight = json.loads(altitudeDumped)["elevation"]

        return altitudeHeight

    def status(self):
        elevationStatus = json.loads(self.elevationInfo.decode())["status"]
        return elevationStatus
