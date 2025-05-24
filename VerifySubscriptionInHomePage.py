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
confirmation = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/footer/div[1]/div/div/div[2]/div/h2"))
)

print("subscription field appeared successfully!")
elem = driver.find_element(By.XPATH,"/html/body/footer/div[1]/div/div/div[2]/div/form/input[2]")
elem.send_keys("yasser@gmail.com")
elem = driver.find_element(By.XPATH,"/html/body/footer/div[1]/div/div/div[2]/div/form/button")
elem.click()
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'You have been successfully subscribed!')]"))
)
print("you have been subscribed successfully!")