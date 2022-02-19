import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from bs4 import BeautifulSoup

options = Options()
#options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.



urls = []
url1 = "https://www.realtor.com/realestateandhomes-search/Pleasanton_CA/pg-"
url2 = "https://www.realtor.com/realestateandhomes-search/Livermore_CA/pg-"
url3 = "https://www.realtor.com/realestateandhomes-search/Dublin_CA/pg-"

for i in range(1, 5):
	urls.append(url1 + str(i))
for i in range(1, 7):
	urls.append(url2+ str(i))
for i in range(1, 6):
	urls.append(url3 + str(i))
random.shuffle(urls)



file = open("property_urls.txt", mode='a')

try:
    for url in urls:
        driver = webdriver.Chrome('/usr/local/bin/chromedriver' , chrome_options=options)
        print(url)
        driver.get(url)
        time.sleep(100)
        html = driver.execute_script("return document.documentElement.outerHTML")
        soup=BeautifulSoup(html,'lxml')
        for item in soup.select('.component_property-card'):
            a = item.find('a')
            try:
                if 'href' in a.attrs:
                    l = a.get('href')
                    print(l)
                    file.write(l + '\n')
            except:
                pass
        driver.quit()
finally:
    driver.quit()
