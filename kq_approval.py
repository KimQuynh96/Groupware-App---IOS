from math import fabs
from time import time
from kq_setup import driver
from kq_lib_common import By , data, time,cm

def approval():
    ac_menu = True
    if cm.is_displayed(data["approval"]["bt_write"]) == True : 
        cm.msg("p",data["msg_approval"]["pass_access"])
    else :
        ac_menu = False
        cm.msg("f",data["msg_approval"]["fail_access"])
    if ac_menu == True :
        driver.find_element_by_xpath(data["approval"]["bt_write"]).click()
        
        # Choose recipient
        driver.find_element_by_xpath(data["approval"]["org"]).click()
        if cm.is_displayed(data["approval"]["search"]) == True :  
            cm.msg("p",data["msg_approval"]["pass_ic_org"])

            # Click on search icon 
            driver.find_element_by_xpath(data["task"]["search"]).click()
            if cm.is_displayed(data["task"]["bt_search"]) == True :  
                cm.msg("p",data["msg_approval"]["pass_ic_search"])
                recipient = cm.add_recipient()
            else :
                cm.msg("f",data["msg_approval"]["fail_ic_search"])


        else :
            cm.msg("f",data["msg_approval"]["fail_ic_org"])
        # Choose form
        driver.find_element_by_xpath(data["approval"]["se_form"]).click()
        driver.find_element_by_xpath(data["approval"]["form"]).click()
        if recipient == True :
            driver.find_element_by_xpath(data["approval"]["send"]).click()
            driver.find_element_by_xpath(data["approval"]["apply"]).click()

            
    
    
    
    

