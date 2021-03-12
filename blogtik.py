from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
req_proxy = RequestProxy() 
proxies = req_proxy.get_proxy_list() #Proxy

PATH = "Chrome Driver Lokasyonu"
driver = webdriver.Chrome(PATH)

while 1:
    driver.get("Site Adresi")
    print(driver.title)