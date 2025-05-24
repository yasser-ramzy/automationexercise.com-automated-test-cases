from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://automationexercise.com/")
driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a").click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/p[2]/a/u"))
).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div[2]/table/tbody/tr/td[6]/a"))
).click()