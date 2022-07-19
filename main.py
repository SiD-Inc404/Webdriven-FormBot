from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random

# ALGORITHMS

# First item is empty, so that index of scope[] can match with question number
# Each option in the question is a Map, the key being the option value, and the value being its XPath
print('ACTIVATING SCOPE')
scope = [
    {},
    {
        3:
        '//*[@id="i8"]/div[3]/div',
        4:
        '//*[@id="i11"]/div[3]/div',
        5:
        '//*[@id="i14"]/div[3]/div',
        0:
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
    },
    {
        8: '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        10: '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        15: '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        20: '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
    },
    {
        "yes": '//*[@id="i33"]/div[3]/div',
        "no": '//*[@id="i36"]/div[3]/div'
    },
    {
        "hang it on a hook": '//*[@id="i43"]/div[3]/div',
        "place it in a laundry basket": '//*[@id="i46"]/div[3]/div',
        "place it in a closed container": '//*[@id="i49"]/div[3]/div',
        "throw it away": '//*[@id="i52"]/div[3]/div',
    },
    {
        "limitations":
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea'
    },
]

# SETUP WEBDRIVER
print('INITIALISING WEBDRIVER')
option = Options()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument("--headless")
option.add_argument("disable-gpu")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
# browser = webdriver.Chrome(executable_path='./chromedriver', options=option)


# CLASS SELECTORS
# submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

# XPATH SELECTORS

def submitResponse():
    browser.get("https://forms.gle/cADiu4wdfWZX3nSQ9")
    qnNo = 0
    for qn in scope:
        if (qnNo == 1):
            randomChoice = [3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5]
            browser.find_elements(By.XPATH,scope[qnNo][random.choice(randomChoice)])[0].click()
        if (qnNo == 2):
            randomChoice = [8, 8, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20]
            choice = random.choice(randomChoice)
            browser.find_elements(By.XPATH,scope[qnNo][choice])[0].send_keys(str(choice))
        if (qnNo == 3):
            randomChoice = ['yes', 'no']
            browser.find_elements(By.XPATH,scope[qnNo][random.choice(randomChoice)])[0].click()
        if (qnNo == 4):
            randomChoice = [
                "hang it on a hook","hang it on a hook","hang it on a hook",
                "place it in a laundry basket",
                "place it in a closed container","place it in a closed container",
                "throw it away"
                ]
            browser.find_elements(By.XPATH,scope[qnNo][random.choice(randomChoice)])[0].click()
        if (qnNo==5):
            browser.find_elements(By.XPATH,scope[qnNo]['limitations'])[0].send_keys(
                random.choice([
                    'nil',
                    'masks exposed to dust',
                    'masks become dirty',
                    'unhygienic',
                    'inconvenient',
                ])
            )
        qnNo+=1
    browser.find_elements(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')[0].click()

# SEND ACTIONS
targ_resp = 10
sent_resp = 0
print('SENDING ' + str(targ_resp) + ' RESPONSES')
while sent_resp < targ_resp:
    print('SUBMITTING RESPONSE #'+str(sent_resp))
    submitResponse()
    print('    SUCCESS')
    sent_resp += 1

# CLOSE INSTANCE
print('DISPOSING BROWSER INSTANCE')
browser.close()
