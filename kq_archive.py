from math import fabs
from re import L
from time import time
from kq_setup import driver
from kq_lib_common import By , data, time,cm

def archive():
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
            

        else :
            cm.msg("f",data["msg_archive"]["fail_my"])
    else :
        cm.msg("f",data["msg_archive"]["fail_access"])

