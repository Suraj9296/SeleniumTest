import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Actions P3")
@allure.description("Verify Click and Hold")
def test_verify_action_makemytrip():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    chromeService = webdriver.ChromeService(executable_path=r'chromedriver.exe')
    driver = webdriver.Chrome(chrome_options,chromeService)
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    source_element = driver.find_element(By.ID, "draggable")
    target_element = driver.find_element(By.ID, "droppable")
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()

    time.sleep(5)
    driver.quit()