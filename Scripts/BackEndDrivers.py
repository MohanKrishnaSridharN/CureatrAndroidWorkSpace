import sys, os
import XlsxReader
from XlsxReader import *
import time
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..', 'dev', 'cureatr', 'server', 'qa')))
import db_recipes
from random import randint
#test comment

def random_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def CreateUserPY(browser, target, data, currentTestDataSheet,  dataset,currentTestSuiteXLSPATH,currentTestCase):
    
	try:
		if data is not None:
			if str(data).startswith("PY"):
				INSTITUTIONID=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][0])
				TYPE=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][1])
				TITILE=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][2])
				SPECIALTY=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][3])
				FIRSTNAME=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][4])
				LASTNAME=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][5])
				USERNAME=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][6])
				PASSWORD=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][7])
				rn=random_digits(10)
				EMAILID=browser.lower()+"-test"+str(rn)+"@mtuity.com"
				addCellValue(currentTestSuiteXLSPATH,currentTestCase, dataset, "EMAILID", EMAILID)
				addCellValue1(currentTestDataSheet, dataset, "EMAILID", EMAILID)
				db_recipes.qa_create_user(first_name=FIRSTNAME, institution_id=INSTITUTIONID, specialty=SPECIALTY, 
					title=TITILE, password=PASSWORD, last_name=LASTNAME, email=EMAILID)
				return "PASS", ""
				
	except Exception as err:
		if EMAILID in str(err):
			return "UserId already existed", ""
		else:
			print "User Ceration Failed & Stopped Automation Test Execution"
			return "FAIL", ""

def CreateInstitution(browser, target, data, currentTestDataSheet,  dataset,currentTestSuiteXLSPATH,currentTestCase):
	try:
		if data is not None:
			if str(data).startswith("PY"):
				INSTITUTIONID=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][0])
				INSTITUTIONSHORTNAME=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][1])
				INSTITUTIONNAME=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][2])
				db_recipes.qa_create_institution(INSTITUTIONID, short_name=INSTITUTIONSHORTNAME, name=INSTITUTIONNAME)
				return "PASS", ""
	except Exception as err:
		if "id ["+INSTITUTIONID+"] exists" in str(err):
			return "INSTITUTIONID Exists", ""
		else:
			print "INSTITUTION Ceration Failed & Stopped Automation Test Execution"
			return "FAIL", ""
