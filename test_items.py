import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Проверяем наличие кнопки добавления в корзину
    try:
        add_to_cart_button = browser.find_element(By.CLASS_NAME,"btn.btn-lg.btn-primary.btn-add-to-basket")
        assert add_to_cart_button.is_displayed(), "Add to cart button is not displayed"
    except NoSuchElementException:
        assert False, "Add to cart button is not found on the page"

    time.sleep(3)