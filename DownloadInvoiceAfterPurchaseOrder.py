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

# Click on first product
driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a").click()

# Click 'Add to cart'
driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button").click()

# Wait for view cart link and print it
heading = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div[2]/div[1]/div/div/div[2]/p[2]/a/u")))
print("🔍 Heading text is:", heading.text)
cart = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div/div[2]/div[1]/div/div/div[2]/p[2]/a/u")))
cart.click()
driver.find_element(By.XPATH,"/html/body/section/div/section/div[1]/div/div/a").click()
# Wait and click register/login
register = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/section/div[2]/div/div/div[2]/p[2]/a/u")))
register.click()

# Fill sign-up form
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("yasser")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("adasdasdqw@qgmail.com")
driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

# Fill account information
driver.find_element(By.ID, "id_gender1").click()
driver.find_element(By.ID, "password").send_keys("yasser")
driver.find_element(By.ID, "first_name").send_keys("yasser")
driver.find_element(By.ID, "last_name").send_keys("yasser")
driver.find_element(By.ID, "address1").send_keys("asdasd")
driver.find_element(By.ID, "state").send_keys("asdasd")
driver.find_element(By.ID, "city").send_keys("asdasd")
driver.find_element(By.ID, "zipcode").send_keys("123123")
driver.find_element(By.ID, "mobile_number").send_keys("123123")
driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

# Account created confirmation
heading2 = wait.until(EC.presence_of_element_located((By.XPATH, "//h2/b")))
print("🔍 Heading text is:", heading2.text)

# Click 'Continue'
driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()

# Wait for user name to appear
heading3 = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='nav navbar-nav']/li[10]/a")))
print("🔍 Heading text is:", heading3.text)

# Go to Cart again
driver.find_element(By.XPATH, "//a[contains(text(),'Cart')]").click()

# Proceed to checkout
driver.find_element(By.XPATH, "//a[contains(text(),'Proceed To Checkout')]").click()
heading4 = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@id='address_delivery']")))
print("🔍 Heading text is:", heading4.text)

# Enter comment and place order
driver.find_element(By.XPATH, "//textarea[@name='message']").send_keys("i like this order")
driver.find_element(By.XPATH, "//a[contains(text(),'Place Order')]").click()

# Fill payment details
driver.find_element(By.NAME, "name_on_card").send_keys("yasser")
driver.find_element(By.NAME, "card_number").send_keys("123132")
driver.find_element(By.NAME, "cvc").send_keys("123")
driver.find_element(By.NAME, "expiry_month").send_keys("12")
driver.find_element(By.NAME, "expiry_year").send_keys("1233")
driver.find_element(By.ID, "submit").click()

# Wait for confirmation and download invoice
try:
    invoice_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Download Invoice')]")))
    invoice_button.click()
except Exception as e:
    print("❌ Could not click invoice link:", e)

# Click 'Continue'
driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()

# Delete account
driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()

# Confirm deletion
heading5 = wait.until(EC.presence_of_element_located((By.XPATH, "//h2/b")))
print("🔍 Heading text is:", heading5.text)

# Final continue
driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()

# Close browser
driver.quit()
