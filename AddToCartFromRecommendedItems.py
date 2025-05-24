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
heading = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section[2]/div/div/div[2]/div[2]/h2")))
print("🔍 Heading text is:", heading.text)
if heading.text == "RECOMMENDED ITEMS":
    print("RECOMMENDED ITEMS successfully appears")
else :
    print("test failed")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

# Add first item to cart
add_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/section[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/a")
))
add_button.click()
time.sleep(2)

# View cart
view_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']")))
view_cart.click()
time.sleep(3)

print("✅ Successfully added item to cart!")
driver.quit()
