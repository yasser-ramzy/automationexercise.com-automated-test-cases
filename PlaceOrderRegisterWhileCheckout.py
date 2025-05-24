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
driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a").click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/p[2]/a")))
element.click()
driver.find_element(By.XPATH,"/html/body/section/div/section/div[1]/div/div/a").click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/section/div[2]/div/div/div[2]/p[2]/a/u")))
element.click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[2]").send_keys("yasserrr")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[3]").send_keys("yasserrsr12222@gmail.com")
driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/button").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/div[4]/input").send_keys("yasser")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[1]/input").send_keys("yasser")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[2]/input").send_keys("ramzy")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[5]/input").send_keys("asdasd")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[4]/input").send_keys("asdawqtadga")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[7]/input").send_keys("asdasdasd")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[8]/input").send_keys("alexandria")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[9]/input").send_keys("00000")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[10]/input").send_keys("2351341")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/button").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/a").click()
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[3]/a").click()
driver.find_element(By.XPATH,"/html/body/section/div/section/div[1]/div/div/a").click()
driver.find_element(By.XPATH,"/html/body/section/div/div[6]/textarea").send_keys("this is my new order place it")
driver.find_element(By.XPATH,"/html/body/section/div/div[7]/a").click()
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[1]/div/input").send_keys("34143")
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[2]/div/input").send_keys("4134134")
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[1]/input").send_keys("3414")
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[2]/input").send_keys("12")
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[3]/input").send_keys("41241")
driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[5]/div/button").click()

driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[5]/a").click()