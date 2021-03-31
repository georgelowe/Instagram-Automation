
from time import sleep
from secrets import username
from secrets import password

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import os

# Configure the selenium web driver
def config_driver():
    driver = webdriver.Chrome()
    return driver

# Login to a given instagram account and bypass notification alerts
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

# def interact_with_hashtags(driver,hashtag):
#     driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))

# # Get users that an account is followed by and store in a text file
# def get_list_of_followers(driver, account):
#     target_user_link = 'https://www.instagram.com/{}/'.format(account)
#     driver.get(target_user_link)
#     time.sleep(4)
#     # //*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span

# # Get users that an account follows and store in a text file
def get_list_of_following(driver, account):
    target_user_link = 'https://www.instagram.com/{}/'.format(account)
    driver.get(target_user_link)
    sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').click()
    sleep(3)
    count = int(input("How many users do you want to scrape?"))

    for i in range(1,count):
        scr1 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[%s]' % i)
        driver.execute_script("arguments[0].scrollIntoView();", scr1)
        sleep(1)
        text = scr1.text
        print(text)
        list = text.encode('utf-8').split()
        dirname = os.path.dirname(os.path.abspath(__file__))
        csvfilename = os.path.join(dirname, account + "-" + "following" + ".txt")
        file_exists = os.path.isfile(csvfilename)
        f = open(csvfilename,'a')
        f.write(str(list[0]) + "\r\n")
        f.close()
        print('{};{}'.format(i, list[0]))
        
# # Compare the lists of followers vs following and create file of accounts to unfollow
# def calculate_unfollowers(driver):


# # Write usernames to a file
# def write_to_file(filename, users):
#     filename = filename + ".txt"
#     f = open(filename, w)
#     s1 = '\n'.join(users)
#     f.write(s1)
#     f.close()
    



# # Close the browser once finished with the bot
# def close_browser(driver):
#     driver.close()

if __name__ == "__main__":
    driver = config_driver()
    driver = config_driver()
    instagram_login(driver,username,password)
    account_to_scrape = "thepawtraitdesignco"
    get_list_of_following(driver, account_to_scrape)

    
        
        
