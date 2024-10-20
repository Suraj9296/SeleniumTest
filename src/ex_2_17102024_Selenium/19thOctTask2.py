from selenium import webdriver
import allure
import pytest
import time

from selenium.webdriver.common.by import By


@allure.title("Verify Invalid credentials of  https://app.vwo.com/")
def test_task_case():
    chromeService = webdriver.ChromeService(executable_path=r'chromedriver.exe')
    driver = webdriver.Chrome(service=chromeService)

    driver.get("https://app.vwo.com/")
    user_login = driver.find_element(By.ID, "login-username")
    user_pwd = driver.find_element(By.ID, "login-password")
    user_login.send_keys("d@d.com")
    user_pwd.send_keys("123")

    time.sleep(10)
    assert driver.current_url == "https://app.vwo.com/#/login"
    content = driver.page_source
    #print(content)
    assert "Your email, password, IP address or location did not match" in content
    #https://app.vwo.com/#/login
