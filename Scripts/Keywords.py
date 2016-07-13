import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
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
from itertools import izip
from selenium.webdriver.common.keys import Keys
import BackEndDrivers
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyPdf import PdfFileReader

def LaunchWebBrowser(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		if browser=="FF":
			profile = webdriver.FirefoxProfile("/home/cureatr/CureatrPythonWorkSpace/Images/pey75pqn.Cureatr_Profile")
			#profile.set_preference('browser.download.folderList', 2)
			#profile.set_preference('browser.download.manager.showWhenStarting', False)
			#profile.set_preference('browser.download.dir', os.getcwd())
			#profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain;application/octet-stream;application/vnd.ms-excel;application/pdf;audio/mpeg3;application/x-pdf')
			#profile.set_preference('browser.helperApps.neverAsk.openFile', 'application/pdf;application/x-pdf')	
			desired_capabilities=webdriver.DesiredCapabilities.FIREFOX
			desired_capabilities['firefox_profile'] = profile.encoded
			#driver=webdriver.Remote('http://192.168.73.1:5557/wd/hub', cap, browser_profile=profile.update_preferences())
			driver=webdriver.Remote('http://192.168.73.1:5557/wd/hub', desired_capabilities)
			return driver, "PASS"
		elif browser=="Chrome":
			"""
			cap = webdriver.ChromeOptions()
			cap.add_argument={'prefs': {'download': {'default_directory': '/home/cureatr/CureatrPythonWorkSpace/Images/'}}}
			driver=webdriver.Remote('http://192.168.73.1:5557/wd/hub', cap)
			driver = webdriver.Chrome(chrome_options=cap)
			"""
			chromeOptions = webdriver.ChromeOptions()
			prefs = {"download.default_directory" : "/Users/macmini/Cureatr/CureatrPythonWorkSpace/Images/"}
			chromeOptions.add_experimental_option("prefs",prefs)
			#chromeOptions.add_experimental_option("download.default_directory", "/Users/macmini/Cureatr/CureatrPythonWorkSpace/Images/")
			desired_capabilities=webdriver.DesiredCapabilities.CHROME
			desired_capabilities=chromeOptions.to_capabilities()
			driver=webdriver.Remote('http://192.168.73.1:5557/wd/hub', desired_capabilities)

			#driver = webdriver.Chrome()
			#driver = webdriver.Chrome(executable_path="D:/CureatrPythonWorkSpace/chromedriver_win32/chromedriver.exe")
			return driver, "PASS"
		elif browser=="IE":
			if user=="user1":
				cap=webdriver.DesiredCapabilities.INTERNETEXPLORER
				driver=webdriver.Remote('http://192.168.73.137:5558/wd/hub', cap)
				return driver, "PASS"
			else:
				cap=webdriver.DesiredCapabilities.CHROME
				driver=webdriver.Remote('http://192.168.73.137:5558/wd/hub', cap)
				#driver = webdriver.Chrome()
				#driver = webdriver.Chrome(executable_path="D:/CureatrPythonWorkSpace/chromedriver_win32/chromedriver.exe")
				return driver, "PASS"
	except Exception as err:
		print err
		logger.info("Exception @ LaunchWebBrowser"+str(err))
		return driver, "FAIL"

def OpenWebApp(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		if driver.current_url != CureatrPlayURL:
			driver.get(getattr(Config, str(target)))
			driver.implicitly_wait(10)
			Status=PageRefresh(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			if Status=="PASS":
				return "PASS", ""
			else:
				return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ OpenWebApp"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def Type(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		Text=element.get_attribute("value")
		if Text!="":
			element.clear()
		element.send_keys(str(data))
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Type"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def AttachFile(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		if browser=="FF" or browser=="Chrome":
			data="/Users/macmini/Cureatr/FileUpload/"+str(data)
		else:
			data="/Users/macmini/Cureatr/FileUpload/"+str(data)
		if browser=="FF":
			element=driver.find_element_by_xpath(getattr(Config, str(target)))
			driver.execute_script("document.querySelector('[id^=fileuploadview]').parentNode.parentNode.className=''")
			driver.find_element_by_xpath(getattr(Config, str(target))).send_keys(data)
			driver.execute_script("document.querySelector('[id^=fileuploadview]').parentNode.parentNode.className='upload-manager'")
		else:
			driver.find_element_by_xpath(getattr(Config, str(target))).send_keys(data)
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ AttachFile"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def TypeGroupName(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		Text=element.get_attribute("value")
		if Text!="":
			element.clear()
		data="Group Test "+str(BackEndDrivers.random_digits(10))
		element.send_keys(str(data))
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Type"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def verifysearch(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		BEUserList=[]
		AppUserList=[]
		TotalList=BackEndDrivers.qa_search3(str(data), currentTestDataSheet, dataset)
		UsersList=TotalList[0]
		Status="PASS"
		for UsersLength in range(0, len(UsersList)):
			SingleUser=UsersList[UsersLength]
			UserFirstLastName=str(SingleUser.first_name).lower()+" "+str(SingleUser.last_name).lower()
			BEUserList.append(UserFirstLastName)
			if str(data).lower() in str(SingleUser.first_name).lower() or str(data).lower() in str(SingleUser.last_name).lower():
				Status="PASS"
			else:
				Status="FAIL"
				break
		GroupsList=TotalList[1]
		for GroupLength in range(0, len(GroupsList)):
			SingleGroup=GroupsList[GroupLength]
			BEUserList.append(str(SingleGroup['name']).lower())
			if str(data).lower() in str(SingleGroup['name']).lower():
				Status="PASS"
			else:
				Status="FAIL"
				break

		BESearchLength=len(UsersList)+len(GroupsList)
		
		element=driver.find_element_by_xpath(getattr(Config, target)[4])
		Text=element.get_attribute("value")
		if Text!="":
			element.clear()
		element.send_keys(str(data))
		time.sleep(5)
		List=driver.find_elements_by_xpath(getattr(Config, target)[0])
				
		if BESearchLength==0 and len(List)==2 and str(TCID)=="ContactsSearch":
			ListLength=len(List)-2
			FeSearchStatus="PASS"	
		elif str(TCID)=="ContactsSearch":
			ListLength=len(List)-1
			for ListCount in range(1, len(List)+getattr(Config, target)[5]):
				name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
				title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
				if str(data).lower() in str(name.encode('ascii', 'ignore').decode('ascii')).lower() or str(data).lower() in str(title.encode('ascii', 'ignore').decode('ascii')).lower():
					FeSearchStatus="PASS"
					if " (" in name:
						AppUserList.append(str(name.split(" (")[0:][0]).lower())
					else:
						AppUserList.append(str(name).lower())
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
		else:
			try:
				ListLength=len(List)
				for ListCount in range(1, len(List)+getattr(Config, target)[5]):
					name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
					title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
					if str(data).lower() in str(name.encode('ascii', 'ignore').decode('ascii')).lower() or str(data).lower() in str(title.encode('ascii', 'ignore').decode('ascii')).lower():
						FeSearchStatus="PASS"
						if " (" in name:
							AppUserList.append(str(name.split(" (")[0:][0]).lower())
						else:
							AppUserList.append(str(name).lower())
					else:
						ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
						return "FAIL", ""
				if len(List)==0 and BESearchLength==0:
					element1=driver.find_element_by_xpath(getattr(Config, target)[6]).text
					if element1=="No contacts found" or element1=="No patients found" or element1=="No results found" or element1=="No results are available. Please check your search.":
						FeSearchStatus="PASS"
					else:
						ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
						return "FAIL", ""
			except Exception as err:
				ListLength=len(List)-1
				element1=driver.find_element_by_xpath(getattr(Config, target)[6]).text
				if element1=="No contacts found" or element1=="No patients found" or element1=="No results found" or element1=="No results are available. Please check your search.":
					FeSearchStatus="PASS"
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
		CompareAPPBERestults=cmp(BEUserList.sort(),AppUserList.sort())
		if BESearchLength==ListLength and Status=="PASS" and FeSearchStatus=="PASS" and CompareAPPBERestults==0:
			return "PASS", ""
		else:
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ Verify Search"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def verifyToFieldsearch(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:

		TotalList=BackEndDrivers.qa_search3(str(data), currentTestDataSheet, dataset)
		UsersList=TotalList[0]
		for UsersLength in range(0, len(UsersList)):
			SingleUser=UsersList[UsersLength]
			if str(data).lower() in str(SingleUser.first_name).lower() or str(data).lower() in str(SingleUser.last_name).lower():
				Status="PASS"
			else:
				Status="FAIL"

		GroupsList=TotalList[1]
		for GroupLength in range(0, len(GroupsList)):
			SingleGroup=GroupsList[GroupLength]
			if str(data).lower() in str(SingleGroup['name']).lower():
				Status="PASS"
			else:
				Status="FAIL"

		BESearchLength=len(UsersList)+len(GroupsList)
		element=driver.find_element_by_xpath(getattr(Config, target)[4])
		Text=element.get_attribute("value")
		if Text!="":
			element.clear()
		element.send_keys(str(data))
		time.sleep(5)
		List=driver.find_elements_by_xpath(getattr(Config, target)[0])
		FeSearchStatus=Searchcontacts(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		if BESearchLength==len(List) and Status=="PASS" and FeSearchStatus[0]=="PASS":
			return "PASS", ""
		else:
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ Verify Search"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
def verifyRecentContacts(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		time.sleep(3)
		List = driver.find_elements_by_xpath(getattr(Config, target)[0])
		for ListCount in range(1, len(List)+getattr(Config, target)[5]):
			name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
			title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
			if str(data).lower() in str(name.encode('ascii', 'ignore').decode('ascii')).lower() or str(data).lower() in str(title.encode('ascii', 'ignore').decode('ascii')).lower():
				return "PASS", ""
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", ""
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ Search Contacts Method:: "+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def TypeEMAILID(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
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
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def Maximize(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		driver.maximize_window()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Maximize"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def Click(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, target))))
		element=driver.find_element_by_xpath(getattr(Config, target))
		element.click()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Click"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def NotClick(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, target))))
		element=driver.find_element_by_xpath(getattr(Config, target))
		if(element.click()):
			return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Click"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def DoubleClick(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, target))))
		element=driver.find_element_by_xpath(getattr(Config, target))
		element.click()
		time.sleep(0.300)
		element.click()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Click"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def ClickHidden(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, target))))
		element=driver.find_element_by_xpath(getattr(Config, target))
		driver.execute_script("arguments[0].click();", element)
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Click"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def ClickStale(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_css_selector(getattr(Config, str(target)))
		driver.execute_script("arguments[0].click();", element)
		return "PASS", ""
	except Exception as err:
		try:
			element=driver.find_element_by_css_selector(getattr(Config, str(target)))
			driver.execute_script("arguments[0].click();", element)
			return "PASS", ""
		except Exception as err:
			try:
				element=driver.find_element_by_css_selector(getattr(Config, str(target)))
				driver.execute_script("arguments[0].click();", element)
				return "PASS", ""
			except Exception as err:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL"

def HoverClick(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		add = driver.find_element_by_css_selector('div.fancybox-image')
		SearchButton = driver.find_element_by_css_selector('div.download-button.undisplayed')
		Hover = ActionChains(driver).move_to_element(add).move_to_element(SearchButton)
		Hover.click().build().perform()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Click"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
	
def ClickCss(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		a=driver.find_element_by_css_selector(getattr(Config, str(target)))
		a.click()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Click"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def CloseWebApp(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
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
			Status=PageRefresh(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			a=driver.find_element_by_xpath(getattr(Config, str("ChangeOrg")))
			a.click()
			if Status=="PASS":
				return "PASS", ""
			else:
				return "FAIL", ""
		except:
			logger.info("Exception @ CloseWebApp"+str(err))
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""

def CloseBrowser(driver):
	try:
		driver.close()
		driver.quit()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ CloseBrowser"+str(err))
		return "FAIL", ""
		
def verifyAppTitle(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		if data== driver.title:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyAppTitle"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		ScreenShotDirPath=subdirectory+"ScreenShots/"
		if not os.path.exists(ScreenShotDirPath):
			os.makedirs(ScreenShotDirPath)
		driver.get_screenshot_as_file(ScreenShotDirPath+TCID+"-"+TSID+"-"+DSID+'.jpg')
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ ScreenShot, "+str(err))
		return "Fail", ""

def isElementVisible(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		ui.WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str(target)))))
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ isElementVisible"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "Fail", ""

def PageRefresh(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	for i in range(3): 
		try:
			ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str("WelcomeMsg")))))
			return "PASS"
		except TimeoutException:
			driver.refresh()
			if i>3:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL"
			else:
				continue

def RefreshBrowser(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		driver.refresh()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ RefreshBrowser"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "Fail", ""

def navigateBack(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		driver.back()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ navigateBack"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "Fail", ""
	
def LinkState(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		ClassValue=element.get_attribute("class")
		if str(data)=="enabled":
			if "disabled" in ClassValue:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", ""
			else:
				return "PASS", ""
		else:
			if "disabled" in ClassValue:
				return "PASS", ""
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ LinkState"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def verifyText(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=""
		ui.WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, target))))
		element = driver.find_element_by_xpath(getattr(Config, str(target))).text
		element = element.encode('ascii', 'ignore').decode('ascii')
		if str(element)==str(data):
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyText"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def verifyUserStatus(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		Text=element.get_attribute("class")
		if str(Text)==str(data):
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ Type"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def verifyTextcss(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element = driver.find_element_by_css_selector(getattr(Config, str(target))).text
		if str(data) in element.encode('ascii', 'ignore').decode('ascii'):
			return "PASS", ""
		else:
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyTextcss"+str(err))
		return "FAIL", ""

def verifyErrorMsg(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		if data!="":
			ui.WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str(target)))))
			element = driver.find_element_by_xpath(getattr(Config, str(target))).text
			if data in str(element):
				return "PASS", ""
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ verifyErrorMsg"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def verifyTextContains(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element = driver.find_element_by_xpath(getattr(Config, str(target))).text
		if str(data).lower() in str(element).lower():
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyTextContains"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def verifyOrgText(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element = driver.find_element_by_xpath(getattr(Config, str(target))).text
		StaticText="Sign in for "
		if element==StaticText+data:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyOrgText"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def verifyReadStatus(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		List=driver.find_elements_by_xpath(getattr(Config, target)[0])
		n=len(List)
 		for i in range(21):
			element = driver.find_element_by_xpath(getattr(Config, target)[1]+str(n)+getattr(Config, target)[2]).text
			#StartTime=datetime.datetime.now()
			#presenttime=StartTime.strftime('%l:%M %p')
			if element[:4]==data:
				return "PASS", ""
			elif data=="Unread" and element==data:
				return "PASS", ""
			elif i<20 and element[:4]!=data:
				element = driver.find_element_by_xpath(Config.Logo).click()
				element = driver.find_element_by_xpath(Config.ContactsLink).click()
				element = driver.find_element_by_xpath(Config.InboxLink).click()
				element = driver.find_element_by_xpath(Config.ChatThread).click()
				time.sleep(1)
				continue
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyOrgText"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def SearchInstitution(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
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
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ SearchInstitution"+str(err))
		return "FAIL", ""
		
def selectInstitution(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
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
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ selectInstitution"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def selectQuickMsg(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		List=driver.find_elements_by_xpath(getattr(Config, target)[0])
		for ListCount in range(1, len(List)+1):
			Status=""
			ActOrg=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
			if str(ActOrg)==data:
				driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).click()
				Status="PASS"
				return "PASS", ""
		if Status=="":
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ selectInstitution"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset)
		return "FAIL", ""

def DeleteAllQuickMsgs(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		List=driver.find_elements_by_xpath(getattr(Config, target)[0])
		ListCount=len(List)
		while ListCount>0:
			Status=""
			ActOrg=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
			if str(ActOrg)=="Delete":
				time.sleep(2)
				driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).click()
				driver.find_element_by_xpath(getattr(Config, target)[3]).click()
				time.sleep(2)
				Status=verifyQuickMsgList(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				ListCount=ListCount-1
		if Status[0]=="PASS":
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ DeleteAllQuickMsgs"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def ClearText(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		element.clear()
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ ClearText"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def verifyTextBoxValue(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		TextBoxValue=element.get_attribute("value")
		if str(data) in str(TextBoxValue):
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyTextBoxValue"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def isEncrypted(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		FieldType=element.get_attribute("type")
		if FieldType=="password" and data=="TRUE":
			return "PASS", ""
		elif FieldType=="text" and data=="FALSE":
			return "PASS", ""
		elif FieldType=="textarea" and data=="FALSE":
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ isEncrypted"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def isTextBoxWrapped(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		FieldType=element.get_attribute("type")
		GetTagName=element.tag_name
		if (FieldType=="password" or FieldType=="text" or FieldType=="textarea") and (GetTagName=="input" or GetTagName=="textarea"):
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ isTextBoxWrapped"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def verifyWaterMarkVailability(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		FieldType=element.get_attribute("placeholder")
		GetFieldValue=element.get_attribute("value")
		if data==FieldType+GetFieldValue:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyWaterMarkVailability"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def verifyWaterMarkUnVailability(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		FieldType=element.get_attribute("placeholder")
		GetFieldValue=element.get_attribute("value")
		if data==FieldType+GetFieldValue:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ verifyWaterMarkUnVailability"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def verifySignIn(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		if Correct_Data=="Y":
			element1 = driver.find_element_by_xpath(getattr(Config, "InboxLink")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "ContactsLink")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "YES"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", "NO"
		else:
			element1 = driver.find_element_by_xpath(getattr(Config, "WelcomeMsg")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "GetSupportLink")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "NO"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", "NO"
	except Exception as err:
		logger.info("Exception @ verifySignIn"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", "NO"

def verifySignOut(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element1 = driver.find_element_by_xpath(getattr(Config, "WelcomeMsg")).is_displayed()
		element2 = driver.find_element_by_xpath(getattr(Config, "GetSupportLink")).is_displayed()
		if element1==True and element2==True:
			return "PASS", "YES"
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", "NO"
	except Exception as err:
		logger.info("Exception @ verifySignOut"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", "NO"
		
def verifyFirstTimeSignIn(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		if Correct_Data=="Y":
			element1 = driver.find_element_by_xpath(getattr(Config, "NewPasswordLabel")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "ReTypePasswordLabel")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "YES"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", "NO"
		else:
			time.sleep(5)
			element1 = driver.find_element_by_xpath(getattr(Config, "WelcomeMsg")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "GetSupportLink")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "NO"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", "NO"
	except Exception as err:
		logger.info("Exception @ verifyFirstTimeSignIn"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", "NO"
	
def verifyChangePassword(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		if data=="Y":
			element1 = driver.find_element_by_xpath(getattr(Config, "TSSignOut")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "TSAccept")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "YES"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", "NO"
		else:
			time.sleep(5)
			element1 = driver.find_element_by_xpath(getattr(Config, "NewPasswordLabel")).is_displayed()
			element2 = driver.find_element_by_xpath(getattr(Config, "ReTypePasswordLabel")).is_displayed()
			if element1==True and element2==True:
				return "PASS", "NO"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", "NO"
	except Exception as err:
		logger.info("Exception @ verifyChangePassword"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", "NO"

def wait(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		time.sleep(data)
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ wait"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def DriverWait(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		WebDriverWait(driver, 10).until(wait_for_text_to_start_with(By.find_element_by_xpath, getattr(Config, str(target)), data))
		return "PASS", ""
	except Exception as err:
		logger.info("Exception @ DriverWait"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def ImageComparision(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element = driver.find_element_by_xpath(getattr(Config, target))
		BasePath=element.get_attribute("src")
		print "BasePath=",BasePath
		driver.get(BasePath)
		driver.get_screenshot_as_file(ActFile)
		
		i1 = Image.open(ActFile)
		i2 = Image.open(getattr(Constants, data))
		#assert i1.mode == i2.mode, "Different kinds of images."
		#assert i1.size == i2.size, "Different sizes."

		pairs = izip(i1.getdata(), i2.getdata())
		if len(i1.getbands()) == 1:
			# for gray-scale jpegs
			dif = sum(abs(p1-p2) for p1,p2 in pairs)
		else:
			dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

		ncomponents = i1.size[0] * i1.size[1] * 3
		if (dif / 255.0 * 100)/ncomponents==0.0:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		print err
		logger.info("Exception @ ImageComparision"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def PdfComparision(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		oldfile=[]
		newfile=[]
		for line in get_pdf_content_lines(ExpPdfFile):
			oldfile.append(str(line))
			
		for line in get_pdf_content_lines(ActPdfFile):
			newfile.append(str(line.encode('ascii', 'ignore').decode('ascii')))
			
		print len(set(oldfile) - set(newfile))
		return "PASS", ""
	except Exception as err:
		print err
		logger.info("Exception @ PdfComparision"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def get_pdf_content_lines(pdf_file_path):
	
	with open(pdf_file_path) as f:
		pdf_reader = PdfFileReader(f)
		for page in pdf_reader.pages:
			for line in page.extractText().splitlines():
				yield line

def ExcelComparision(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	wb = openpyxl.load_workbook('/home/cureatr/CureatrPythonWorkSpace/Images/Suite_Web.xlsx')
	wb1 = openpyxl.load_workbook('/home/cureatr/CureatrPythonWorkSpace/Images/Suite_Web.xlsx')
	sheet1 = wb.get_sheet_by_name('Suite')
	sheet2 = wb1.get_sheet_by_name('Suite')
	if sheet1.max_row ==sheet2.max_row:
		if  sheet1.max_column==sheet2.max_column:
			for i in range(1, sheet1.max_column):
				for j in range(1,sheet1.max_row):
					if sheet1.cell(row = j, column = i).value != sheet2.cell(row = j, column = i).value:
						print sheet1.cell(row = j, column = i).value, sheet2.cell(row = j, column = i).value
					else:
						print "file are same"
	return "PASS", ""

def VoiceComparision(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		audiodiff.equal('airplane.flac', 'airplane.m4a')
		audiodiff.audio_equal('airplane.flac', 'airplane.m4a')
		audiodiff.tags_equal('airplane.flac', 'airplane.m4a')
	except Exception as err:
		print err
		logger.info("Exception @ ImageComparision"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
def VerifyProfileImage(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element = driver.find_element_by_xpath(getattr(Config, target))
		BasePath=element.value_of_css_property("background-image")
		ImageUrl=BasePath.split("\"")[1:][0]
		if ImageUrl=="/static/images/user.png" or "https://play-profileimages-cureatr.s3.amazonaws.com/" in ImageUrl:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ ImageComparision"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def verifyTermsofService(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
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

def Searchcontacts(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		time.sleep(5)
		List = driver.find_elements_by_xpath(getattr(Config, target)[0])
		Status=""
		for ListCount in range(1, len(List)+getattr(Config, target)[5]):
			name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
			title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
			if str(data).lower() in str(name.encode('ascii', 'ignore').decode('ascii')).lower() or str(data).lower() in str(title.encode('ascii', 'ignore').decode('ascii')).lower():
				Status="PASS"
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
				return "FAIL", ""
		
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		logger.info("Exception @ Search Contacts Method:: "+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def selectContact(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		time.sleep(5)
		ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, target)[0])))
		List = driver.find_elements_by_xpath(getattr(Config, target)[0])
		for ListCount in range(1, len(List)+getattr(Config, target)[5]):
			Status=""
			name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
			title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
			if str(data).lower() in name.lower() or str(data).lower() in title.lower():
				element=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2])
				driver.execute_script("arguments[0].click();", element)
				Status="PASS"
				return "PASS", ""
		
		if Status=="":
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ selectInstitution"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def isVissible(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		if element.is_displayed():
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", "" 
	except Exception as err:
		logger.info("Exception @ isVissible"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""  

def isUploadSucessVissible(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		List=driver.find_elements_by_xpath(getattr(Config, target)[0])
		ui.WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, target)[1]+str(len(List))+getattr(Config, target)[2])))
		element=driver.find_element_by_xpath(getattr(Config, target)[1]+str(len(List))+getattr(Config, target)[2])
		if element.is_displayed():
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", "" 
	except Exception as err:
		logger.info("Exception @ isUploadCancelBtnVissible"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", "" 		

def isNotVissible(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		if element.is_displayed():
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", "" 
		else:
			return "PASS", ""
	except Exception as err:
		if "no such element: Unable to locate element:" in str(err):
			return "PASS", ""
		else:
			logger.info("Exception @ isVissible"+str(err))
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""  

def isEnabled(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		if element.is_enabled():
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", "" 
	except Exception as err:
		logger.info("Exception @ isVissible"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""  
  
def delLastchars(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
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
						ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
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
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
					
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def AddCharByChar(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
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
						ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
						return "FAIL", ""
			except Exception as err:
				element1=driver.find_element_by_xpath(getattr(Config, target)[6]).text
				if element1=="No contacts found" or element1=="No patients found" or element1=="No results found":
					continue
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL",""
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def delLastcharsManageGroup(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
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
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
			time.sleep(1)
			for ListCount in range(1, len(List)+getattr(Config, target)[5]):
				name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
				title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
				if GetFieldValue.lower()  in name.lower()  or GetFieldValue.lower()  in title.lower():
					Status="PASS"
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
			element.send_keys(Keys.BACKSPACE)
			GetFieldValue=element.get_attribute("value")
					
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def AddCharByCharManageGroup(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
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
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
			for ListCount in range(1, len(List)+getattr(Config, target)[5]):
				name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
				title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
				if str(Char).lower()  in name.lower()  or str(Char).lower()  in title.lower():
					Status="PASS"
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def delLastcharsCoverageSearch(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
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
							ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
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
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
					
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""
		
def AddCharByCharCoverageSearch(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		for Count, Char in enumerate(data):
			try:
				element=driver.find_element_by_xpath(getattr(Config, target)[4])
				element.send_keys(str(Char))
				time.sleep(2)
				List = driver.find_elements_by_xpath(getattr(Config, target)[0])
				for ListCount in range(1, len(List)+getattr(Config, target)[5]):
					name=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[2]).text
					title=driver.find_element_by_xpath(getattr(Config, target)[1]+str(ListCount)+getattr(Config, target)[3]).text
					if str(Char).lower()  in name.lower()  or str(Char).lower()  in title.lower():
						Status="PASS"
					else:
						ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
						return "FAIL", ""
			except Exception as err:
				element1=driver.find_element_by_xpath(getattr(Config, target)[6]).text
				time.sleep(5)
				if element1=="No results are available. Please check your search.":
					continue
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL",""
		if Status=="PASS":
			return "PASS", ""
	except Exception as err:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def MaximizeComposeScreen(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		ui.WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, target))))
		time.sleep(1)
		element = driver.find_element_by_xpath(getattr(Config, str(target))).size
		if str(element)=="{'width': 482, 'height': 283}" and str(data)=="Maximize":
			return "PASS", ""
		elif str(element)=="{'width': 270, 'height': 41}" and str(data)=="Minimize":
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyText"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def verifyQuickMsgList(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
	try:
		List = driver.find_elements_by_xpath("//div/div[1]/div/div[2]/ul[2]/li")
		n=len(List)
		num=4
		Status=""
		while n > 0:
			text=driver.find_element_by_xpath("//div/div[1]/div/div[2]/ul[2]/li["+str(n)+"]/div[2]/div[2]").text
			deletestate=driver.find_element_by_xpath("//div/div[1]/div/div[2]/ul[2]/li["+str(n)+"]/div[2]/a").text
			number=driver.find_element_by_xpath("//div/div[1]/div/div[2]/ul[2]/li["+str(n)+"]/div[1]/div").text
			icon=driver.find_element_by_xpath("//div/div[1]/div/div[2]/ul[2]/li["+str(n)+"]/div[2]/div[1]").is_displayed()
			if len(List)>6 and num<10:
				if str(num)==str(number) and icon==True and text is not None and str(deletestate)=="Delete":
					Status="PASS"
					num=num+1
					n=n-1
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
			elif len(List)<7:
				if str(num)==str(number) and icon==True and text is not None and str(deletestate)=="Delete":
					Status="PASS"
					num=num+1
					n=n-1
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
			else:
				if str(number)=="" and icon==True and text is not None and str(deletestate)=="Delete":
					Status="PASS"
					n=n-1
				else:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
					return "FAIL", ""
		if Status=="PASS" and len(List)>0:
			return "PASS", ""
		elif Status=="" and len(List)==0:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
			return "FAIL", ""
	except Exception as err:
		logger.info("Exception @ verifyText"+str(err))
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
		return "FAIL", ""

def verifyLatestMessage(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
 	try:
 		time.sleep(3)
 		i=1
 		while i < 30:
 			List=driver.find_elements_by_xpath(getattr(Config, target)[0])
 			n=len(List)
 			element=driver.find_element_by_xpath(getattr(Config, target)[1]+str(n)+getattr(Config, target)[2]).text
 			if str(element)==str(data):
 				return "PASS", ""
 			else:
 				time.sleep(1)
 				i=i+1
 				Status="FAIL"
 		if Status=="FAIL":
 			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
 			return "FAIL", ""
 	except Exception as err:
 		logger.info("Exception @ selectInstitution"+str(err))
 		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
 		return "FAIL", ""

def verifyLatestImage(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
 	try:
 		time.sleep(3)
 		timesec=1
 		while timesec < 60:
 			List=driver.find_elements_by_xpath(getattr(Config, target)[0])
 			element=driver.find_element_by_xpath(getattr(Config, target)[1]+str(len(List))+getattr(Config, target)[2]).text
 			if element==data:
 				Status="PASS"
 				break
 			else:
 				Status="FAIL"
 				time.sleep(1)
 				timesec=timesec+1

 		element=driver.find_element_by_xpath(getattr(Config, target)[1]+str(len(List))+getattr(Config, target)[3]).is_displayed()
 		if element==True and Status=="PASS":
 			return "PASS", ""
 		else:
 			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
 			return "FAIL", ""
 	except Exception as err:
 		logger.info("Exception @ selectInstitution"+str(err))
 		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
 		return "FAIL", ""

def SelectLatestImage(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user):
 	try:
 		List=driver.find_elements_by_xpath(getattr(Config, target)[0])
 		print "List=",List
 		print getattr(Config, target)[1]+str(len(List))+getattr(Config, target)[3]
 		element=driver.find_element_by_xpath(getattr(Config, target)[1]+str(len(List))+getattr(Config, target)[3]).is_displayed()
 		print element
 		if element==True:
 			driver.find_element_by_xpath(getattr(Config, target)[1]+str(len(List))+getattr(Config, target)[3]).click()
 			return "PASS", ""
 		else:
 			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
 			return "FAIL", ""
 	except Exception as err:
 		logger.info("Exception @ selectInstitution"+str(err))
 		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data, currentTestDataSheet, dataset, user)
 		return "FAIL", ""