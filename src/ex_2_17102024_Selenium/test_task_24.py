from selenium import webdriver
import allure
import pytest
import time

from selenium.webdriver.common.by import By


@allure.title("Verify Radio Button Checkbox")
def test_task_case():
    chromeService = webdriver.ChromeService(executable_path=r'chromedriver.exe')
    driver = webdriver.Chrome(service=chromeService)

    driver.get("https://awesomeqa.com/practice.html")

    time.sleep(5)
    make_app_element=driver.find_element(By.ID,"sex-1")
    make_app_element.click()

    time.sleep(5)

    make_app_element = driver.find_element(By.ID, "exp-2")
    make_app_element.click()

    time.sleep(5)

    make_app_element = driver.find_element(By.ID, "profession-1")
    make_app_element.click()

    time.sleep(10)
    driver.quit()