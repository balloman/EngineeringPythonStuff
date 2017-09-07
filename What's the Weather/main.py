import simplejson as json
import requests
from urllib import urlopen

url = urlopen('http://api.openweathermap.org/data/2.5/forecast/daily?zip=35613,us&APPID=2b4bb0388f506b5ea4ee3a7e514a8b43&cnt=7&units=imperial').read()

five_day = json.loads(url)

print five_day