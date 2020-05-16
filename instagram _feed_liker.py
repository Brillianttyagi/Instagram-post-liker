from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
try:
    Username = str(input("Enter your username>>"))
    Password = str(input("Enter your password>>"))
    print("\t\tYOU ARE ALL SET!!\n\tKEEP WORKING YOUR TIME IS PRECIOUS\nI will like all your new feed posts of instagram until you close me")
    sleep(8)
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(20)
    driver.get("https://www.instagram.com/")
    sleep(4)


    driver.find_element_by_name("username").send_keys(Username)
    driver.find_element_by_name("password").send_keys(Password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    sleep (2)

    notnow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
    notnow.click()
    sleep(10)
    while(True):
        driver.refresh()
        sleep(5)
        for i in range(1,20):
            try:
                like = driver.find_element_by_xpath('//*[name()="svg" and @aria-label="Like"][@width="24"]')
                sleep(5)
                like.click()
                sleep(5)
            except:
                pass
        sleep(480)
except:
    print("i think you close chrome or your id or password are wrong")
    print("open me once again and type your correct username password")
    sleep(8)

    
