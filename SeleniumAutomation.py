from selenium import webdriver
import os.path
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
# chrome_options = Options()
# driver = webdriver.Chrome(executable_path= path.abspath("chromedriver"), chrome_options=chrome_options)

# site: https://www.e-access.att.com/dws/dwsPortal/listReport.do UserID: XD17669126 Password: NewPasswordRequirement
#options = webdriver.FirefoxOptions()
chromeoptions = {"download.default_directory": "C:\Downloads\AttDashboard"}
options = webdriver.ChromeOptions()

# options.add_argument("download.default_directory=c:/Downloads/AttDashboard")
# options.add_argument("browser.download.folderList", 2)
# options.add_argument("browser.helperApps.neverAsk.openFile", "application/zip")
# options.add_argument("browser.helperApps.neverAsk.saveToDisk", "application/zip")
# options.add_argument("browser.download.useDownloadDir", "C:\Downloads\AttDashboard")
# options.add_argument('browser.download.dir', "C:\Downloads\AttDashboard")

options.add_experimental_option("prefs", chromeoptions)


# profile = webdriver.FirefoxProfile()
# profile = webdriver.Ch

# options.set_preference("browser.download.folderList", 2)
# options.set_preference("browser.helperApps.neverAsk.openFile", "application/zip")
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
# options.set_preference("browser.download.useDownloadDir", "C:\Downloads\AttDashboard")
# options.set_preference('browser.download.dir', "C:\Downloads\AttDashboard")



# profile.set_preference("browser.download.dir", "/home/i-06/Downloads")

#driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile)
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(50)

driver.get("https://www.e-access.att.com/dws/dwsPortal/listReport.do")
useridelem = driver.find_element_by_xpath('//*[@id="lrrFormId"]/table[3]/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td/input')
useridelem.send_keys("XD17669126")

passwordelem = driver.find_element_by_xpath('//*[@id="lrrFormId"]/table[3]/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[3]/td/input')
passwordelem.send_keys("NewPasswordRequirement")

driver.find_element_by_xpath('//*[@id="lrrFormId"]/table[3]/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/input').click()

driver.find_element_by_xpath('//*[@id="srv_successok"]/input').click()



# try:
  #  acknowledgeelem = WebDriverWait(driver, 50).until(
   #     EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/input')))

#finally:
 #       elem1 = ""
acknowledgeelem = driver.find_element_by_xpath(
    '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/input').click()
loginelem = driver.find_element_by_xpath(
    '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/form/table[2]/tbody/tr[2]/td/input[1]').click()

#try:
 #   reportselem = WebDriverWait(driver, 50).until(
  #      EC.presence_of_element_located((By.XPATH, '/html/body/table[1]/tbody/tr[5]/td[2]/a[2]')))
reportselem = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[5]/td[2]/a[2]').click()
salesselection = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/form/table[2]/tbody/tr[2]/td[2]/select/option[5]').click()

#finally:
#        elem1 = ""

currentmonthelem = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td[7]')
print(currentmonthelem.text)

currentmonthinputcheckbox = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td[1]/input').click()

currentelemdownload = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr/td[1]/table/tbody/tr/td/input').click()
fileexists = False
my_file = 'C:/Downloads/AttDashboard/*.zip'
while not fileexists:
    if os.path.isfile(my_file):
        fileexists = True
driver.close()
