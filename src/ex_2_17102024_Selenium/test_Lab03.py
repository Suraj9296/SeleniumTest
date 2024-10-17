from selenium import webdriver
import allure
import pytest
import time

from selenium.webdriver.common.by import By


@allure.title("Verify the Title/URL/Page Source of the webpage https://katalon-demo-cura.herokuapp.com/")
def test_task_case():
    chromeService = webdriver.ChromeService(executable_path=r'chromedriver.exe')
    driver = webdriver.Chrome(service=chromeService)

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_app_element=driver.find_element(By.ID,"btn-make-appointment")
    make_app_element.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    user_login = driver.find_element(By.ID,"txt-username")
    user_pwd = driver.find_element(By.ID, "txt-password")
    user_login.send_keys("suraj")
    user_pwd.send_keys("123")
    make_app_login = driver.find_element(By.ID, "btn-login")
    make_app_login.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"


    time.sleep(10)
    driver.quit()