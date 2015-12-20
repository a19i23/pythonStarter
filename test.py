import urllib2
import json

locu_api = '6252bab312fd63a8b43f273bbbc5b8ae973d9822'

url = 'https://api.locu.com/v1_0/venue/search/?has_menu=TRUE&locality=Austin&api_key=6252bab312fd63a8b43f273bbbc5b8ae973d9822'
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

print data
