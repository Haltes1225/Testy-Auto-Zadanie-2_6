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

def test_search(driver):

    url = "https://kodilla.com/pl/test/store"
    driver.get(url)
    
    page = KodillaStorePom(driver)

    page.search_bar.clear()
    page.search_bar.send_keys("Laptop")

    print("\n")
    for result in page.search_results:
        print(result.text)
        print("\n")

def test_search_result_amount(driver):
    url = "https://kodilla.com/pl/test/store"
    driver.get(url)

    assert_amount(driver, "NoteBook", 2)
    assert_amount(driver, "School", 1)
    assert_amount(driver, "Brand", 1)
    assert_amount(driver, "Business", 0)
    assert_amount(driver, "Gaming", 1)
    assert_amount(driver, "Powerful", 0)


