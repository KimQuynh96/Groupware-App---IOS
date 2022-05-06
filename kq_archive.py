from math import fabs
from re import L
from time import time
from kq_setup import driver
from kq_lib_common import By , data, time,cm

def archive():
    title_ar = content = "Archive" + cm.to_day()
    content1 = title1 = True
    
    driver.find_element_by_xpath(data["archive"]["menu"]).click()
    if cm.is_displayed(data["archive"]["left"]) == True :
        cm.msg("p",data["msg_archive"]["pass_access"])

        # Go to My Archive folder #
        driver.find_element_by_xpath(data["archive"]["my"]).click()
        if cm.is_displayed(data["archive"]["pass"]) == True :
            cm.msg("p",data["msg_archive"]["pass_my"])

            pw = driver.find_element_by_xpath(data["archive"]["pass"])
            pw.send_keys("matkhau1!")
            driver.find_element_by_xpath(data["archive"]["enter"]).click()
            if cm.is_displayed(data["archive"]["bt_wr"]) == True :
                cm.msg("p",data["msg_archive"]["pass_folder"]) 
                
                # Craete archive 
                driver.find_element_by_xpath(data["archive"]["bt_wr"]).click()
                if cm.is_displayed(data["archive"]["bt_save"]) == True :
                    cm.msg("p",data["msg_archive"]["pass_wr"])  

                    # Enter Title archive 
                    title = driver.find_element_by_xpath(data["archive"]["ip_title"])
                    title.send_keys(title_ar)
                    if title.text == title_ar :
                        cm.msg("p",data["msg_archive"]["pass_title"])  
                    else :
                        title1 = False
                        cm.msg("f",data["msg_archive"]["fail_title"]) 

                    # Enter content archive 
                    editor = driver.find_element_by_xpath(data["editor"])
                    editor.send_keys(content)
                    if editor.text == content :
                        cm.msg("p",data["msg_whisper"]["pass_content"])
                    else :
                        content1 = False
                        cm.msg("f",data["msg_whisper"]["fail_content"])
                    
                    # Save 
                    if title1 == True and content1 == True :
                        driver.find_element_by_xpath(data["archive"]["bt_save"]).click()

                        if cm.is_displayed(data["archive"]["bt_wr"]) == True :
                            cm.msg("p",data["msg_archive"]["pass_save"])  
                        else :
                            cm.msg("p",data["msg_archive"]["fail_save"])  
                        
                        

                else :
                    cm.msg("f",data["msg_archive"]["fail_wr"])
            else :
                cm.msg("f",data["msg_archive"]["fail_folder"]) 
        else :
            cm.msg("f",data["msg_archive"]["fail_my"])
    else :
        cm.msg("f",data["msg_archive"]["fail_access"])

