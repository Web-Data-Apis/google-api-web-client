import urllib3
import json

class proximity(object):
	def __init__(self, auth, keyword, location, locationType, radius):
		auth = str(auth)
		location = tuple(location)
		keyword = str(keyword)
		radius = int(radius)

		proximityInstance = urllib3.PoolManager()
		proximityRequest = proximityInstance.request("GET", f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location[0]},{location[1]}&radius={radius}&type={locationType}&keyword={keyword}&key={auth}")
		self._proximityInfo = proximityRequest.data

	def locations():
            with open("googleapi/types/locationtypes.types", "r") as types:
                typeContent = types.read()
                return typeContent.split("\n")

	def status(self):
		proximityStatusCleaned = json.loads(self._proximityInfo.decode())
		proximityStatusDumped = json.dumps(proximityStatusCleaned)
		proximityStatus = json.loads(proximityStatusDumped)["status"]

		return json.loads(self._proximityInfo.decode())["status"]

	def attributions(self):
		proximityAttr = json.loads(self._proximityInfo.decode())["html_attributions"]
		return json.dumps(proximityAttr, indent=4)

	def proximityLocate(self):
		proximityCleaned = json.loads(self._proximityInfo.decode())["results"]
		proximityDumped = json.dumps(proximityCleaned)
		
		proximityLocation = json.loads(proximityDumped)
		proximityLocation2 = json.dumps(proximityLocation)
		proximityLocation3 = json.loads(proximityLocation2)[0]
		
		proximityLocation4 = json.dumps(proximityLocation3)
		proximityLocation5 = json.loads(proximityLocation4)["geometry"]
		proximityLocation6 = json.dumps(proximityLocation5)
		
		proximityLocation7 = json.loads(proximityLocation6)["location"]
		proximityLocationDumped = json.dumps(proximityLocation7)

		return proximityLocationDumped

	def viewport(self):
		proximityCleaned = json.loads(self._proximityInfo.decode())["results"]
		proximityDumped = json.dumps(proximityCleaned)
		proximityLocation = json.loads(proximityDumped)
		
		proximityLocation2 = json.dumps(proximityLocation)
		proximityLocation3 = json.loads(proximityLocation2)[0]
		proximityLocation4 = json.dumps(proximityLocation3)
		
		proximityLocation5 = json.loads(proximityLocation4)["geometry"]
		proximityLocation6 = json.dumps(proximityLocation5)
		proximityViewport = json.loads(proximityLocation6)["viewport"]
		
		return proximityViewport
