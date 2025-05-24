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
elem = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[2]/a")
elem.click()
elem = driver.find_element(By.XPATH,"/html/body/section[1]/div/input")
elem.send_keys("blue top")
elem = driver.find_element(By.XPATH,"/html/body/section[1]/div/button")
elem.click()
confirmation = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]"))
)

print("blue top appears successfully !")