# Google Api Python Web Client
Basic google api python client library. Get information on elevation data or use the directions api to view routes. Note, this project is still in development. If you want more information on googlemaps api's and python go here for [*googlemaps*](https://github.com/googlemaps/google-maps-services-python) module.

## Prerequisites
* Python 3.x.x [Most recent version](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe)
* urllib3 [Most recent version](https://pypi.org/project/urllib3/)
* [Google Developers API key](https://developers.google.com/places/web-service/get-api-key)
## Includes
* Google Cloud Translate Api [Docs](https://cloud.google.com/translate/docs)
* Google Elevation Api [Docs](https://developers.google.com/maps/documentation/elevation/start)
* Google Directions Api [Docs](https://developers.google.com/maps/documentation/directions/intro)
* Google Timezone Api [Docs](https://developers.google.com/maps/documentation/timezone/start)
* Google Places Api [Docs](https://developers.google.com/places/web-service/intro)

## Example
googleapi example using googleapi.places
```python
import googleapi

key = "Google api key"
place = googleapi.places(auth=key, place="Renwick Gallery of the Smithsonian American Art Museum, Washington")

#download image from photos.
placePhoto = place.photo(auth=key, download=True)
```
Downloaded image saved as "photoreference.jpg"
![photoreference](https://user-images.githubusercontent.com/57685626/76582781-9f1fc280-64ad-11ea-8c19-71f0f46e5a1a.jpg)
