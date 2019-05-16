#!/usr/bin/env python

import rospy

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(firefox_options=options)

control_url = rospy.get_param("control_url", "http://10.5.5.9/gp/gpControl/execute?p1=gpStream&a1=proto_v2&c1=restart") # gopro5 session

driver.get(control_url)

while not rospy.is_shutdown():

    rospy.loginfo("refresh")
    time.sleep(10)
    driver.refresh()
