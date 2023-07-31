import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)

    # Проверяем наличие кнопки добавления в корзину
    try:
        add_to_cart_button = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div["
                                                        "2]/form/button")))
        assert add_to_cart_button.is_displayed(), "Add to cart button is not displayed"
        print("Button appears on the website")
    except NoSuchElementException:
        assert False, "Add to cart button is not found on the page"

    time.sleep(3)