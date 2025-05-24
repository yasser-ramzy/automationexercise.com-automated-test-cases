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
elem = driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a")
elem.click()
elem = driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/input[1]")
elem.clear()
elem.send_keys("4")
elem = driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button")
elem.click()
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div[2]/div[1]/div/div/div[2]/p[2]/a"))
)
viewcart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div/div[2]/div[1]/div/div/div[2]/p[2]/a/u"))
)

viewcart.click()
quantity = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div[2]/table/tbody/tr[1]/td[4]"))
)

# Check if quantity is 4
if quantity.text == "4":
    print("✅ Quantity is correct!")
else:
    print("❌ Quantity is incorrect. Found:", quantity.text)
