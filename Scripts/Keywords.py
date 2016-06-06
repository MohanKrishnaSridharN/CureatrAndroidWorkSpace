import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
import Config
from Config import *
import Constants
from Constants import *
import XlsxReader
from XlsxReader import *
import time
import os,sys
from DriverScript import logger,handler
import logging
import logging.handlers
import PIL
from PIL import ImageChops
from PIL import Image
from selenium.webdriver.common.keys import Keys
import BackEndDrivers


def LaunchWebBrowser(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if browser=="FF":
			#driver = webdriver.Firefox()
			cap=webdriver.DesiredCapabilities.FIREFOX
			driver=webdriver.Remote('http://192.168.73.1:5557/wd/hub', cap)
			return driver, "PASS"
		elif browser=="Chrome":
			cap=webdriver.DesiredCapabilities.CHROME
			driver=webdriver.Remote('http://192.168.73.1:5557/wd/hub', cap)
			#driver = webdriver.Chrome()
			#driver = webdriver.Chrome(executable_path="D:/CureatrPythonWorkSpace/chromedriver_win32/chromedriver.exe")
			return driver, "PASS"
		elif browser=="IE":
			cap=webdriver.DesiredCapabilities.INTERNETEXPLORER
			driver=webdriver.Remote('http://192.168.73.125:5558/wd/hub', cap)
			return driver, "PASS"
	except Exception as err:
		logger.info("Exception @ LaunchWebBrowser"+str(err))
		return driver, "FAIL"
def OpenWebApp(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if driver.current_url != CureatrPlayURL:
			driver.get(getattr(Config, str(target)))
			driver.implicitly_wait(10)
			Status=PageRefresh(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			if Status=="PASS":
				return "PASS", ""
			else:
				return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ OpenWebApp"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def Type(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		Text=element.get_attribute("value")
		if Text!="":
			element.clear()
		element.send_keys(str(data))
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Type"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def verifysearch(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		"""
		currentTestSuiteXLSPATH=subdirectory+"Web_SEARCH"+".xlsx"
		currentTestDataSheet=load_workbook(currentTestSuiteXLSPATH).get_sheet_by_name("ContactsSearch")
		print currentTestSuiteXLSPATH
		print currentTestDataSheet
		EMAILID=getCellValueBySheet(currentTestDataSheet, 2, "EMAILID")
		print "email id @ verify search",EMAILID
		"""

		TotalList=BackEndDrivers.qa_search3(str(data))
		UsersList=TotalList[0]
		for UsersLength in range(0, len(UsersList)):
			SingleUser=UsersList[UsersLength]
			if str(data).lower() in str(SingleUser.first_name).lower() or str(data).lower() in str(SingleUser.last_name).lower():
				Status="PASS"
			else:
				print "FAIL", str(data), str(SingleUser.first_name)
				Status="FAIL"

		GroupsList=TotalList[1]
		for GroupLength in range(0, len(GroupsList)):
			SingleGroup=GroupsList[GroupLength]
			if str(data).lower() in str(SingleGroup['name']).lower():
				Status="PASS"
			else:
				Status="FAIL"

		print "len(GroupsList)=",len(GroupsList)
		BESearchLength=len(UsersList)+len(GroupsList)
		element=driver.find_element_by_xpath(getattr(Config, target)[4])
		Text=element.get_attribute("value")
		if Text!="":
			element.clear()
		element.send_keys(str(data))
		time.sleep(5)
		List=driver.find_elements_by_xpath(getattr(Config, target)[0])
		print "before list length=",len(List)
		

		#BESearchLength=len(BackEndDrivers.qa_search3(str(data)))
		print "BESearchLength=",BESearchLength
		
		if BESearchLength==0 and len(List)==2:
			ListLength=len(List)-2
		else:
			ListLength=len(List)-1
		print "BESearchLength=", BESearchLength, "ListLength=",ListLength
		time.sleep(10)
		if BESearchLength==ListLength and Status=="PASS":
			return "PASS", ""
		else:
			return "FAIL", ""
	except Exception as err:
		print err
		logger.info("Exception @ Verify Search"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""


def TypeEMAILID(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if data =="":
			browser=""
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		Text=element.get_attribute("value")
		if Text!="":	
			element.clear()
		element.send_keys(str(browser)+str(data))
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ TypeEMAILID"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def Maximize(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		driver.maximize_window()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Maximize"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def Click(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		a=driver.find_element_by_xpath(getattr(Config, str(target)))
		a.click()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Click"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def ClickCss(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		a=driver.find_element_by_css_selector(getattr(Config, str(target)))
		a.click()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Click"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def CloseWebApp(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		time.sleep(3)#Need to comment this line
		driver.delete_all_cookies()
		#driver.delete_cookies()
		driver.get(getattr(Config, str("CureatrPlayURL")))
		a=driver.find_element_by_xpath(getattr(Config, str("ChangeOrg")))
		a.click()
		return "PASS", ""
	except Exception as err:
		try:
			Status=PageRefresh(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			a=driver.find_element_by_xpath(getattr(Config, str("ChangeOrg")))
			a.click()
			if Status=="PASS":
				return "PASS", ""
			else:
				return "FAIL", ""
		except:
			logger.info("Exception @ CloseWebApp"+str(err))
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""

def CloseBrowser(driver):
	try:
		driver.close()
		driver.quit()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ CloseBrowser"+str(err))
		return "FAIL", ""
		
def verifyAppTitle(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if data== driver.title:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyAppTitle"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		ScreenShotDirPath=subdirectory+"ScreenShots/"
		if not os.path.exists(ScreenShotDirPath):
			os.makedirs(ScreenShotDirPath)
		driver.get_screenshot_as_file(ScreenShotDirPath+TCID+"-"+TSID+"-"+DSID+'.jpg')
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ ScreenShot, "+str(err))
		return "Fail", ""

def isElementVisible(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		ui.WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str(target)))))
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ isElementVisible"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "Fail", ""

def PageRefresh(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	for i in range(3): 
		try:
			ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str("WelcomeMsg")))))
			return "PASS"
		except TimeoutException:
			driver.refresh()
			if i>3:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL"
			else:
				continue

def LinkState(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		ClassValue=element.get_attribute("class")
		if str(data)=="enabled":
			if "disabled" in ClassValue:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", ""
			else:
				return "PASS", ""
		else:
			if "disabled" in ClassValue:
				return "PASS", ""
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ LinkState"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyText(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element = driver.find_element_by_xpath(getattr(Config, str(target))).text
		element = element.encode('ascii', 'ignore').decode('ascii')
		if element==data:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyText"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyTextcss(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element = driver.find_element_by_css_selector(getattr(Config, str(target))).text
		if data in element:
			return "PASS", ""
		else:
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyTextcss"+str(err))
		return "FAIL", ""

def verifyErrorMsg(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if data!="":
			ui.WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str(target)))))
			element = driver.find_element_by_xpath(getattr(Config, str(target))).text
			if data in str(element):
				return "PASS", ""
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ verifyErrorMsg"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyTextContains(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element = driver.find_element_by_xpath(getattr(Config, str(target))).text
		if str(data).lower() in str(element).lower():
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyTextContains"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyOrgText(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element = driver.find_element_by_xpath(getattr(Config, str(target))).text
		StaticText="Sign in for "
		if element==StaticText+data:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyOrgText"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def SearchInstitution(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		List=driver.find_elements_by_xpath("//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li")
		for ListCount in range(1, len(List)+1):
			ActOrg=driver.find_element_by_xpath("//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li["+str(ListCount)+"]/div/div").text
			if str(ActOrg) in data:
				Status="PASS"
				break
					
		if Status=="PASS":
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ SearchInstitution"+str(err))
		return "FAIL", ""
		
def selectInstitution(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		List=driver.find_elements_by_xpath("//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li")
		for ListCount in range(1, len(List)+1):
			Status=""
			ActOrg=driver.find_element_by_xpath("//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li["+str(ListCount)+"]/div/div").text
			if str(ActOrg)==data:
				driver.find_element_by_xpath("//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li["+str(ListCount)+"]/div/div").click()
				Status="PASS"
				return "PASS", ""
		
		if Status=="":
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ selectInstitution"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def ClearText(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		element.clear()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ ClearText"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyTextBoxValue(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		TextBoxValue=element.get_attribute("value")
		if str(data) in str(TextBoxValue):
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyTextBoxValue"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def isEncrypted(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		FieldType=element.get_attribute("type")
		if FieldType=="password" and data=="TRUE":
			return "PASS", ""
		elif FieldType=="text" and data=="FALSE":
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ isEncrypted"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def isTextBoxWrapped(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		FieldType=element.get_attribute("type")
		GetTagName=element.tag_name
		if (FieldType=="password" or FieldType=="text") and GetTagName=="input":
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ isTextBoxWrapped"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyWaterMarkVailability(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		FieldType=element.get_attribute("placeholder")
		GetFieldValue=element.get_attribute("value")
		if data==FieldType+GetFieldValue:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyWaterMarkVailability"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyWaterMarkUnVailability(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		FieldType=element.get_attribute("placeholder")
		GetFieldValue=element.get_attribute("value")
		if data==FieldType+GetFieldValue:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ verifyWaterMarkUnVailability"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifySignIn(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if Correct_Data=="Y":
			element1 = driver.find_element_by_xpath(getattr(Config, "InboxLink")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "ContactsLink")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "YES"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", "NO"
		else:
			element1 = driver.find_element_by_xpath(getattr(Config, "WelcomeMsg")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "GetSupportLink")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "NO"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", "NO"
	except Exception as err:
		logger.info("Exception @ verifySignIn"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", "NO"

def verifySignOut(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element1 = driver.find_element_by_xpath(getattr(Config, "WelcomeMsg")).is_displayed()
		element2 = driver.find_element_by_xpath(getattr(Config, "GetSupportLink")).is_displayed()
		if element1==True and element2==True:
			return "PASS", "YES"
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", "NO"
	except Exception as err:
		logger.info("Exception @ verifySignOut"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", "NO"
		
def verifyFirstTimeSignIn(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if Correct_Data=="Y":
			element1 = driver.find_element_by_xpath(getattr(Config, "NewPasswordLabel")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "ReTypePasswordLabel")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "YES"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", "NO"
		else:
			time.sleep(5)
			element1 = driver.find_element_by_xpath(getattr(Config, "WelcomeMsg")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "GetSupportLink")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "NO"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", "NO"
	except Exception as err:
		logger.info("Exception @ verifyFirstTimeSignIn"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", "NO"
	
def verifyChangePassword(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if data=="Y":
			element1 = driver.find_element_by_xpath(getattr(Config, "TSSignOut")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "TSAccept")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "YES"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", "NO"
		else:
			time.sleep(5)
			element1 = driver.find_element_by_xpath(getattr(Config, "NewPasswordLabel")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "ReTypePasswordLabel")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "NO"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", "NO"
	except Exception as err:
		logger.info("Exception @ verifyChangePassword"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", "NO"

def wait(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		time.sleep(data)
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ wait"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def DriverWait(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		WebDriverWait(driver, 10).until(wait_for_text_to_start_with(By.find_element_by_xpath, getattr(Config, str(target)), data))
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ DriverWait"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def ImageComparision(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element = driver.find_element_by_xpath(getattr(Config, target))
		BasePath=element.value_of_css_property("background-image")
		ImageUrl=BasePath.split("\"")[1:][0]
		driver.get(ImageUrl)
		driver.get_screenshot_as_file(ActlogoFile)
		im1 = Image.open(ActlogoFile)
		im2 = Image.open(ExplogoFile)
		if ImageChops.difference(im1, im2).getbbox is None:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ ImageComparision"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyTermsofService(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		driver.switch_to.frame("tos_update_text")
		TSelement = driver.find_element_by_xpath(getattr(Config, str(target))).text
		TSelement = TSelement.encode('ascii', 'ignore').decode('ascii')
		ActFilePath=TOSFileDir+'ActFile.txt'
		OpenActFile = open(ActFilePath, 'w')
		OpenActFile.write(str(TSelement))
		OpenActFile.close()
		file1 = open(TOSFileDir+'ActFile.txt', 'r')
		file2 = open(TOSFileDir+'ExpFile.txt', 'r')
		f1_line = file1.readline()
		f2_line = file2.readline()
		while f1_line != '' or f2_line != '':
			f1_line = f1_line.rstrip()
			f2_line = f2_line.rstrip()
			if f1_line==f2_line:
				Status="pass"
			else:
				Status="FAIL"
				break
			f1_line = file1.readline()
			f2_line = file2.readline()
		
		if Status=="PASS":
			return "PASS", ""
		else:
			return "FAIl", ""
		file1.close()
		file2.close()
	except Exception as err:
		logger.info("Exception @ verifyTermsofService"+str(err))
		return "FAIL", ""

def Searchcontacts(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		time.sleep(5)
		List = driver.find_elements_by_xpath(getattr(Config, target)[0])
		Status=""
		print "len(List)=", len(List)
		for ListCount in range(1, len(List)+getattr(Config, target)[5]):
			name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
			title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
			print ListCount
			if str(data).lower() in str(name.encode('ascii', 'ignore').decode('ascii')).lower() or str(data).lower() in str(title.encode('ascii', 'ignore').decode('ascii')).lower():
				Status="PASS"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", ""
		
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Search Contacts Method:: "+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def selectContact(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		time.sleep(1)
		List = driver.find_elements_by_xpath(getattr(Config, target)[0])
		for ListCount in range(1, len(List)+getattr(Config, target)[5]):
			Status=""
			name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
			title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
			if str(data).lower() in name.lower() or str(data).lower() in title.lower():
				driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).click()
				Status="PASS"
				return "PASS", ""
		
		if Status=="":
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ selectInstitution"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def isVissible(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		if element.is_displayed():
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""  
  
def delLastchars(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, target)[4])
		element.clear()
		element.send_keys(data)
		GetFieldValue=element.get_attribute("value")
		while len(GetFieldValue) !=0:
			try:
				time.sleep(2)
				List = driver.find_elements_by_xpath(getattr(Config, target)[0])
				for ListCount in range(1, len(List)+getattr(Config, target)[5]):
					name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
					title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
					if GetFieldValue.lower()  in name.lower()  or GetFieldValue.lower()  in title.lower():
						Status="PASS"
					else:
						ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
						return "FAIL", ""
				element.send_keys(Keys.BACKSPACE)
				GetFieldValue=element.get_attribute("value")
			except Exception as err:
				element1=driver.find_element_by_xpath(getattr(Config, target)[6]).text
				if element1=="No contacts found" or element1=="No patients found" or element1=="No results found":
					element.send_keys(Keys.BACKSPACE)
					GetFieldValue=element.get_attribute("value")
					Status="PASS"
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
					return "FAIL", ""
					
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def AddCharByChar(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		for Count, Char in enumerate(data):
			try:
				element=driver.find_element_by_xpath(getattr(Config, target)[4])
				element.send_keys(str(Char))
				time.sleep(1)
				List = driver.find_elements_by_xpath(getattr(Config, target)[0])
				for ListCount in range(1, len(List)+getattr(Config, target)[5]):
					name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
					title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
					if str(Char).lower()  in name.lower()  or str(Char).lower()  in title.lower():
						Status="PASS"
					else:
						ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
						return "FAIL", ""
			except Exception as err:
				element1=driver.find_element_by_xpath(getattr(Config, target)[6]).text
				if element1=="No contacts found" or element1=="No patients found" or element1=="No results found":
					continue
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
					return "FAIL",""
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def delLastcharsManageGroup(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, target)[4])
		element.clear()
		element.send_keys(data)
		GetFieldValue=element.get_attribute("value")
		time.sleep(2)
		while len(GetFieldValue) !=0:
			List = driver.find_elements_by_xpath(getattr(Config, target)[0])
			if len(List)==0:
				element1=driver.find_element_by_xpath(getattr(Config, target)[6]).text
				if element1=="No results are available. Please check your search.":
					Status="PASS"
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
					return "FAIL", ""
			time.sleep(1)
			for ListCount in range(1, len(List)+getattr(Config, target)[5]):
				name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
				title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
				if GetFieldValue.lower()  in name.lower()  or GetFieldValue.lower()  in title.lower():
					Status="PASS"
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
					return "FAIL", ""
			element.send_keys(Keys.BACKSPACE)
			GetFieldValue=element.get_attribute("value")
					
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def AddCharByCharManageGroup(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		for Count, Char in enumerate(data):
			element=driver.find_element_by_xpath(getattr(Config, target)[4])
			element.send_keys(str(Char))
			time.sleep(1)
			List = driver.find_elements_by_xpath(getattr(Config, target)[0])
			if len(List)==0:
				element1=driver.find_element_by_xpath(getattr(Config, target)[6]).text
				if element1=="No results are available. Please check your search.":
					Status="PASS"
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
					return "FAIL", ""
			for ListCount in range(1, len(List)+getattr(Config, target)[5]):
				name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
				title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
				if str(Char).lower()  in name.lower()  or str(Char).lower()  in title.lower():
					Status="PASS"
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
					return "FAIL", ""
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def delLastcharsCoverageSearch(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, target)[4])
		element.clear()
		element.send_keys(data)
		GetFieldValue=element.get_attribute("value")
		while len(GetFieldValue) !=0:
			try:
				while len(GetFieldValue) !=0:
					time.sleep(5)
					List = driver.find_elements_by_xpath(getattr(Config, target)[0])
					for ListCount in range(1, len(List)+getattr(Config, target)[5]):
						name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
						title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
						if GetFieldValue.lower()  in name.lower()  or GetFieldValue.lower()  in title.lower():
							Status="PASS"
						else:
							ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
							return "FAIL", ""
					element.send_keys(Keys.BACKSPACE)
					GetFieldValue=element.get_attribute("value")
			except Exception as err:
				element1=driver.find_element_by_xpath(getattr(Config, target)[6]).text
				if element1=="No results are available. Please check your search.":
					element.send_keys(Keys.BACKSPACE)
					GetFieldValue=element.get_attribute("value")
					continue
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
					return "FAIL", ""
					
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def AddCharByCharCoverageSearch(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		for Count, Char in enumerate(data):
			try:
				element=driver.find_element_by_xpath(getattr(Config, target)[4])
				element.send_keys(str(Char))
				time.sleep(2)
				List = driver.find_elements_by_xpath(getattr(Config, target)[0])
				print "len(List)=", len(List)
				for ListCount in range(1, len(List)+getattr(Config, target)[5]):
					name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
					title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
					print ListCount
					if str(Char).lower()  in name.lower()  or str(Char).lower()  in title.lower():
						Status="PASS"
					else:
						ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
						return "FAIL", ""
			except Exception as err:
				element1=driver.find_element_by_xpath(getattr(Config, target)[6]).text
				time.sleep(5)
				if element1=="No results are available. Please check your search.":
					continue
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
					return "FAIL",""
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""