from fileinput import close
import unittest
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument('--headless')



class NypBot(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./drivers/chromedriver',options=opt)
        self.driver.get("http://www.nyp.org")

    def test_nyp_is_up(self):
        driver = self.driver
        self.assertIn('NewYork-Presbyterian',driver.title)

    def test_bot_is_working(self):
        driver = self.driver
        time.sleep(3)
        syllableFrame = driver.find_element_by_id('syllable-frame')
        driver.switch_to.frame(syllableFrame)
        syllableButton = driver.find_element_by_id('SyllableButton')
        syllableButton.click()
        time.sleep(3)
        closeButton = driver.find_element_by_class_name('CloseButton').is_displayed()
        self.assertTrue(closeButton)
        textArea = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/div[2]/div/textarea')
        textArea.send_keys('what age groups')
        time.sleep(5)
        results = driver.find_element_by_xpath('//*[@id="autocomplete-list"]/li[3]/button/span/span/span[3]')
        self.assertEqual(results.get_attribute('innerText'),' are most at risk for of serious symptoms from coronavirus?')
    
    def test_spanish_is_working(self):
        driver = self.driver
        syllableFrame = driver.find_element_by_id('syllable-frame')
        driver.switch_to.frame(syllableFrame)
        syllableButton = driver.find_element_by_id('SyllableButton')
        syllableButton.click()
        time.sleep(5)
        changeLanguage = driver.find_element_by_id('languageName')
        changeLanguage.click()
        time.sleep(5)
        sugerencias = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/div[4]/div/h2')
        self.assertEqual(sugerencias.get_attribute('innerText'),'SUGERENCIAS')

    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)