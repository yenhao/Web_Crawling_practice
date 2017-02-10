import requests
from bs4 import BeautifulSoup

based_url = "https://www.yelp.com/search?find_desc="
loc_url = "&find_loc="

find_what= "Restaurants"
location = "Hsinchu"

url = based_url + find_what + loc_url + location

yelp_r = requests.get(url)

#200
#print(yelp_r.status_code)

yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

#print(yelp_soup.prettify())

for link in yelp_soup.findAll('a', {'class': 'biz-name'}):
	print(link.text)
