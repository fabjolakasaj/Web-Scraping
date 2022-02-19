import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
options = Options()
#options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome('/usr/local/bin/chromedriver' , chrome_options=options)



total_x = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div/main/section[1]/div[2]/div[1]/div[1]/span'
beds_x = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div/main/section[1]/div[2]/div[1]/div[2]/ul/li[1]/span[1]'

baths_x = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div/main/section[1]/div[2]/div[1]/div[2]/ul/li[2]/span[1]'
sq_x = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div/main/section[1]/div[2]/div[1]/div[2]/ul/li[3]/span[1]'
lot_x = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div/main/section[1]/div[2]/div[1]/div[2]/ul/li[4]/span[1]'

add_x = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div/main/section[1]/div[2]/div[1]/div[3]/h1'
types_x = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div/main/section[1]/div[4]/ul/li[1]/div/span[2]'
built_x = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div/main/section[1]/div[4]/ul/li[4]/div/span[2]'
price_x = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div/main/section[1]/div[4]/ul/li[5]/div/span[2]'
garage_x = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div/main/section[1]/div[4]/ul/li[6]/div/span[2]'


high_school_x = '//*[@id="content-nearby_schools"]/table/tbody/tr[1]/td[1]/span/span'
mid_school_x = '//*[@id="content-nearby_schools"]/table/tbody/tr[2]/td[1]/span/span'
ele_school_x = '//*[@id="content-nearby_schools"]/table/tbody/tr[3]/td[1]/span/span'

value_x = '//*[@id="content-home_value"]/section/section[2]/div/div/table'


def convertValue(s):
    s = s.replace(',', '')
    res = ''
    for v in s.split():
        if '$' in v or '—' in v:
            res = res+' '+ v
    return res

def func():
    html = driver.execute_script("return document.documentElement.outerHTML")

    t1= b2= b3= s4= l5= p6= t7= b8= g9= a10= e13= m14= h15= v16 = None

    try:
        t1 = driver.find_element_by_xpath(total_x)
    except:
        pass
    try:
        b2 = driver.find_element_by_xpath(beds_x)
    except:
        pass
    try:
        b3 = driver.find_element_by_xpath(baths_x)
    except:
        pass
    try:
        s4 = driver.find_element_by_xpath(sq_x)
    except:
        pass
    try:
        l5 = driver.find_element_by_xpath(lot_x)
    except:
        pass
        time.sleep(0.2)
    try:
        p6 = driver.find_element_by_xpath(price_x)
    except:
        pass
    try:
        t7 = driver.find_element_by_xpath(types_x)
    except:
        pass
    try:
        b8 = driver.find_element_by_xpath(built_x)
    except:
        pass
    try:
        g9 = driver.find_element_by_xpath(garage_x)
    except:
        pass
        time.sleep(0.2)
    try:
        a10 = driver.find_element_by_xpath(add_x)
    except:
        pass
        # c10 = driver.find_element_by_xpath(city_x)
        # s11 = driver.find_element_by_xpath(state_x)
        # z12= driver.find_element_by_xpath(zip_x)
        time.sleep(0.2)
    try:
        e13 = driver.find_element_by_xpath(ele_school_x)
        m14 = driver.find_element_by_xpath(mid_school_x)
        h15 = driver.find_element_by_xpath(high_school_x)
    except:
        pass
        time.sleep(0.2)
    try:
        v16 = driver.find_element_by_xpath(value_x)
    except:
        pass




    d = {'total': '',
    'bed': '',
    'bath': '',
    'square': '',
    'lot': '',
    'price': '',
    'type': '',
    'built': '',
    'garage': '',
    'address': '',
    'city': '',
    'state': '',
    'zip': '',
    'elementary school': '',
    'middle school': '',
    'high school': '',
    'Estimate info': '',
    'Collateral': '',
    'CoreLogic': '',
    'Quantarium':''}

    if t1:
        d['total'] = t1.text.replace(',', '').replace('\n', '')
    if b2:
        d['bed'] = b2.text.replace(',', '').replace('\n', '')
    if b3:
        d['bath'] = b3.text.replace(',', '').replace('\n', '')
    if s4:
        d['square']  = s4.text.replace(',', '').replace('\n', '')
    if l5:
        lot_value = l5.text.replace(',', '').replace('\n', '')
        if(float(lot_value) < 5):
            lot_value = int(float(lot_value)* 43560)
        d['lot'] = str(lot_value)
    if p6:
        d['price'] = p6.text.replace(',', '').replace('\n', '')
    if t7:
        d['type'] = t7.text.replace(',', '').replace('\n', '')
    if b8:
        d['built'] = b8.text.replace(',', '').replace('\n', '')
    if g9:
        d['garage'] = g9.text.replace(',', '').replace('\n', '')
    if a10:
        tup  = a10.text.split(',')
        d['address'] = tup[0]
        d['city'] = tup[1]
        d['state'] = tup[2]
        d['zip'] = tup[3]
    if e13:
        d['elementary school'] = e13.text
    if m14:
        d['middle school'] = m14.text
    if h15:
        d['high school'] = h15.text
    if v16:
        value_text= v16.text.split('\n')
        if len(value_text) > 1:
            for i, e in enumerate(value_text):
                if 'Quantarium' in e:
                    d['Quantarium'] = convertValue(value_text[i+1])
                if 'CoreLogic' in e:
                    d['CoreLogic'] = convertValue(value_text[i+1])
                if 'Collateral' in e:
                    d['Collateral'] = convertValue(value_text[i+1])
                d['Estimate info'] = value_text[1].replace(',', '')



    print(d)

    with open('mycsvfile.csv', 'a') as f:
        w = csv.DictWriter(f, d.keys())
        w.writerow(d)

while True:
    url = next(iter(urls))
    driver.get(url)
    time.sleep(50)
    e = driver.find_element_by_xpath('//*[@id="content-home_value"]/section/section[2]/button/div/div')
    e.click()
    time.sleep(10)
    func()
