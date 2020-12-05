#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from time import sleep 


def run_chrome(url):
	# Will allow us to specify options for our chromedriver
	options = ChromeOptions()
	# Turn off logging
	options.add_argument('log-level=3')
	# Start browser in full screen mode
	options.add_argument("start-maximized")
    # Start browser in headless mode 
    options.add_argument("headless")


	# Starting browser with specified options and sending all logs to null file
	driver = Chrome(executable_path=path_to_driver, options=options)
	
	return driver

def open_tab(driver, new_tab_url):
    # Open new tab with keyboard shortcut CTRL + t
    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
     
    # Open new url
    driver.get(new_tab_url)

    return driver


def close_tab(driver):
    # .close closes the currently opened tab
    driver.close()    


def main():
    # Start firefix in headless mode
    driver = start_firefox("http://www.google.com", headless=False) 

    print(driver.title)
    print(driver.session_id)
    print(driver.get_cookies())

    # Select HTML tag by name
    search = driver.find_element_by_name('q')

    # Send string to search for
    search.send_keys("How much wood could a wood chuck chuck?")

    # Press enter
    search.send_keys(Keys.RETURN)

    sleep(1)

    # Opening new tab
    driver = open_tab(driver, "http://www.fullstackacademy.com")

    print(driver.title)
    print(driver.session_id)

    # Close currently opened tab
    close_tab(driver)

    # .quit closes all the entire browser
    driver.quit()


if __name__ == "__main__":
    main()
