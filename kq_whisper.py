from math import fabs
from time import time
from tkinter.tix import Tree
from kq_setup import driver
from kq_lib_common import By , data, time,cm

def whisper():

    ac_menu = content1 =True
    content = "Content"

    if cm.is_displayed(data["whisper"]["bt_write"]) == True : 
        cm.msg("p",data["msg_whisper"]["pass_access"])
    else :
        ac_menu = False
        cm.msg("f",data["msg_whisper"]["fail_access"])

    if ac_menu == True :
        driver.find_element_by_xpath(data["whisper"]["bt_write"]).click()
        if cm.is_displayed(data["whisper"]["bt_send"]) == True : 
            cm.msg("p",data["msg_whisper"]["pass_write"])

            # Add recipient
            driver.find_element_by_xpath(data["whisper"]["ic_org"]).click()
            recipient = cm.add_recipient()

            # Enter content 
            # Enter Content work diary
            editor = driver.find_element_by_xpath(data["editor"])
            editor.send_keys(content)
            if editor.text == content :
                cm.msg("p",data["msg_whisper"]["pass_content"])
            else :
                content1 = False
                cm.msg("f",data["msg_whisper"]["fail_content"])
            
            # Send whisper
            if recipient == True and content1 == True :
                driver.find_element_by_xpath(data["whisper"]["bt_send"]).click()
                if cm.is_displayed(data["whisper"]["bt_write"]) == True : 
                    cm.msg("p",data["msg_whisper"]["pass_send"])
                else :
                    ac_menu = False
                    cm.msg("f",data["msg_whisper"]["fail_send"])
            

        else :
            ac_menu = False
            cm.msg("f",data["msg_whisper"]["pass_write"])
        
