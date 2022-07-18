from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random

# ALGORITHMS
# numbers represent the index of the answers
opts = {
    1: [1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3],
    2: [15, 16, 17, 18, 19, 20, 21, 22],
    3: [0, 0, 0, 0, 1],
    4: [0, 2, 3],
    5: ['not convenient', 'masks can become dirty', 'nil']
}

# First item is empty, so that index of scope[] can match with question number
# Each option in the question is a dictionary, the key being the option value, and the value being its XPath
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

option = Options()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument("--headless")
option.add_argument("disable-gpu")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
# browser = webdriver.Chrome(executable_path='./chromedriver', options=option)
browser.get("https://forms.gle/cADiu4wdfWZX3nSQ9")

# CLASS SELECTORS
# submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

# XPATH SELECTORS
qnNo = 1
for qn in scope:
    if (qnNo == 1):
        randomChoice = [3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5]
        browser.find_elements(By.XPATH,scope[1][random.choice(randomChoice)])[0].click()
    if (qnNo == 2):
        randomChoice = []
        

# SEND ACTIONS

# CLOSE INSTANCE
browser.close()
