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
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[2]/a").click()
driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[1]/div/div[3]/div/ul/li[1]/a").click()
wait = WebDriverWait(driver, 10)
heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@class='title text-center']")))
print("🔍 Heading text is:", heading.text)
if "POLO" in heading.text:
    print("✅ Successfully navigated to POLO > SECTION.")
else:
    print("❌ Unexpected heading. Check the XPath or timing.")


driver.find_element(By.XPATH,"/html/body/section/div/div[2]/div[1]/div[1]/div[2]/div/ul/li[2]/a").click()
wait = WebDriverWait(driver,10)
heading2 = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/section/div/div[2]/div[2]/div/h2")))
print("🔍 Heading text is:", heading2.text)
if "H&M" in heading2.text:
    print("✅ Successfully navigated to H&M > SECTION.")
else:
    print("❌ Unexpected heading. Check the XPath or timing.")
