from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options --> De invatat
import time


# --Section 1: This connects the Chrome browser with selenium using chromeDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get(" ")


'''
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.XPATH,"//*[contains(text(),'Tee')]"))
)
'''


# --Section 2:  Finding the first tee on the page, selecting the colour and size
btn_tee = driver.find_element(By.XPATH,"//*[contains(text(),'Tee')]")
print("Element is visible?"+str(btn_tee.is_displayed()))
#btn_tee = driver.find_element(By.CLASS_NAME,"aria-label=Lollipop Tee product link")
btn_tee.click()

time.sleep(0.5) #Are nevoie de timp pentru a se incarca culoarea

colour = driver.find_element(By.XPATH,"//button[contains(@title,'White')]")
print("Element is visible?"+str(colour.is_displayed()))
colour.click()

time.sleep(0.3)

size = driver.find_element(By.XPATH,"//select/option[contains(text(),'Large')]")
print("Element is visible?"+str(size.is_displayed()))
size.click()

start_time = time.time()



# --Section 3: Finding the checkout and submiting the form
add_bag = driver.find_element(By.XPATH,"//button[contains(text(),'add to cart')]").click()

WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.XPATH,"//span[contains(text(),'checkout')]"))
)

#if find high traffic reload the page..........
checkout = driver.find_element(By.XPATH,"//span[contains(text(),'checkout')]").click()

#WebDriverWait(driver,120).until(
#    EC.presence_of_all_elements_located((By.ID,"accept-tos"))
#)

button = driver.find_element(By.ID,"accept-tos")
if button.is_displayed() == False:
    driver.refresh()
else:
    button.click()

email = driver.find_element(By.NAME,"email")
email.click()
email.send_keys("tudorpantofaru@gmail.com")

country_code = driver.find_element(By.NAME,"countryCode").click()
country = driver.find_element(By.XPATH,"//select/option[contains(text(),'Romania')]").click()

random_button = driver.find_element(By.ID,"shipping-methods")
random_button.click()

time.sleep(0.3)

county = driver.find_element(By.XPATH,"//select/option[contains(text(),'Neam')]").click()

time.sleep(0.3)

driver.execute_script("document.getElementsByName('firstName')[0].value='Pantofaru';")
driver.execute_script("document.getElementsByName('lastName')[0].value='Tudor';")
driver.execute_script("document.getElementsByName('address1')[0].value='Strada 1 Decembrie 1918, nr 61';")
driver.execute_script("document.getElementsByName('postalCode')[0].value='610219';")
driver.execute_script("document.getElementsByName('city')[0].value='Piatra Neamt';")
driver.execute_script("document.getElementsByName('phone')[0].value='0771052736';")






end_time = time.time()
print(end_time - start_time)
time.sleep()