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
	print(titles[0].text.strip(' \n\t\r'))
	
	#This have multi line
	address = business.findAll('address')[0].contents
	total_address = ''
	for line in address:
		if "br" in str(line):
			total_address += line.getText().strip(' \n\t\r')
		else:
			total_address += line.strip(' \n\t\r')
	print(total_address)
	phone = business.findAll('span', {'class':'biz-phone'})[0].text
	print(phone.strip(' \n\t\r'))
	print()
