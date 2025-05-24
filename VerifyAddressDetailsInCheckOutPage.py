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
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[4]/a").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[2]").send_keys("yasser")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[3]").send_keys("yassexrasrsraaamzy@gmail.com")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/button").click()
wait2 = WebDriverWait(driver,5)
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/div[4]/input").send_keys("123123")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[1]/input").send_keys("yasser")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[2]/input").send_keys("yasser")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[4]/input").send_keys("asdasdasd")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[7]/input").send_keys("alex")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[8]/input").send_keys("alex")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[9]/input").send_keys("123123")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[10]/input").send_keys("12323123")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/button").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/a").click()
heading = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a")))
print("🔍 Heading text is:", heading.text)
driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a").click()
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[3]/a").click()
heading2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div[1]/ol/li[2]")))
print("🔍 Heading text is:", heading2.text)
driver.find_element(By.XPATH,"/html/body/section/div/section/div[1]/div/div/a").click()
heading3 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div[3]/div/div[1]/ul/li[4]")))
print("🔍 Heading text is:", heading3.text)
if heading3 == "asdasdasd":
    print("ADDRESS MATCH CORRECTLY")
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[5]/a").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/a").click()
driver.quit()