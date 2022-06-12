import pytest
import time
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired_cap = {'os_version': '10', 'resolution': '1920x1080', 'browser': 'Firefox', 'browser_version': 'latest', 'os': 'Windows', 'name': 'BStack-[Python] Sample Test',  'build': 'BStack Build Number 1' }
    
#{'os_version': '10', 'resolution': '1920x1080', 'browser': 'Chrome', 'browser_version': 'latest', 'os': 'Windows', 'name': 'BStack-[Python] Sample Test','build': 'BStack Build Number 1' }
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):
 
    
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='https://magdalena_C2YphJ:FbjvuNPwTeCry3g5hxXs@hub-cloud.browserstack.com/wd/hub', desired_capabilities=desired_cap)
        
    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
      
    def testing(self):
        co = 0
        driver = self.driver
        driver.get("https://www.ncbi.nlm.nih.gov/")
        
        self.driver.set_window_size(1576, 922)   
        self.assertIn("National", driver.title)
        co=+1
 
        # locate element using name
        self.driver.find_element(By.ID, "database").click()
        dropdown = self.driver.find_element(By.ID, "database")
        dropdown.find_element(By.XPATH, "//option[. = 'Nucleotide']").click()
        assert "Nucleotide"  in driver.page_source
        co=+1
        
        
        # send data
        self.driver.find_element(By.ID, "term").click()
        self.driver.find_element(By.ID, "term").send_keys("zika 1950")
        assert "50" in driver.page_source
        self.driver.find_element(By.ID, "term").send_keys(Keys.ENTER)
        self.assertIn("Dengue", driver.title) 
        co=+1
        #chceckBLAST
        self.driver.find_element(By.ID, "ReportShortCut6").click()
        element = self.driver.find_element(By.LINK_TEXT, "Run BLAST")
        
        assert "blast" in driver.page_source
        co=+1

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "Run BLAST").click()
        self.driver.find_element(By.CSS_SELECTOR, "#blastButton1 > .blastbutton").click()
        co=+1
        elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "qorganism")))
        
        
        #choose organism
        self.driver.find_element(By.ID, "qorganism").click()
        self.driver.find_element(By.ID, "qorganism").send_keys("virus")
        assert "virus"  in driver.page_source

        self.driver.find_element(By.ID, "btnFilter").click()
        element = self.driver.find_element(By.ID, "btnFilter")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.vars["window_handles"] = self.driver.window_handles
        co=+1
    
        #choose record
        self.driver.find_element(By.CSS_SELECTOR, "#dtr_MZ008458 .dflSeq").click()
        self.vars["win2773"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win2773"])
        co=+1
            
        #search by id
        self.driver.find_element(By.ID, "term").click()
        assert "MZ008458.1" in driver.page_source
        self.driver.find_element(By.ID, "term").send_keys("MZ008458.1")
        self.driver.find_element(By.ID, "term").send_keys(Keys.ENTER)
        co=+1
        
        
        #choose CDS
        assert "CDS"  in driver.page_source
        self.driver.find_element(By.LINK_TEXT, "CDS").click()
        co=+1
        
        # find dengue virus family
        assert "Dengue"  in driver.page_source
        self.driver.find_element(By.LINK_TEXT, "Dengue virus 2").click()
        element = self.driver.find_element(By.LINK_TEXT, "Dengue virus 2")
        actions = ActionChains(self.driver)
        assert "2"  in driver.page_source
        actions.move_to_element(element).perform()
        co=+1
        
        #choosing diff 
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(6) strong").click()
        self.driver.find_element(By.LINK_TEXT, "Translation table 1 (Standard)").click()
        assert "Translation"  in driver.page_source
        assert "mitochonrial" not in driver.page_source
        co=+1
        
        #change format
        self.driver.find_element(By.LINK_TEXT, "Click here to change format").click()
        assert "format"  in driver.page_source
        co=+1
        #click on citation link
        self.driver.find_element(By.LINK_TEXT, "Clark-Walker and Weiller, 1994").click()
        assert "1994"  in driver.page_source
        assert "mitochondrial"  in driver.page_source
        co=+1
        #cite
        self.driver.find_element(By.CSS_SELECTOR, ".inner-wrap:nth-child(2) > .citation-button > .button-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".export-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".close-overlay:nth-child(1)").click()
        co=+1
        #add to favourites
        self.driver.find_element(By.ID, "sidebar-favorites-button-link").click()
        co=+1
        #back on start page
        self.driver.find_element(By.CSS_SELECTOR, ".logo > img").click()
        self.assertIn("Library", driver.title)
        
        co=+1
        #diffrent section
        self.driver.find_element(By.CSS_SELECTOR, ".learn > p").click()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, ".no_border > h2").click()
        co=+1
        
        #search for zika event
        self.driver.find_element(By.ID, "search_keywords").click()
        self.driver.find_element(By.ID, "search_keywords").send_keys("zika")
        self.driver.find_element(By.ID, "search_keywords").send_keys(Keys.ENTER)
        assert "Zika"  in driver.page_source
        co=+1
        
        #diff event
        self.driver.find_element(By.CSS_SELECTOR, ".wpem-main:nth-child(3) .wpem-icon-menu").click()
        self.driver.execute_script("window.scrollTo(0,1233.6134033203125)")
        self.driver.find_element(By.CSS_SELECTOR, ".wpem-event-box-col:nth-child(3) .wpem-heading-text").click()
        assert "Library" not in driver.title
        assert "Python"  in driver.page_source
        
        co=+1
        #diffrent page
        self.driver.find_element(By.LINK_TEXT, "NIH").click()
        assert "Health"  in driver.page_source
        assert "Nucleotide" not in driver.page_source
        co=+1
        
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        
        #subsection
        self.driver.find_element(By.LINK_TEXT, "Training at NIH").click()
        assert "Health"  in driver.page_source
        co=+1
        #search fo empty
        self.driver.find_element(By.NAME, "commit").click()
        assert "Please enter a search term in the box above." in driver.page_source
        assert "Test-text"  not in driver.page_source
        co=+1
        assert co >10
        

 
    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()
 
# execute the script
if __name__ == "__main__":
    unittest.main()