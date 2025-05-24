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

wait = WebDriverWait(driver, 10)

# Click "Women" category
women_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#Women']")))
women_category.click()

# Click "Dress" under "Women"
dress_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Dress ']")))
dress_link.click()

# Verify heading by printing it
heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@class='title text-center']")))
print("🔍 Heading text is:", heading.text)

if "DRESS" in heading.text:
    print("✅ Successfully navigated to Women > Dress.")
else:
    print("❌ Unexpected heading. Check the XPath or timing.")

men_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#Men']")))
men_category.click()

# Click "Tshirts" under "Men"
tshirts_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Tshirts']")))
tshirts_link.click()

# Verify heading
heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@class='title text-center']")))
print("🔍 Heading text (Men):", heading.text)

if "TSHIRTS" in heading.text.upper():
    print("✅ Navigated to Men > Tshirts.")
else:
    print("❌ Unexpected heading under Men.")