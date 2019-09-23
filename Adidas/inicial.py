from selenium import webdriver
from config import keys
import time

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper



driver = webdriver.Chrome('google/chromedriver')
driver.get(keys['product_url'])
#proposal_origin__flA-p gl-link
time.sleep(.10)

driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div/div/div[2]/a/strong').click() # OPCAO BR E AU
#driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div/ol/li[2]/a').click()  #HOME
driver.find_element_by_css_selector('.gl-cta.gl-cta--primary.gl-cta--full-width.btn-bag').click() # click add to bag
time.sleep(5)
driver.refresh()
#click sacola
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div[2]/a').click() # sacola
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[1]/div[1]/div[2]/div[1]/form/fieldset/button').click() #checkout


#form

driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[1]/div/input').send_keys(keys['name'])
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[2]/div/input').send_keys(keys['lastname'])
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[3]/div/input').send_keys(keys['company_name'])
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[4]/div/input').send_keys(keys['apt'])
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[5]/div/input').send_keys(keys['street_no'])
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[6]/div/input').send_keys(keys['street_address']) 
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[7]/div/input').send_keys(keys['suburb'])


driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[9]/div[1]/input').send_keys(keys['zip_code'])
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[11]/div[1]/input').send_keys(keys['phone_number'])


driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div[2]/div[1]/div/input').send_keys(keys['email'])
#state
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[8]/div/div").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/div[1]/div[8]/div/div/div/div/div[2]/div/ul/li[4]/span").click()
#review & pay
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div[4]/div[1]/button[1]').click()
#payment method
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div[3]/div/div[1]/div/div[2]/form/fieldset/div[1]/div/div[1]/input").send_keys(keys['card_number'])
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div[3]/div/div[1]/div/div[2]/form/fieldset/div[3]/div[2]/div/div").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div[3]/div/div[1]/div/div[2]/form/fieldset/div[3]/div[2]/div/div/div/div/div[2]/div/ul/li[12]/span").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div[3]/div/div[1]/div/div[2]/form/fieldset/div[3]/div[3]/div/div/div/a").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div[3]/div/div[1]/div/div[2]/form/fieldset/div[3]/div[3]/div/div/div/div/div[2]/div/ul/li[9]/span").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div[3]/div/div[1]/div/div[2]/form/fieldset/div[4]/div[1]/input").send_keys(keys["card_cvv"])
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div[4]/div/button/span").click()
