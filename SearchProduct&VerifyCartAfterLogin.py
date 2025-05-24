from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get("https://automationexercise.com/")

# Click 'Products'
driver.find_element(By.XPATH, "//a[@href='/products']").click()

# Wait for product page heading
heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'All Products')]")))
print("🔍 Heading text is:", heading.text)

# Search for "Blue Top"
driver.find_element(By.ID, "search_product").send_keys("Blue Top")
driver.find_element(By.ID, "submit_search").click()

# Wait for search result
heading2 = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Blue Top')]")))
print("🔍 Search Result text is:", heading2.text)

# ✅ Add to Cart (hover + click)
add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-product-id='1']")))
add_to_cart_button.click()

# Wait for modal and click 'View Cart'
view_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']")))
view_cart.click()

# Wait for cart table to load
wait.until(EC.presence_of_element_located((By.ID, "cart_info_table")))

# Extra wait (optional safety net)
time.sleep(2)

# ✅ Check for product in cart (fixed XPath)
try:
    product_in_cart = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//table[@id='cart_info_table']//a[contains(text(),'Blue Top')]")
    ))
    print("✅ Product successfully added to Cart:", product_in_cart.text)
except:
    print("❌ Product NOT found in Cart.")

driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[4]/a").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div/form/input[2]").send_keys("yasserramzy6@gmail.com")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div/form/input[3]").send_keys("yasser")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div/form/button").click()
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[3]/a").click()
try:
    product_in_cart = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//table[@id='cart_info_table']//a[contains(text(),'Blue Top')]")
    ))
    print("✅ Product successfully added to Cart:", product_in_cart.text)
except:
    print("❌ Product NOT found in Cart.")
