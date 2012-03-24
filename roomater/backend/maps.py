from models import Room
import urllib
import simplejson as json

api_address_0 = "http://maps.googleapis.com/maps/api/geocode/json?address="
api_address_1 = "&sensor=false"

zap = "http://api.zappos.com/Search/term/mens%20pants?limit=100&page=1&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de"

def geo_code(address, city):
    link = str(api_address_0+address+city+api_address_1)
    open = urllib.urlopen(link)
    result = json.load(open)
    try:
        lat = result['results'][0]['geometry']['location']['lat']
        lng = result['results'][0]['geometry']['location']['lng']
    except:
        lat = 33.935728
        lng = -122.106486100
    list = [lat, lng]
    return list

