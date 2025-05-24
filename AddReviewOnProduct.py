from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get("https://automationexercise.com/")
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[2]/a").click()
heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'All Products')]")))
print("🔍 Heading text is:", heading.text)
driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a").click()
heading2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div[2]/div[3]/div[1]/ul/li/a")))
print("🔍 Heading text is:", heading2.text)
driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div[3]/div[2]/div/div/form/span/input[1]").send_keys("yasser")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div[3]/div[2]/div/div/form/span/input[2]").send_keys("yasserramzy6@gmail.com")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div[3]/div[2]/div/div/form/textarea").send_keys("i like this product")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div[3]/div[2]/div/div/form/button").click()
expected_message = "Your form has been submitted successfully!"
message_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, f"//*[contains(text(),'Thank you for your review')]"))
)

print("✅ Message appeared:", message_element.text)