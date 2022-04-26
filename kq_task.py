from math import fabs
from time import time
from tkinter.tix import Tree
from kq_setup import driver
from kq_lib_common import By , data, time,cm

def task():
    ac_menu = write = title1 = content1 = recipient = True
    work_diary  = "Work Diary " + cm.to_day
    task_report  = "Task Report  " + cm.to_day
    content = "Content"
    if cm.is_displayed(data["task"]["bt_write"]) == True : 
        cm.msg("p",data["msg_task"]["pass_access"])
    else :
        ac_menu = False
        cm.msg("f",data["msg_task"]["fail_access"])

    if ac_menu == True :
        # WRITE WORK DIARY 
        # Click on wtite button
        driver.find_element_by_xpath(data["task"]["bt_write"]).click()
        if cm.is_displayed(data["task"]["bt_di_save"]) == True :  
            cm.msg("p",data["msg_task"]["pass_write"])
        else :
            write = False
            cm.msg("f",data["msg_task"]["fail_write"])

        if write == True :
            # Enter title work diary 
            title = driver.find_element_by_xpath(data["task"]["title_di"])
            title.send_keys(work_diary)
            if title.text == work_diary :
                cm.msg("p",data["msg_task"]["pass_title_di"])
            else :
                title1 = False
                cm.msg("f",data["msg_task"]["fail_title_di"])

            # Enter Content work diary
            editor = driver.find_element_by_xpath(data["editor"])
            editor.send_keys(content)
            if editor.text == content :
                cm.msg("p",data["msg_task"]["pass_content"])
            else :
                content1 = False
                cm.msg("f",data["msg_task"]["fail_content"])

            if title1 == True and content1 == True :
                driver.find_element_by_xpath(data["task"]["bt_save"]).click()
                if cm.is_displayed(data["task"]["bt_back"]) == True :  
                    cm.msg("p",data["msg_task"]["pass_save"])
                else :
                    write = False
                    cm.msg("f",data["msg_task"]["fail_save"])

        #WRITE TASK REPORT  
        driver.find_element_by_xpath(data["task"]["bt_write"]).click()
        if cm.is_displayed(data["task"]["bt_di_save"]) == True :  
            cm.msg("p",data["msg_task"]["pass_write"])

            # Enter title task report 
            title = driver.find_element_by_xpath(data["task"]["title_di"])
            title.send_keys(task_report)
            if title.text == task_report :
                cm.msg("p",data["msg_task"]["pass_title_di"])
            else :
                title1 = False
                cm.msg("f",data["msg_task"]["fail_title_di"])

            # Choose recipient
            driver.find_element_by_xpath(data["task"]["org"]).click()
            if cm.is_displayed(data["task"]["search"]) == True :  
                cm.msg("p",data["msg_task"]["pass_ic_org"])

                # Click on search icon 
                driver.find_element_by_xpath(data["task"]["search"]).click()
                if cm.is_displayed(data["task"]["bt_search"]) == True :  
                    cm.msg("p",data["msg_task"]["pass_ic_search"])
                    recipient = cm.add_recipient()
                else :
                    cm.msg("f",data["msg_task"]["fail_ic_search"])


            else :
                cm.msg("f",data["msg_task"]["fail_ic_org"])

            # Enter content 
            editor = driver.find_element_by_xpath(data["editor"])
            editor.send_keys(content)
            if editor.text == content :
                cm.msg("p",data["msg_task"]["pass_content"])
            else :
                content1 = False
                cm.msg("f",data["msg_task"]["fail_content"])

            # Save task
            if title1 == True and  content1 == True and  recipient == True :
                driver.find_element_by_xpath(data["task"]["bt_save"]).click()
                if cm.is_displayed(data["task"]["bt_ok"]) == True :  
                    cm.msg("p",data["msg_task"]["pass_save"])
                    driver.find_element_by_xpath(data["task"]["bt_ok"]).click()
                    if cm.is_displayed(data["task"]["bt_back"]) == True :  
                        cm.msg("p",data["msg_task"]["pass_save"])
                    else :
                        write = False
                        cm.msg("f",data["msg_task"]["fail_save"])
                else :
                    cm.msg("f",data["msg_task"]["fail_save"])


        else :
            write = False
            cm.msg("f",data["msg_task"]["fail_write"])