from math import fabs
from time import time
from kq_setup import driver
from kq_lib_common import By , data, time,cm

def contact():

    work_name = "Project" + cm.to_day()
    driver.find_element_by_xpath(data["project"]["menu"]).click()
    if cm.is_displayed(data["project"]["bt_wr"]) == True :
        cm.msg("p",data["msg_pro"]["pass_access"])

        pro_list = driver.find_elements_by_xpath(data["project"]["pro_list"])
        total_pro = len(pro_list)
        if total_pro > 0 :
            # Choose first project to add work 
            driver.find_element_by_xpath(data["project"]["pro"]).click()
            if cm.is_displayed(data["project"]["more"]) == True :
                cm.msg("p",data["msg_pro"]["pass_pro"])

                work_list = driver.find_elements_by_xpath(data["project"]["wor_list"])
                total_before = len(work_list)
                # Click add work icon  
                driver.find_element_by_xpath(data["project"]["work"]).click()
                if cm.is_displayed(data["project"]["save"]) == True :
                    cm.msg("p",data["msg_pro"]["pass_ic"])

                    # Add work name
                    name = driver.find_element_by_xpath(data["project"]["name"])
                    name.send_keys(work_name)
                    
                    if work_name == name.text() :
                        cm.msg("p",data["msg_pro"]["pass_title"])

                        # Save work 
                        driver.find_element_by_xpath(data["project"]["save"]).click()
                        if cm.is_displayed(data["project"]["work"]) == True :
                            cm.msg("p",data["msg_pro"]["pass_work"])

                            work_list1 = driver.find_elements_by_xpath(data["project"]["wor_list"])
                            total_after = len(work_list1)
                            if total_before + 1 == total_after :
                                cm.msg("p",data["msg_pro"]["pass_display"])
                            else :
                                cm.msg("f",data["msg_pro"]["fail_display"])

                        else :
                            cm.msg("f",data["msg_pro"]["fail_work"])

                    else :
                        cm.msg("f",data["msg_pro"]["fail_title"])
                else :
                    cm.msg("f",data["msg_pro"]["fail_ic"])
            else :
                cm.msg("f",data["msg_pro"]["fail_pro"])
        else :
            # Add Project
            driver.find_element_by_xpath(data["project"]["bt_wr"]).click()
            
    else :
        cm.msg("f",data["msg_pro"]["pass_access"]) 
