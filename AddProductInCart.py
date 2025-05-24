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

# Click 'Products' menu
elem = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[2]/a")
elem.click()

wait = WebDriverWait(driver, 10)

# Add first product to cart
elem =driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a")
elem.click()
wait.until(EC.visibility_of_element_located((By.ID, "cartModal")))
elem = driver.find_element(By.XPATH, "//button[contains(text(),'Continue Shopping')]")
elem.click()
wait.until(EC.invisibility_of_element_located((By.ID, "cartModal")))

# Add second product to cart
elem =driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a")
elem.click()
wait.until(EC.visibility_of_element_located((By.ID, "cartModal")))
elem = driver.find_element(By.XPATH, "//button[contains(text(),'Continue Shopping')]")
elem.click()
wait.until(EC.invisibility_of_element_located((By.ID, "cartModal")))

# Go to Cart
elem = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[3]/a")
elem.click()

# Confirm both items are in cart
wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div[2]/table/tbody/tr[1]")))
print("First item appeared successfully!")

wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div[2]/table/tbody/tr[2]")))
print("Second item appeared successfully!")

wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div[2]/table/tbody/tr[1]/td[5]/p")))
print("First item price appeared successfully!")

wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div[2]/table/tbody/tr[2]/td[5]/p")))
print("Second item price appeared successfully!")
