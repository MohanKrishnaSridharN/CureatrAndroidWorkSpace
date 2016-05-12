from fabric.api import *
from fabric.context_managers import cd
import random
from random import randint

env.use_ssh_config = False
#host='192.168.73.129'
env.hosts = ['192.168.73.129']
env.user = "cureatr"
env.password = "cureatr"
env.port = 22

def CreateUserPY(filepath):
   with shell_env(PYTHONPATH='/home/cureatr/dev/cureatr/server'):
       with cd('/home/cureatr/dev/cureatr/server'):
           run(". /virtualenv/bin/activate")
           put(filepath,'/home/cureatr/dev/cureatr/server')
           run("./tools/admin.py dev user_create < /home/cureatr/createuserChrome.json")


def cureatejsonfile(INSTITUTIONID, TYPE, TITILE, SPECIALTY, FIRSTNAME, LASTNAME, USERNAME, PASSWORD, browser):
	#RanNumber=random.random()
	RanNumber="0001"
	if browser=="IE":
		Filename="createuserIE"
		EmailId="IE"+RanNumber+"@mtuity.com"
	elif browser=="Chrome":
		Filename="createuserChrome"
		EmailId="Chrome"+RanNumber+"@mtuity.com"
	else:
		Filename="createuserFF"
		EmailId="FF"+RanNumber+"@mtuity.com"


	filepath='/Users/macmini/Cureatr/CureatrPythonWorkSpace/User/'+Filename+'.json'
	file = open(filepath,'w')
	a = {"first_name": str(FIRSTNAME), "last_name": str(LASTNAME), "username": str(USERNAME), "password": str(PASSWORD), "email": str(EmailId), "institution": str(INSTITUTIONID), "specialty": str(SPECIALTY), "title": str(TITILE)}
	print a
	file.write(str(a))
	file.close()
	CreateUserPY(filepath)  
           