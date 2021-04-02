# Get users that an account is followed by and store in a text file
def get_list_of_followers(driver, account, count):
    target_user_link = 'https://www.instagram.com/{}/'.format(account)
    driver.get(target_user_link)
    sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').click()
    sleep(3)

    count = count + 1

    f = open_file(account, "followers")

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

# Get users that an account follows and store in a text file
def get_list_of_following(driver, account, count):
    target_user_link = 'https://www.instagram.com/{}/'.format(account)
    driver.get(target_user_link)
    sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').click()
    sleep(3)

    count = count + 1

    f = open_file(account, "following")
   
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


# Refactor the above two functions into one function
def get_usernames(driver, account, count, mode):

    target_user_link = 'https://www.instagram.com/{}/'.format(account)
    if(driver.current_url != target_user_link):
        driver.get(target_user_link)
        sleep(4)
    
    if(mode == "following"):
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').click()
    if(mode == "followers"):
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').click()
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




    


def testif():
    a =10
    b = 5
    if(a!=b):
        print("worked")
    else:
        print("else")

if __name__ == "__main__":
    