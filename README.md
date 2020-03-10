# googleapi
Basic google api python client library.

## Requirements
* Python >= 3.6
* urllib3 <= 1.25.8 
* Google console developers api key

## Example
googleapi example using googleapi.places
```python
import googleapi

key = "Google api key"
place = googleapi.places(auth=key, place="Renwick Gallery of the Smithsonian American Art Museum, Washington")

#return status of api request
placeStatus = place.status()

#return place json data parsed
placeJson = place.placesParsed(True)
```
