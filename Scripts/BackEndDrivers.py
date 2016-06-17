import sys, os
import XlsxReader
from XlsxReader import *
import time
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..', 'dev', 'cureatr','server','qa')))
import db_recipes
from cureatr.model.users import Users, UID, User

from cureatr.lib.search import (
    user_search, email_search, recent_search,
    coverage_search, combined_search, group_search, role_search
)
from random import randint
SEARCH_TYPE_RECENT = "recent"
SEARCH_TYPE_CUREATR_ONLY = "cureatr"
SEARCH_TYPE_EMAIL = "email"
SEARCH_TYPE_COVERAGE = "coverage"
OTP=()

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
				#LASTNAME=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][5])
				USERNAME=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][6])
				PASSWORD=getCellValueBySheet(currentTestDataSheet, dataset, data.split("$")[1:][7])
				rn=random_digits(10)
				LASTNAME=str(rn)
				#EMAILID=browser.lower()+"-test002@mtuity.com"
				EMAILID="mohan.nimmala+"+str(rn)+browser+"@mtuity.com"#Testsn25
				print EMAILID
				if str(target)=="USER-B":
					addCellValue(currentTestSuiteXLSPATH,currentTestCase, dataset, "USERB", EMAILID)
					addCellValueToBuff(currentTestDataSheet, dataset, "USERB", EMAILID)
				else:
					addCellValue(currentTestSuiteXLSPATH,currentTestCase, dataset, "EMAILID", EMAILID)
					addCellValueToBuff(currentTestDataSheet, dataset, "EMAILID", EMAILID)
				
				OTP=db_recipes.qa_create_user(first_name=FIRSTNAME, institution_id=INSTITUTIONID, specialty=SPECIALTY, 
					title=TITILE, password=None, last_name=LASTNAME, email=EMAILID,make_active=True,admin_iids=[INSTITUTIONID])
				
				if str(target)=="USER-B":
					addCellValue(currentTestSuiteXLSPATH,currentTestCase, dataset, "PASSWORDB", OTP[1])
					addCellValueToBuff(currentTestDataSheet, dataset, "PASSWORDB", OTP[1])
				else:
					addCellValue(currentTestSuiteXLSPATH,currentTestCase, dataset, "PASSWORD", OTP[1])
					addCellValueToBuff(currentTestDataSheet, dataset, "PASSWORD", OTP[1])

				addCellValue(currentTestSuiteXLSPATH,currentTestCase, dataset, "LASTNAME", str(rn))
				addCellValueToBuff(currentTestDataSheet, dataset, "LASTNAME", str(rn))
				return "PASS", ""
				
	except Exception as err:
		print err
		if EMAILID in str(err):
			print "UserId already existed"
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
				db_recipes.qa_create_institution(INSTITUTIONID, short_name=INSTITUTIONSHORTNAME, name=INSTITUTIONNAME,allowed_domains=['mtuity.com'])
				return "PASS", ""
	except Exception as err:
		if "id ["+str(INSTITUTIONID)+"] exists" in str(err):
			print "INSTITUTIONID Exists"
			return "INSTITUTIONID Exists", ""
		else:
			print "INSTITUTION Ceration Failed & Stopped Automation Test Execution"
			return "FAIL", ""

def qa_search3(data, currentTestDataSheet, dataset):
	#user=OTP[0]
	EMAILID=getCellValueBySheet(currentTestDataSheet, dataset, "EMAILID")
	user=Users.find_by_email(EMAILID)[0]
	search_type=""
	query=data
	include_groups = True
	include_inactive=True
	include_roles=True
	profiles_directory = ()
	results_directory = ()
	results_cureatr = ()
	roles = []
	limited_results = False
	if search_type == SEARCH_TYPE_EMAIL:
		# used in the prototype of "message by email" button in messenger
		# FIXFIX: consider privacy implications? who can search for who? open right now
		results_cureatr = email_search(query)
	elif search_type == SEARCH_TYPE_RECENT:
		results_cureatr, roles = recent_search(user, include_inactive=include_inactive, include_roles=include_roles)
	elif search_type == SEARCH_TYPE_CUREATR_ONLY:
		results_cureatr, limited_results = user_search(user, query, include_inactive=include_inactive)
	elif search_type == SEARCH_TYPE_COVERAGE:
		results_cureatr, limited_results = coverage_search(user, query, include_inactive=include_inactive)
	else:
		results_directory, profiles_directory, results_cureatr, limited_results = combined_search(user, query, include_inactive=include_inactive)

	# FIXFIX: roll group search into combined search / user search?
	groups = []
	if include_groups and search_type not in (SEARCH_TYPE_EMAIL, SEARCH_TYPE_RECENT):
		groups, groups_limited = group_search(user, query)
		limited_results = limited_results or groups_limited
	if include_roles and search_type not in (SEARCH_TYPE_EMAIL, SEARCH_TYPE_COVERAGE, SEARCH_TYPE_RECENT):
		roles, roles_limited = role_search(user, query, include_inactive=include_inactive)
		limited_results = limited_results or roles_limited

	raw_results= {
	'results_directory': results_directory,  # directory + schedule results
	'profiles_directory': profiles_directory,  # cureatr users that link to the directory results
	'results_cureatr': results_cureatr,  # other cureatr users that match the query
	'limited_results': limited_results,  # if True, some results may be limited
	'recipient_groups': groups,
	'roles': roles,
	}
	Total_Results=[raw_results['results_cureatr'], raw_results['recipient_groups']]
	return Total_Results
