
from time import sleep
from secrets import username
from secrets import password

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver.get('https://www.instagram.com/explore/tags/dog/')

def config_driver():
    driver = webdriver.Chrome()
    return driver

def instagram_login(driver, username, password):
    driver.get('https://www.instagram.com')
    sleep(3)

    driver.implicitly_wait(20)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
    username_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    username_input.send_keys(username)

    driver.implicitly_wait(20)
    password_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password_input.send_keys(password)

    sleep(2)
    driver.implicitly_wait(20)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click() 

    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(1)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

def interact_with_hashtags(driver,hashtag)
    driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))

if __name__ == "__main__":
 
        driver = config_driver()
        instagram_login(driver,username,password)
        var hashtag = "doggy"
        interact_with_hashtags(driver,hashtag)