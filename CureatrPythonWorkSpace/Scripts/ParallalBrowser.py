from threading import Thread
import DriverScript

def executefunctions(browser, driver):

# open a public URL, in this case, the webbrowser docs

    threads=[]

def mainp():
    try:
        t1=Thread(target=executefunctions,args=('FF', ''))
        t2=Thread(target=executefunctions,args=('Chrome', ''))
        t3=Thread(target=executefunctions,args=('IE', ''))
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        t1.start()
        t2.start()
        t3.start()
    except:
        print "Error: unable to start thread"
