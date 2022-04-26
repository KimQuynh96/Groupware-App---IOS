import json,os,time,datetime
from pathlib import Path
from datetime import date
from tkinter.messagebox import NO
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from kq_setup import driver
import tkinter


json_file = os.path.dirname(Path(__file__).absolute()) + "/kq_data.json"
with open(json_file) as json_file :
    data = json.load(json_file)

class cm :

    def to_day():
        return str(datetime.date.today()) + "," + str(datetime.datetime.now().time())[None:str(datetime.datetime.now().time()).rfind(".")]

    def is_displayed(element):
        try :
            time.sleep(10)
            driver.find_element_by_xpath(element)
            return True
        except NoSuchElementException:
            return False
    
    def msg(t,text):
        if t == "p":
            print("\033[32m" + text + "\033[39m")
        elif t == "n" :
            print("\033[33m" + text + "\033[39m")

        elif t == "t" :
            print("\033[37m" + text + "\033[39m")
        else :
            print("\033[31m" + text + "\033[39m")

    def add_recipient():
        recipient = True 
        # Enter user name to saerch 
        input = driver.find_element_by_xpath(data["task"]["ip_search"])
        input.send_keys("TS2")
        driver.find_element_by_xpath(data["task"]["bt_search"]).click()
        driver.find_element_by_xpath(data["task"]["ts1"]).click()
        driver.find_element_by_xpath(data["task"]["ok"]).click()

        # Check recipient added 
        user =  driver.find_element_by_xpath(data["task"]["name"]).text
        if user == "TS2" :
            cm.msg("p",data["msg_task"]["pass_recipients"])

        else :
            recipient = False 
            cm.msg("f",data["msg_task"]["fail_recipients"])

        return recipient

