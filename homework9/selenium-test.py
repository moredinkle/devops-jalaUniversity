from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = "https://github.com/"
driver.get(url)

#clicking signup button on github
button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/a")
button.click()

