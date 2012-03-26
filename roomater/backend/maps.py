from models import Room
import urllib
import simplejson as json

api_address_0 = "http://maps.googleapis.com/maps/api/geocode/json?address="
api_address_1 = "&sensor=false"

zap = "http://api.zappos.com/Search/term/mens%20pants?limit=100&page=1&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de"

def geo_code(address, city, state, zip):
    link = str(api_address_0+address+city+state+zip+api_address_1)
    open = urllib.urlopen(link)
    result = json.load(open)
    try:
        lat = result['results'][0]['geometry']['location']['lat']
        lng = result['results'][0]['geometry']['location']['lng']
    except:
<<<<<<< HEAD
        lat = 37.77493
        lng = -122.419416
=======
        lat = 37.92977070
        lng = -122.32791480
>>>>>>> jack
    list = [lat, lng]
    return list
