import unittest 
from selenium import webdriver 
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
#Un TestCase se crea mediante la subclase unittest.TestCase. Creamos nuestra clase de Test y la definimos como unittest
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriverChrome\chromedriver.exe") #Ruta navegador Chrome
        driver = self.driver
        driver.implicitly_wait(10)

    def test_crear_cuenta(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://automationpractice.com/index.php")
        time.sleep(3)

        registro = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        registro.click()
        time.sleep(3)

        email_create = driver.find_element_by_id("email_create") 
        email_create.send_keys("evelio@yopmail.com") 
        time.sleep(3)
        
        signin = driver.find_element_by_id('SubmitCreate') 
        signin.click()
        time.sleep(3)

        title = driver.find_element_by_xpath('//*[@id="account-creation_form"]/div[1]/div[1]/div[1]/label')
        title.click()
        time.sleep(3)

        first_name = driver.find_element_by_id('customer_firstname')
        first_name.send_keys("Evelio")
        time.sleep(3)

        customer_lastname = driver.find_element_by_id('customer_lastname')
        customer_lastname.send_keys("Diaz")
        time.sleep(3)

        email = driver.find_element_by_id('email')
        email.clear()
        email.send_keys('evelio@yopmail.com')
        time.sleep(3)

        password = driver.find_element_by_id('passwd')
        password.send_keys('evelio2021*')
        time.sleep(3)

        days = driver.find_element_by_id('days')
        days.click()
        option1 = driver.find_element_by_xpath('//*[@id="days"]/option[5]')
        option1.click()
        time.sleep(3)

        months = driver.find_element_by_id('months')
        months.click()
        option2 = driver.find_element_by_xpath('//*[@id="months"]/option[8]')
        option2.click()
        time.sleep(3)

        years = driver.find_element_by_id('years')
        years.click()
        option3 = driver.find_element_by_xpath('//*[@id="years"]/option[28]')
        option3.click()
        time.sleep(3)

        newsletter = driver.find_element_by_id('newsletter')
        newsletter.click()
        time.sleep(3)

        #Your address

        first_name2 = driver.find_element_by_id('firstname')
        first_name2.clear()
        first_name2.send_keys("Evelio")
        time.sleep(3)

        customer_lastname2 = driver.find_element_by_id('lastname')
        customer_lastname2.clear()
        customer_lastname2.send_keys("Diaz")
        time.sleep(3)

        company = driver.find_element_by_id('company')
        company.send_keys("New Experience")
        time.sleep(3)

        address1 = driver.find_element_by_id('address1')
        address1.send_keys("Calle 22")
        time.sleep(3)

        city = driver.find_element_by_id('city')
        city.send_keys("Manizales")
        time.sleep(3)

        state = driver.find_element_by_id('id_state')
        state.click()
        option4 = driver.find_element_by_xpath('//*[@id="id_state"]/option[7]')
        option4.click()
        time.sleep(3)
        
        postcode = driver.find_element_by_id('postcode')
        postcode.send_keys("12345")
        time.sleep(3)

        country  = driver.find_element_by_id('id_state')
        country.click()
        option5 = driver.find_element_by_xpath('//*[@id="id_country"]/option[2]')
        option5.click()
        time.sleep(3)

        mobile = driver.find_element_by_id('phone_mobile')
        mobile.send_keys("300000000")
        time.sleep(3)

        register = driver.find_element_by_id('submitAccount')
        register.click()
        time.sleep(3)

        msje_confirmation = driver.find_element_by_xpath('//*[@id="center_column"]/p')
        text = msje_confirmation.text
        print(text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='Reportes', report_name='REGISTRO'))