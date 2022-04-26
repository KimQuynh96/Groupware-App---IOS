from math import fabs
from time import time
from kq_setup import driver
from kq_lib_common import By , data, time,cm

def contact():
    ac_menu = fo = na = True 
    ct_name = "User" +  cm.to_day
    
    driver.find_element_by_xpath(data["contact"]["menu"]).click()
    if cm.is_displayed(data["contact"]["more"]) == True : 
        cm.msg("p",data["msg_contact"]["pass_access"])
    else :
        ac_menu = False
        cm.msg("f",data["msg_contact"]["fail_access"])

    if ac_menu == True :

        driver.find_element_by_xpath(data["contact"]["left"]).click()
        if  cm.is_displayed(data["contact"]["my"]) == True : 
            
            # Click on My Contacts Folder 
            driver.find_element_by_xpath(data["contact"]["my"]).click()
            if cm.is_displayed(data["contact"]["wri"]) == True : 
                cm.msg("p",data["msg_contact"]["pass_my"])

                # Click on add contact icon 
                driver.find_element_by_xpath(data["contact"]["wri"]).click()
                if cm.is_displayed(data["contact"]["bt_save"]) == True : 
                    cm.msg("p",data["msg_contact"]["pass_write"])

                    # Choose folder
                    driver.find_element_by_xpath(data["contact"]["folder"]).click()
                    folder = driver.find_element_by_xpath(data["contact"]["folder_na"]).text 
                    if folder == "My Folder" :
                        cm.msg("p",data["msg_contact"]["pass_folder"])
                    else :
                        fo = False
                        cm.msg("p",data["msg_contact"]["fail_folder"])
                    
                    # Enter contact name
                    name = driver.find_element_by_xpath(data["contact"]["name"])
                    name.send_keys(ct_name)
                    if name.text == ct_name :
                        cm.msg("p",data["msg_contact"]["pass_name"])
                    else :
                        na = False
                        cm.msg("f",data["msg_contact"]["fail_name"])

                    if fo == True and na == True    :
                        driver.find_element_by_xpath(data["contact"]["bt_save"]).click()
                        if cm.is_displayed(data["contact"]["bt_modi"]) == True : 
                            cm.msg("p",data["msg_contact"]["pass_save"])
                        else :
                            cm.msg("p",data["msg_contact"]["fail_save"])
            else :
                cm.msg("f",data["msg_contact"]["fail_my"])
        else :
            cm.msg("f",data["msg_contact"]["fail_left"])

        
            
        
            
    
    
    
    

