import os
import requests
import shutil
import time
from selenium import webdriver
from bs4 import BeautifulSoup


url = "URL"

driver = webdriver.Firefox()
driver.get(url)


# get current working directary
current_path = os.getcwd()

iterations = 0
while iterations < 10:
    html = driver.execute_script("return document.documentElement.outerHTML")
    sel_soup = BeautifulSoup(html, 'html.parser')
    # This is the images src list
    images = []
    for i in sel_soup.findAll("img"):
        print(i)
        src = i["src"]
        images.append(src)
    

    for img in images:
        try:
            filename = os.path.basename(img)
            img_r = requests.get(img, stream = True)
            new_path = os.path.join(current_path, "images",filename)

            if not os.path.exists('images/'): os.makedirs('images/')
            with open(new_path, "wb") as out_file:
                shutil.copyfileobj(img_r.raw, out_file)
            del img_r
        except:
            pass
    iterations +=1
    time.sleep(5)