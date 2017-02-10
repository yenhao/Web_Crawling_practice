from selenium import webdriver
from bs4 import BeautifulSoup


url = "http://www.chrisburkard.com"

driver = webdriver.Firefox()
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")

sel_soup = BeautifulSoup(html, 'html.parser')

images = []
for i in sel_soup.findAll("img"):
	print(i)
	src = i["src"]
	images.append(src)

print(images)
