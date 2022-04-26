from math import fabs
from time import time
from kq_setup import driver
from kq_lib_common import By , data, time,cm

def mail():
    ac_menu = to_me = tit = send  = True 
    displayed = False
    content = "Content mail"
    subject = "Mail " + cm.to_day
    driver.find_element_by_xpath(data["mail"]["menu"]).click()

    if cm.is_displayed(data["mail"]["bt_write"]) == True : 
        cm.msg("p",data["msg_mail"]["pass_ac_menu"])
    else :
        ac_menu = False
        cm.msg("p",data["msg_mail"]["fail_ac_menu"])

    if ac_menu == True :
        # Click on write button
        driver.find_element_by_xpath(data["mail"]["bt_write"]).click()
        if cm.is_displayed(data["mail"]["bt_send"]) == True : 
            cm.msg("p",data["msg_mail"]["pass_bt_write"])
        else :
            cm.msg("p",data["msg_mail"]["fail_bt_write"]) 

        # Choose recipient 
        driver.find_element_by_xpath(data["mail"]["bt_me"]).click()
        ad_me = driver.find_element_by_xpath(data["mail"]["text"]).text
        if ad_me == data["mail"]["to"]:
            cm.msg("p",data["msg_mail"]["pass_add_reci"]) 
        else :
            to_me = False
            cm.msg("p",data["msg_mail"]["fail_add_reci"]) 
        
        # Enter title mail
        title = driver.find_element_by_xpath(data["mail"]["subject"])
        title.send_keys(subject)
        
        if title.text == subject :
            cm.msg("p",data["msg_mail"]["pass_title"])
        else :
            tit = False
            cm.msg("f",data["msg_mail"]["fail_title"])

        # Enter content mail
        editor = driver.driver.find_element_by_id(data["editor"])
        editor.send_keys(subject)
        
        if editor.text == content :
            cm.msg("p",data["msg_mail"]["pass_content"])
        else :
            tit =False
            cm.msg("f",data["msg_mail"]["fail_content"])

        # Send mail
        if to_me == True and tit == True :
            driver.find_element_by_xpath(data["mail"]["send"]).click()
            if cm.is_displayed(data["mail"]["bt_write"]) == True :  
                cm.msg("p",data["msg_mail"]["pass_send"])
            else :
                send = False
                cm.msg("p",data["msg_mail"]["fail_send"])
            # Check mail list
            if send == True :
                driver.find_element_by_class_name(data["mail"]["sub_sent"]).click()
                if cm.is_displayed(data["mail"]["icon"]) == True :  
                    cm.msg("p",data["msg_mail"]["pass_sub_sent"])
                    par = driver.find_element_by_xpath(data["mail"]["list_mail"])
                    mail = par.find_elements_by_xpath(data["mail"]["mail"])
                    if len(mail) == 0 :
                        cm.msg("p",data["msg_mail"]["pass_displayed"])
                    else :
                        i=0
                        while i <= len(mail) :
                            title1 = driver.find_elements_by_xpath(data["mail"]["title1"] + str(i) + data["mail"]["title2"]).text
                            if title1 == subject :
                                displayed = True
                                cm.msg("p",data["msg_mail"]["pass_displayed"])
                                break
                        if displayed == False :
                            cm.msg("p",data["msg_mail"]["fail_displayed"])

                else :
                    cm.msg("p",data["msg_mail"]["fail_sub_sent"]) 
        else :
            cm.msg("p",data["msg_mail"]["pass_no_send"])
        
            
    
    
    
    

