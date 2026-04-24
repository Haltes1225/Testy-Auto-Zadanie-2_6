from pom import KodillaStorePom

def assert_amount(driver, search_phrase, amount):

    phrase_type = type(search_phrase)
    if not phrase_type is str:
        raise TypeError(f"amount must be str type, is {phrase_type}")

    amount_type = type(amount)
    if not amount_type is int:
        raise TypeError(f"amount must be int type, is {amount_type}")
    
    if not amount >= 0:
        raise ValueError("amount must be a non negative integer")
    
    page = KodillaStorePom(driver)

    page.search_bar.clear()
    page.search_bar.send_keys(search_phrase)

    assert len(page.search_results) == amount

def assert_amount_compare(driver, search_phrase_1, search_phrase_2):

    phrase_type = type(search_phrase_1)
    if not phrase_type is str:
        raise TypeError(f"amount must be str type, is {phrase_type}")

    phrase_type = type(search_phrase_2)
    if not phrase_type is str:
        raise TypeError(f"amount must be str type, is {phrase_type}")
    
    page = KodillaStorePom(driver)

    page.search_bar.clear()
    page.search_bar.send_keys(search_phrase_1)
    search_results_1 = page.search_results

    page.search_bar.clear()
    page.search_bar.send_keys(search_phrase_2)
    search_results_2 = page.search_results

    assert len(search_results_1) == len(search_results_2)

def test_search_result_amount(driver):
    url = "https://kodilla.com/pl/test/store"
    driver.get(url)

    assert_amount(driver, "NoteBook", 2)
    assert_amount(driver, "School", 1)
    assert_amount(driver, "Brand", 1)
    assert_amount(driver, "Business", 0)
    assert_amount(driver, "Gaming", 1)
    assert_amount(driver, "Powerful", 0)

def test_search_result_case_sensitivity(driver):
    url = "https://kodilla.com/pl/test/store"
    driver.get(url)

    assert_amount_compare(driver, "Laptop", "laptop")
    assert_amount_compare(driver, "Laptop", "LAPTOP")
    assert_amount_compare(driver, "Laptop", "lApToP")
    assert_amount_compare(driver, "Laptop", "lAPTOP")

