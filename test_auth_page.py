import pytest
from selenium import webdriver

from pages.auth_page import AuthPage
import time

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
   # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.close()


def test_auth_page(driver):
   page = AuthPage(driver)
   page.enter_email("mag1@mail.ru")
   page.enter_pass("30052023New")
   page.btn_click()

   #знак != или == будет зависеть от того, верные или неверные данные мы вводим
   assert page.get_relative_link() == '/all_pets', "login error"

   time.sleep(5) #задержка для учебных целей