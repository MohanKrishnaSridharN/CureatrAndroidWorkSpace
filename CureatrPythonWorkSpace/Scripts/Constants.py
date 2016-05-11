import os,sys
import platform
import webbrowser
import xlwt
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time


def executefunctions(browser, driver):
    driver=openbrowser(browser, driver)
    openapp(driver)
    close(driver)


def openbrowser(browser, driver):
    if browser=="FF":
        driver = webdriver.Firefox()
        print "Firefox opened"
    elif browser=="Chrome":
        driver = webdriver.Chrome()
        print "Chrome opened"
    elif browser=="IE":
        driver = webdriver.Chrome()
        print "Chrome opened"
    return driver


def openapp(driver):
    driver.get("https://messenger.play.cureatr.com")

def close(driver):
    driver.close()
    driver.quit()

# open a public URL, in this case, the webbrowser docs
threads=[]

def mainp():
    try:
       t1=Thread(target=executefunctions,args=('FF', ''))
       t2=Thread(target=executefunctions,args=('Chrome', ''))
       threads.append(t1)
       threads.append(t2)
       t1.start()
       t2.start()
    except:
       print "Error: unable to start thread"


mainp()
