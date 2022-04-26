from datetime import date, datetime
from time import time
from unittest import result
from kq_setup import driver
from kq_lib_common import By , data, time,cm

def board():
    result_save = False
    title = data["board"]["title"] + cm.to_day()
    content = data["board"]["content"]
    
    driver.find_element_by_xpath(data["board"]["menu"]).click()
    if cm.is_displayed(data["board"]["bt_wr"]) == True :
        cm.msg("p",data["msg_board"]["pass_ac_menu"])
    else :
        cm.msg("f",data["msg_board"]["fail_ac_menu"])


    driver.find_element_by_xpath(data["board"]["bt_wr"]).click()
    time.sleep(5)
    title_board = driver.find_element_by_id(data["board"]["ip_title"])
    title_board.send_keys(title)
    
    if title_board == title_board.text() :
        cm.msg("p",data["msg_board"]["pass_title"])
    else :
        cm.msg("f",data["msg_board"]["fail_title"])

    driver.swipe(start_x=523,start_y=1778,end_x=523,end_y=1089,duration=800)
    time.sleep(3)

    driver.switch_to.frame(driver.find_element_by_id(data["board"]["ifame"]))
    editor = driver.find_element_by_xpath(data["board"]["editor"])
    driver.switch_to.default_content()
    editor.send_keys(content)
    if content == editor.text() :
        cm.msg("p",data["msg_board"]["pass_content"])
    else :
        cm.msg("f",data["msg_board"]["fail_content"])
    driver.find_element_by_xpath(data["board"]["bt_save"]).click()
    if cm.is_displayed(data["board"]["bt_wr"]) == True :
        cm.msg("p",data["msg_board"]["pass_save"])
    else :
        cm.msg("f",data["msg_board"]["fail_save"])

    i = 1
    list_board = driver.find_elements_by_xpath(data["board"]["list_board"])
    while i < list_board :
        title_post = driver.find_element_by_xpath(data["board"]["title_pt"]+str(i)+"]").text
        if title_post == title :
            result_save = True 
            break

    if result_save == True :
        cm.msg("p",data["msg_board"]["pass_display"])
    else :
        cm.msg("f",data["msg_board"]["fail_display"])



    









    
    
        
    

    
    
    
    
    

