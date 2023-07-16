from pages.main_page import MainPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'Tshirt'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() > 0

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        title = title.lower().split("\n")[1]
        assert 'shirt' in title, msg


def test_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(web_browser)

    # Try to enter "cvfhnajy" with English keyboard:
    page.search = 'cvfhnajy'
    page.search_run_button.click()

    # Verify that user can see empty list of products:
    assert page.products_titles.count() == 0
def test_check_sort_by_price(web_browser):
    """ Проверка сортировки продуктов
    """

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()

    # Прокрутка до элемента, чтобы он стал виден пользователю
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Получение цен всех выведенных продуктов
    all_prices = page.products_prices.get_text()

    # Конвертирование всех цен из строк в числа
    all_prices = [float(p.replace(' ', '')) for p in all_prices]

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"
    #
    # print(all_prices)
    #
    # print(sorted(all_prices))