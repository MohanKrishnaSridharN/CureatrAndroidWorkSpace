import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
import Config
from Config import *
import time
import os
import PIL
from PIL import ImageChops
from PIL import Image

def LaunchWebBrowser(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if browser=="FF":
			driver = webdriver.Firefox()
			#cap=webdriver.DesiredCapabilities.FIREFOX
			#driver=webdriver.Remote('http://192.168.73.1:5557/wd/hub', cap)
			return driver, "PASS"
		elif browser=="Chrome":
			cap=webdriver.DesiredCapabilities.CHROME
			#driver=webdriver.Remote('http://192.168.73.1:5557/wd/hub', cap)
			#driver = webdriver.Chrome()
			#driver = webdriver.Chrome(executable_path="D:/CureatrPythonWorkSpace/chromedriver_win32/chromedriver.exe")
			return driver, "PASS"
		elif browser=="IE":
			cap=webdriver.DesiredCapabilities.INTERNETEXPLORER
			driver=webdriver.Remote('http://192.168.73.125:5557/wd/hub', cap)
			return driver, "PASS"
	except Exception as err:
		print (Exception, err)
		return driver, "FAIL"

def OpenWebApp(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if driver.current_url!="https://messenger.play.cureatr.com/":
			driver.get(getattr(Config, str(target)))
			driver.implicitly_wait(20)
			Status=PageRefresh(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			if Status=="PASS":
				return "PASS", ""
			else:
				return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def Type(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		element.clear()
		element.send_keys(str(data))
		return "PASS", ""
	except Exception as err:
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def Maximize(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		driver.maximize_window()
		return "PASS", ""
	except Exception as err:
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def Click(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		a=driver.find_element_by_xpath(getattr(Config, str(target)))
		a.click()
		return "PASS", ""
	except Exception as err:
		print (Exception, err)
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
		#driver.close()
		#driver.quit()
		return "PASS", ""
	except Exception as err:
		print (Exception, err)
		return "FAIL", ""

def CloseBrowser(driver):
	try:
		driver.close()
		driver.quit()
		return "PASS", ""
	except Exception as err:
		print (Exception, err)
		return "FAIL", ""
		
def verifyAppTitle(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if data== driver.title:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""

def ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		ScreenShotDirPath=subdirectory+"ScreenShots/"
		os.makedirs(ScreenShotDirPath)
		driver.get_screenshot_as_file(ScreenShotDirPath+TCID+"-"+TSID+"-"+DSID+'.jpg')
		return "PASS", ""
	except Exception as err:
		print (Exception, err)
		return "Fail", ""

def isElementVisible(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str(target)))))
		return "PASS", ""
	except TimeoutException:
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "Fail", ""
		
def PageRefresh(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str("WelcomeMsg")))))
		return "PASS"
	except TimeoutException:
		driver.refresh()
		try:
			ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str("WelcomeMsg")))))
			return "PASS"
		except TimeoutException:
			driver.refresh()
			try:
				ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str("WelcomeMsg")))))
				return "PASS"
			except TimeoutException:
				driver.refresh()
				try:
					ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, getattr(Config, str("WelcomeMsg")))))
					return "PASS"
				except TimeoutException:
					ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
					return "FAIL"

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
		print "exception@TypeText" 
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyText(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element = driver.find_element_by_xpath(getattr(Config, str(target))).text
		if element==data:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		print (Exception, err)
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
		print (Exception, err)
		return "FAIL", ""

def verifyErrorMsg(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if data!=None:
			element = driver.find_element_by_xpath(getattr(Config, str(target))).text
			if data in element:
				return "PASS", ""
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyTextContains(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element = driver.find_element_by_xpath(getattr(Config, str(target))).text
		if data in element:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		print (Exception, err)
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
		print (Exception, err)
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
			else:
				ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
				Status="FAIL"
		
		if Status=="PASS":
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		print (Exception, err)
		return "FAIL", ""
		
def selectInstitution(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		List=driver.find_elements_by_xpath("//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li")
		for ListCount in range(1, len(List)+1):
			ActOrg=driver.find_element_by_xpath("//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li["+str(ListCount)+"]/div/div").text
			if str(ActOrg)==data:
				Status="PASS"
				break
			else:
				Status="FAIL"
		
		if Status=="PASS":
			driver.find_element_by_xpath("//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li["+str(ListCount)+"]/div/div").click()
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def ClearText(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		element.clear()
		return "PASS", ""
	except Exception as err:
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def verifyTextBoxValue(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element=driver.find_element_by_xpath(getattr(Config, str(target)))
		TextBoxValue=element.get_attribute("value")
		if data==TextBoxValue:
			return "PASS", ""
		else:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
	except Exception as err:
		print (Exception, err)
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
		print (Exception, err)
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
		print (Exception, err)
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
		print (Exception, err)
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
		print (Exception, err)
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
		print (Exception, err)
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
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", "NO"
		
def verifyFirstTimeSignIn(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if Correct_Data=="Y":
			print "Correct Data Y"
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
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", "NO"
	
def verifyChangePassword(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		if data=="Y":
			print "Correct Data Y"
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
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", "NO"

def wait(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		time.sleep(data)
		return "PASS", ""
	except Exception as err:
		print (Exception, err)
		ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
		return "FAIL", ""
		
def ImageComparision(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data):
	try:
		element = driver.find_element_by_xpath(getattr(Config, target))
		BasePath=element.value_of_css_property("background-image")
		ImageUrl=BasePath.split("\"")[1:][0]
		driver.get(ImageUrl)
		driver.get_screenshot_as_file("/home/cureatr/CureatrPythonWorkSpace/Images/Actlogo.png")
		im1 = Image.open("/home/cureatr/CureatrPythonWorkSpace/Images/Actlogo.png")
		im2 = Image.open("/home/cureatr/CureatrPythonWorkSpace/Images/Actlogo.png")
		if ImageChops.difference(im1, im2).getbbox is None:
			ScreenShot(browser, driver, target, data, subdirectory, TCID, TSID, DSID, Correct_Data)
			return "FAIL", ""
		else:
			return "PASS", ""
	except Exception as err:
		print (Exception, err)
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
		print (Exception, err)
		return "FAIL", ""