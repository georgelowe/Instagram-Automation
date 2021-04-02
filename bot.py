import os
from time import sleep
from random import randint
from secrets import (username,password)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# To do:
# [x] Improve find_unfollowers() function so data is scraped if not present already for a particular user
# [x] Refactor the following / followers methods into one function
# [] Implement method to like pictures for a particular hashtag
# [] Implement method to comment on pictures for a particular hashtag --> list of various comments
# [] Implement method to comment on pictures for a particular hashtag --> list of various comments
# [] Implement method to interact with a list of rep accounts --> list of various comments
# [] Make sure I read the rules around daily interaction limits
# [] Need to make sure when comparing that ALL followers and followings exist else the result is not accurate

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

# Get users that are either followed by or following a particular account
# Mode parameter needs to be "following" or "followers"
# Results are stored in text files, one for followers and one for following
def get_usernames(driver, account, count, mode):

    target_user_link = 'https://www.instagram.com/{}/'.format(account)
    if(driver.current_url != target_user_link):
        driver.get(target_user_link)
        sleep(4)

    if(mode == "followers"):
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').click()
    if(mode == "following"):
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').click()
    else:
        print("Invalid mode...")

    sleep(3)
    count = count + 1
    f = open_file(account, mode)

    for i in range(1,count):
        user = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[%s]' % i)
        driver.execute_script("arguments[0].scrollIntoView();", user)
        sleep(1)
        text = user.text
        list = text.encode('utf-8').split()
        item = list[0].decode('utf-8')
        f.write(item + "\r\n")
    
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button/div').click()
    f.close()


# Compare text files of followers vs following to find accounts that don't reciprocate following
def find_unfollowers(account):

    if(not os.path.isfile(account + "-following.txt") and not os.path.isfile(account + "-followers.txt")):
        print("Error: Followers/following data does not exist for this user \n")
        return 

    with open(account + "-following.txt", 'r') as file1:
        with open(account + "-followers.txt", 'r') as file2:
            same = set(file1).difference(file2)

    same.discard('\n')

    f = open_file(account, "comparison")
    with f as file_out:
        for line in same:
            file_out.write(line)

    print("Comparison complete...")
        
# Open a file to write to
def open_file(account, mode):
    dirname = os.path.dirname(os.path.abspath(__file__))
    csvfilename = os.path.join(dirname, account + "-" + mode + ".txt")
    file_exists = os.path.isfile(csvfilename)
    f = open(csvfilename,'a')
    return f

# Close the browser once finished with the bot
def close_browser(driver):
    driver.close()

if __name__ == "__main__":

    driver = config_driver()
    instagram_login(driver,username,password)
    account = input("Which account would you like to scrape? ")
    count = int(input("How many users does " + account + " follow? "))
    get_usernames(driver, account, count, "following")
    count = int(input("How many followers does " + account + "have? "))
    get_usernames(driver, account, count, "followers")

    
    
        
        
