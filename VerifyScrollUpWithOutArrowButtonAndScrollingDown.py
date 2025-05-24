from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# Open website
driver.get("https://automationexercise.com/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
heading = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/footer/div[1]/div/div/div[2]/div/h2")))
print("🔍 Heading text is:subscription",heading.text)
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
heading2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section[1]/div/div/div/div/div/div[2]/div[1]/h2")))
print("🔍 Heading text is: Full-Fledged practice website for Automation Engineers", heading2.text)
time.sleep(2)
driver.quit()