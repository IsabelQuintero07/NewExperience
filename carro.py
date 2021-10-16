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

    def test_carro(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://automationpractice.com/index.php")
        time.sleep(3)

        registro = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        registro.click()
        time.sleep(3)

        email = driver.find_element_by_id("email")
        email.send_keys("isabel@yopmail.com") 

        password = driver.find_element_by_name("passwd")
        password.send_keys("12345")

        signin = driver.find_element_by_id('SubmitLogin')
        signin.click()

        search = driver.find_element_by_id('search_query_top')
        search.send_keys("dress")
        search.send_keys(Keys.ENTER)
        time.sleep(3)

        image = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img')
        image.click()
        time.sleep(3)

        ##
        addcart = driver.find_element_by_xpath('//*[@id="add_to_cart"]/button')
        addcart.click()

        checkout = driver.find_element_by_class_name('button-medium')
        checkout.click()
        time.sleep(3)

        summary = driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]')
        summary.click()
        time.sleep(3)

        adrres = driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button/span')
        adrres.click()
        time.sleep(3)

        termsservice = driver.find_element_by_id('cgv')
        termsservice.click()
        time.sleep(3)

        shipping = driver.find_element_by_xpath('//*[@id="form"]/p/button/span')
        shipping.click()
        time.sleep(3)

        paybybankwire = driver.find_element_by_xpath('//*[@id="HOOK_PAYMENT"]/div[1]/div/p')
        paybybankwire.click()
        time.sleep(3)

        confirm_order = driver.find_element_by_xpath('//*[@id="cart_navigation"]/button')
        confirm_order.click()
        time.sleep(3)   

        msje_confirmation = driver.find_element_by_xpath('//*[@id="center_column"]/div/p/strong')
        text = msje_confirmation.text
        print(text)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='Reportes', report_name='CARRO'))