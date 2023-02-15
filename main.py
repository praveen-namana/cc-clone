
import requests
import urllib.request

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import time
import random
from random import choice
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chromedriver_py import binary_path

# start web browser

def gen_html(url , file_path ,page_type):
    
# get source" code
    option = webdriver.ChromeOptions()
            
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--disable-gpu')
    option.add_argument('--no-sandbox')
    option.add_argument("--lang=hi")
    # option.add_argument('headless')
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {
        "translate_whitelists": {'en-US':'hi'},
       "translate":{"enabled":"true"}}
    option.add_experimental_option("prefs", prefs)

    # option.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser=webdriver.Chrome(service=Service(binary_path),options=option)
    browser.maximize_window()
    browser.get(url)
    
    try:
    # right_click_ele = browser.find_element(By.ID,f"//input[contains(@id, page-{page_type})")
        right_click_ele = browser.find_element(By.CLASS_NAME,"sticky-footer")
        actions = ActionChains(browser)
    #perform  right click
        # actions.context_click(right_click_ele).perform()
        # time.sleep(5)
     #   actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actions.context_click(right_click_ele).perform()
        # print(browser.window_handles)
        # time.sleep(3)
    
        # whandle = browser.window_handles[1]
        # actions_n = ActionChains(whandle)
        # actions_n.key_down(Keys.ARROW_DOWN).perform()
        #act.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).click()
        #actions.move_by_offset
        #actions.key_down(Keys.ARROW_DOWN).perform()
        
       # actions.scroll_to_element("Inspect")
        time.sleep(5)
        #option = browser.find_element(By.XPATH,"//div[text()='Inspect']")
        #option.click()
        #actions.context_click(right_click_ele).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).sendKeys(Keys.RETURN).build()

        # for i in range(8):
        #     actions.context_click(right_click_ele).send_keys(Keys.ARROW_DOWN).click().perform()
        import pyautogui as p
        for i in range(8):
            p.press('down')
        p.press('enter')
        # for s in range(20):
        #     p.scroll(s*10)
        #     time.sleep(0.5)
        time.sleep(2)
        last_height = browser.execute_script("return document.body.scrollHeight")

        for i in range(0,last_height,200):
            browser.execute_script(f"window.scrollTo(0, {i})")
            time.sleep(1)
        time.sleep(2)
        
        html = browser.page_source

        time.sleep(2)
        #print(html)

        # close web browser
        browser.close()
        import os
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        f = open(file_path, 'w',encoding="utf-8")
        f.write(html)
    except Exception as e:
        print(e)
        return

from bs4 import BeautifulSoup
soup = BeautifulSoup(open('index.html','r',errors='ignore').read(),'html.parser')
hh = []
for a in soup.find_all('a', href=True):
    hh.append(a.get('href'))
    #print("Found the URL:", a['href'])
final=[]
for i in hh:
    if 'classcentral.com' not in i:
        final.append(i)

import uuid  
name_spaces = uuid.NAMESPACE_DNS
final = final[::-1]
print(len(final))
kkkl = open('logs.txt', 'a')
i=0
# gen_html('https://www.classcentral.com/university/stanford','templates/index_stand.html')
for ll in final:
    try:
        if len(ll)>2 and 'htmlfiles' not in ll:
            print('starting',ll,'current',i)
            kk = f"https://www.classcentral.com{ll}"
            data =  ll.split('/')
            hhh = uuid.uuid3(name_spaces,ll)
            lll = str(hhh).replace('-', '')
            kkkl.write(f'{lll},{ll}')
            kkkl.write('\n')
            da = open('index.html','r',errors='ignore').read()
            lk = da.replace(ll,f'htmlfiles/{lll}.html')
            lm = open('index.html','w')
            lm.write(lk)
            gen_html(kk,f'htmlfiles/{lll}.html',data[1][:-4])
            i+=1
    except:
        pass

# print(len(final))

def modify_href():
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(open('index.html','r',errors='ignore').read(),'html.parser')
    hh = []
    for a in soup.find_all('a', href=True):
        ll = str(a.get('href')).replace('https://www.classcentral.com','')
        ll = ll.split('.html')
        da = open('index.html','r',errors='ignore').read()
        for i in ll:
            if 'htmlfiles' in i:
                fi = i
                
                lk = da.replace(str(a.get('href')),f'{fi}.html')
                lm = open('index.html','w')
                lm.write(lk)
                break