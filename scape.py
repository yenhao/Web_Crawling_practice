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

businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})

for business in businesses:
	titles = yelp_soup.findAll('a', {'class': 'biz-name'})
	#for title in titles:
	print(titles[0].text)
	address = business.findAll('address')[0].text
	print(address)
	phone = business.findAll('span', {'class':'biz-phone'})[0].text
	print(phone)
	print()
