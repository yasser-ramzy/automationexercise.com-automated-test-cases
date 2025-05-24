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
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[4]/a").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div/form/input[2]").send_keys("asdadd@gmail.com")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div/form/input[3]").send_keys("yasser")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div/form/button").click()
driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a").click()
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[3]/a").click()
driver.find_element(By.XPATH,"/html/body/section/div/section/div[1]/div/div/a").click()
driver.find_element(By.XPATH,"/html/body/section/div/div[6]/textarea").send_keys("asgaqgqgaqgadgadg")
driver.find_element(By.XPATH,"/html/body/section/div/div[7]/a").click()
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[1]/div/input").send_keys("yasser")
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[2]/div/input").send_keys("asdasd")
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[1]/input").send_keys("123")
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[2]/input").send_keys("12")
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[3]/input").send_keys("1233")
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[5]/div/button").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/a").click()
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[5]/a").click()