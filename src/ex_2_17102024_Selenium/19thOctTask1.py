from selenium import webdriver
import allure
import pytest
import time

from selenium.webdriver.common.by import By


@allure.title("Verify the Registration form of  https://awesomeqa.com/ui/index.php?route=account/register")
def test_task_case():
    chromeService = webdriver.ChromeService(executable_path=r'chromedriver.exe')
    driver = webdriver.Chrome(service=chromeService)

    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    first_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_name_input_tag.send_keys("sp1")
    last_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name_input_tag.send_keys("pr1")
    email_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='E-Mail']")
    email_name_input_tag.send_keys("pr1@pr.com")
    tel_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='Telephone']")
    tel_name_input_tag.send_keys("123456")
    pwd_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    pwd_name_input_tag.send_keys("@#1@Sprasad")
    pwdC_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='Password Confirm']")
    pwdC_name_input_tag.send_keys("@#1@Sprasad")
    radio_name_input_tag = driver.find_element(By.XPATH, "//input[@type='radio'][contains(following-sibling::text(),'No')]")
    radio_name_input_tag.click()
    check_name_input_tag = driver.find_element(By.XPATH, "// input[ @ name = 'agree']")
    check_name_input_tag.click()
    continue_name_input_tag = driver.find_element(By.XPATH, "// input[ @ value = 'Continue']")
    continue_name_input_tag.click()
    content = driver.page_source
    time.sleep(10)
    assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/success"
    content = driver.page_source
    assert "Your Account Has Been Created!" in content






