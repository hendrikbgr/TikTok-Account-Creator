# 🚀 This Project is in it's early stages of Development.
# 📌 Working on new features and main menu.
# ⚠️ Any Questions or Suggestions please Mail to: hendriksdevmail@gmail.com
# 🖥 Version: 1.0.2

from selenium import webdriver
import warnings
import time
import random
import string
import requests
import csv
import sys
import os
clear = lambda: os.system('clear')
clear()
i = 0
#Options
#-------------
#Emial Options
#-------------
auto_email = "true"


print ("""\
 _____ _ _  _____     _              
|_   _(_) ||_   _|   | |             
  | |  _| | _| | ___ | | __          
  | | | | |/ / |/ _ \| |/ /          
  | | | |   <| | (_) |   <           
  \_/ |_|_|\_\_/\___/|_|\_\                                                                               
  ___                            _   
 / _ \                          | |  
/ /_\ \ ___ ___ ___  _   _ _ __ | |_ 
|  _  |/ __/ __/ _ \| | | | '_ \| __|
| | | | (_| (_| (_) | |_| | | | | |_ 
\_| |_/\___\___\___/ \__,_|_| |_|\__|                                                                    
 _____                _              
/  __ \              | |             
| /  \/_ __ ___  __ _| |_ ___  _ __  
| |   | '__/ _ \/ _` | __/ _ \| '__| 
| \__/\ | |  __/ (_| | || (_) | |    
 \____/_|  \___|\__,_|\__\___/|_|    
                                       
""")
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML) Chrome/83.0.4103.97 Safari/537.36")
profile.set_preference("media.volume_scale", "0.0")
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
webdriver = webdriver.Firefox(executable_path="./geckodriver", firefox_profile=profile)
driver = webdriver
# Change Path to Chrome Driver Path (or move your ChromeDriver into the project folder)

url = 'https://www.tiktok.com/signup/phone-or-email/email'

def randomStringDigits(stringLength=13):
    # Generate a random string of letters and digits
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
rngpassword = randomStringDigits(15)
driver.get(url)
time.sleep(5)
#Change Language
print()
print("Setting Language to English")
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/select').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/select/option[4]').click()
time.sleep(1)

#Setting Birth Date
#Setting Month
print()
print("Setting Birthday Month")
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[2]/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[2]/div[1]/ul/li[1]').click()
time.sleep(1)

#Setting Day
print()
print("Setting Birthday Day")
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[2]/div[2]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[2]/div[2]/ul/li[1]').click()
time.sleep(1)

#Setting Year
print()
print("Setting Birthday Year")
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[2]/div[3]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[2]/div[3]/ul/li[20]').click()
time.sleep(1)

#Setting Email Address
print()
print('Setting Email Address')
if auto_email == "true":
    get_response = requests.get("https://lazy-mail.com/mailbox/create/random")
    csrf_token = get_response.text.split("input type=\"hidden\" name=\"_token\" value=\"")[1].split("\"")[0]
    post_data = {"_token": csrf_token}
    post_response = requests.post("https://lazy-mail.com/mailbox/create/random", data=post_data,cookies=get_response.cookies)
    generated_email = post_response.url.split("mailbox/")[1]
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[4]/div[2]/div/input").send_keys(generated_email)
else:
    email = input("Enter your Email: ")
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[4]/div[2]/div/input").send_keys(email)
time.sleep(1)

#Setting Password
print()
print("Setting Password: {}".format(rngpassword))
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[4]/div[4]/div[1]/input').send_keys(rngpassword)
time.sleep(1)

#Sending Email
print()
print("Sending Email")
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[4]/div[5]/button').click()
time.sleep(1)

#Waiting for code
print()
print("Waiting for Code")
if auto_email == "true":
    while (True):
        get_emails = requests.get("https://lazy-mail.com/mail/fetch?new=true", cookies=post_response.cookies)
        get_emails = requests.get("https://lazy-mail.com/mail/fetch", cookies=post_response.cookies)
        if "Verification Code" not in get_emails.text:
            time.sleep(10)
        else:
            get_code = get_emails.text.split("ext\":\"To verify your account, enter this code in TikTok:<br\/>")[1].split("\"")[0]
            break
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[4]/div[5]/div/input').send_keys(get_code)
else:
    code = input('Enter Code got by Email: ')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[4]/div[5]/div/input').send_keys(code)