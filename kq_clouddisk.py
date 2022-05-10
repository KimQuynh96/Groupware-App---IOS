from math import fabs
from time import time
from kq_setup import driver
from kq_lib_common import By , data, time,cm

def clouddisk():
    driver.find_element_by_xpath(data["clouddisk"]["menu"]).click()
    if cm.is_displayed(data["clouddisk"]["bt_upload"]) == True :
        cm.msg("p",data["msg_cld"]["pass_access"])
        driver.find_element_by_xpath(data["clouddisk"]["bt_upload"]).click()
        if cm.is_displayed(data["clouddisk"]["ic_upload"]) == True :
            cm.msg("p",data["msg_cld"]["pass_popup"]) 
            driver.find_element_by_xpath(data["clouddisk"]["ic_upload"]).click()
        else :
            cm.msg("f",data["msg_cld"]["fail_popup"]) 

    else :
        cm.msg("f",data["msg_cld"]["fail_access"])