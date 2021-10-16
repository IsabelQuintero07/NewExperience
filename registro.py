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

    def test_registro(self):
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

        msje_confirmation = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span')
        text = msje_confirmation.text
        print(text)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='Reportes', report_name='REGISTRO'))