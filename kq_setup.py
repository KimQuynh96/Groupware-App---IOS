import os
import unittest
import os
from appium import webdriver

APPIUM_PORT = '4723'
udid = 'bc86e429485c13f34837866fde36e7ed55646317'
app_path = 'Users/hanbiro/Desktop/kimquynhios/HybridMobileCRM.ipa'
command_executor ='http://127.0.0.1:%s/wd/hub' % APPIUM_PORT

desired_capabilities = {
    'orientation' :'LANDSCAPE',
    "deviceName": "Hanbiro Iphone",
    "platformVersion": "12.5.5",
    "platformName": "IOS",
    "udid": udid,
    "autoWebView":True,
    "fullContextList" : True,
    
    #"safari"
    "browserName":"Safari",
    "safariAllowPopups":True

    #"app"
    #"app": app_path,
    #"enablePerformanceLogging" :True,
    #"intrumentApp":True,
}



driver = webdriver.Remote(command_executor,desired_capabilities)



