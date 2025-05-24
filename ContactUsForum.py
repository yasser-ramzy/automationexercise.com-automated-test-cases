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
elem = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[8]/a")
elem.click()
elem = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[1]/input")
elem.send_keys("yasser")
elem = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[2]/input")
elem.send_keys("yasser@gmail.com")
elem = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[3]/input")
elem.send_keys("subject form material")
elem = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[4]/textarea")
elem.send_keys("type any thing you what to send in the message body")
elem = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[6]/input")
elem.click()
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()
try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]"))
    )
    print("Confirmation is visible – test passed.")
except:
    print("Confirmation not visible – test failed.")
    driver.quit()