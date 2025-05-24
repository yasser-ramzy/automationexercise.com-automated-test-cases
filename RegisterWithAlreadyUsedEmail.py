from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://automationexercise.com/")
elem = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")
elem.click()
elem = driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[2]")
elem.send_keys("yasser")
elem = driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[3]")
elem.send_keys("yasserramzy6@gmail.com")
elem = driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/button")
elem.click()
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div[3]/div/form/p"))
    )
    print("Email already registered")
except:
    print("test failed")