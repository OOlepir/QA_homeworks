import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_checkout_total_price():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Авторизація
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Додавання товарів у кошик
    items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item in items:
        item_xpath = f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"
        driver.find_element(By.XPATH, item_xpath).click()

    # Перехід у кошик
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Оформлення замовлення
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Отримання та перевірка підсумкової ціни
    total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text.split(": ")[1]
    assert total_price == "$58.29", f"Підсумкова сума невірна: {total_price}"

    # Закриття браузера
    driver.quit()


if __name__ == "__main__":
    test_checkout_total_price()
