from kq_setup import driver
from kq_lib_common import data,time,cm

def login():
    
    driver.get("https://global3.hanbiro.com")    
    time.sleep(20)
    id = driver.find_element_by_xpath(data["login"]["id"])
    id.click()
    id.send_keys("ts1")

    time.sleep(5)
    driver.switch_to.frame(driver.find_element_by_id("iframeLoginPassword"))
    ps = driver.find_element_by_xpath(data["login"]["ps"])
    ps.click()
    ps.send_keys("matkhau1!")
    driver.switch_to.default_content()

    time.sleep(2)
    bt = driver.find_element_by_xpath(data["login"]["bt_lg"])
    bt.click()

    time.sleep(10)
    
    if cm.is_displayed(data["login"]["hybrid"]) == True :
        cm.msg("p",data["msg_log"]["pass_log"])
        return True
    else :
        cm.msg("f",data["msg_log"]["fail_log"])
        return False





    #app#
    '''
    domain = driver.find_element_by_ios_class_chain(data["domain"])
    domain.clear()
    domain.send_keys(data["key_domain"])
    cm.msg("p",data["msg_log"]["pass_domain"])

    id = driver.find_element_by_ios_class_chain(data["id"])
    id.clear()
    id.send_keys(data["key_id"])
    cm.msg("p",data["msg_log"]["pass_id"])

    pas = driver.find_element_by_ios_class_chain(data["pass"])
    pas.clear()
    pas.send_keys(data["key_pass"])
    cm.msg("p",data["msg_log"]["pass_pass"])


    time.sleep(5)
    bt_login = driver.find_element_by_accessibility_id(data["bt_login"])
    bt_login.click()
    cm.msg("p",data["msg_log"]["pass_bt_log"])

    if cm.is_displayed(data["toolbar"]) == True :
        cm.msg("p",data["msg_log"]["pass_log"])
        return True
    else :
        cm.msg("p",data["msg_log"]["fail_log"])
        return False
    '''



    
    



