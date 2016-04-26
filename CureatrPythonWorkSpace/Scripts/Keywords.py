import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import Config
from Config import *
import time

def LaunchWebBrowser(browser, driver, target, data):
	try:
		if browser=="FF":
			driver = webdriver.Firefox()
			print "Firefox opened"
		elif browser=="Chrome":
			driver = webdriver.Chrome()
			print "Chrome opened"
		elif browser=="IE":
			driver = webdriver.Chrome()
			print "IE/Chrome opened"
		return driver, "PASS"
	except Exception as err:
		print (Exception, err)
		return driver, "FAIL"


def OpenWebApp(browser, driver, target, data):
	try:
		driver.get(getattr(Config, str(target)))
		driver.implicitly_wait(20)
		return "PASS"
	except Exception as err:
		print (Exception, err)
		return "FAIL"

def Type(browser, driver, target, data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		element.send_keys(str(data))
		return "PASS"
	except Exception as err:
		print (Exception, err)
		return "FAIL"

def Maximize(browser, driver, target, data):
	try:
		driver.maximize_window()
		return "PASS"
	except Exception as err:
		print (Exception, err)
		return "FAIL"
		
def Click(browser, driver, target, data):
	try:
		a=driver.find_element_by_xpath(getattr(Config, str(target)))
		a.click()
		return "PASS"
	except Exception as err:
		print (Exception, err)
		return "FAIL"

def CloseWebApp(browser, driver, target, data):
	try:
		time.sleep(10)
		driver.close()
		driver.quit()
		return "PASS"
	except Exception as err:
		print (Exception, err)
		return "FAIL"
		
def verifyTitle(browser, driver, target, data):
	try:
		if data== driver.title:
			return "PASS"
		else:
			return "FAIL"
	except Exception as err:
		print (Exception, err)
		return "FAIL"