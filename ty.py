import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select




from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.maximize_window()

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver.get("https://facebook.com")
sleep(2)


email=driver.find_element_by_id("email")
email.send_keys("100054592715360")
password=driver.find_element_by_id("pass")
password.send_keys("chidozie")
sleep(1)
login=driver.find_element_by_name("login")
login.click()
sleep(4)

i = 1

while i<=5:
 groups_links_list = [
    "https://www.facebook.com/groups/3686706161407106", "https://www.facebook.com/groups/2782001165164383"
    ]


 for group in groups_links_list:
    driver.get(group)
    sleep(4)
       
    
    driver.execute_script("window.scrollTo(0, 200)")
    postbox = driver.find_element_by_xpath("//div[@class='oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl orhb3f3m czkt41v7 fmqxjp7s emzo65vh l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn btwxx1t3 buofh1pr idiwt2bm jifvfom9 kbf60n1y']")
    postbox.click()
    sleep(4)

    

    element = driver.switch_to.active_element
    sleep(3)
    element.send_keys("If you wish to invest in bitcoin today we will help you .")
    sleep(5)

    postbutton = driver.find_element_by_xpath("//div[@aria-label='Post']")
    sleep(1)
    postbutton.click()
    sleep(10)

    i=i+1
    








  