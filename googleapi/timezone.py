import urllib3
import json
from datetime import datetime

class timezone(object):
    def __init__(self, auth, location, timestamp=None):
        auth = str(auth)
        location = tuple(location)

        instance = urllib3.PoolManager()
        location = tuple(location)      
        if not timestamp:
            timestamp = datetime.now().timestamp()

        timezoneRequest = instance.request("GET", f"https://maps.googleapis.com/maps/api/timezone/json?location={location[0]},{location[1]}&timestamp={timestamp}&key={auth}")
        self._timezoneInfo = timezoneRequest.data

    def formatTimestamp(timestamp):
        formattedTimestamp = datetime.fromtimestamp(timestamp)
        return formattedTimestamp

    def json(self, formatting=False):
        timezoneCleaned = json.loads(self._timezoneInfo.decode())
        timezoneDumped = json.dumps(timezoneCleaned)
        timezoneDstoffset = json.loads(timezoneDumped)["dstOffset"]
        timezoneRawoffset = json.loads(timezoneDumped)["rawOffset"]
        timezoneId = json.loads(timezoneDumped)["timeZoneId"]
        timezoneName = json.loads(timezoneDumped)["timeZoneName"]

        parsed = {"results": {"dstOffset": timezoneDstoffset, "rawOffset": timezoneRawoffset, "timeZoneId": timezoneId, "timeZoneName": timezoneName}}

        if formatting is False:
            return parsed
        return json.dumps(parsed, indent=4)

    def dstOffset(self):
        timezoneDstCleaned = json.loads(self._timezoneInfo.decode())
        timezoneDstDumped = json.dumps(timezoneDstCleaned)

        dstOffset = json.loads(timezoneDstDumped)["dstOffset"]
        return dstOffset

    def rawOffset(self):
        timezoneRawCleaned = json.loads(self._timezoneInfo.decode())
        timezoneRawDumped = json.dumps(timezoneRawCleaned)

        rawOffset = json.loads(timezoneRawDumped)["rawOffset"]
        return rawOffset

    def id(self):
        timezoneIdCleaned = json.loads(self._timezoneInfo.decode())
        timezoneIdDumped = json.dumps(timezoneIdCleaned)

        timezoneId = json.loads(timezoneIdDumped)["timeZoneId"]
        return timezoneId

    def name(self):
        timezoneNameCleaned = json.loads(self._timezoneInfo.decode())
        timezoneNameDumped = json.dumps(timezoneNameCleaned)

        timezoneName = json.loads(timezoneNameDumped)["timeZoneName"]
        return timezoneName

    def status(self):
        timezoneStatusCleaned = json.loads(self._timezoneInfo.decode())
        timezoneStatusDumped = json.dumps(timezoneStatusCleaned)
        timezoneStatus = json.loads(timezoneStatusDumped)["status"]

        return timezoneStatus