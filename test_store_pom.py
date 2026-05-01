import pytest
from pom import KodillaStorePom

@pytest.mark.parametrize("search_phrase, expected_amount", [
    ("NoteBook", 2),
    ("School", 1),
    ("Brand", 1),
    ("Business", 0),
    ("Gaming", 1),
    ("Powerful", 0),
])

def test_search_result_amount2(driver, search_phrase, expected_amount):
    url = "https://kodilla.com/pl/test/store"
    driver.get(url)
    store_page = KodillaStorePom(driver)

    results = store_page.search(search_phrase)

    assert len(results) == expected_amount, \
        f"Search for '{search_phrase}' expected {expected_amount} results, but found {len(results)}"

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

    assert len(page.search(search_phrase)) == amount

def assert_amount_compare(driver, search_phrase_1, search_phrase_2):

    phrase_type = type(search_phrase_1)
    if not phrase_type is str:
        raise TypeError(f"amount must be str type, is {phrase_type}")

    phrase_type = type(search_phrase_2)
    if not phrase_type is str:
        raise TypeError(f"amount must be str type, is {phrase_type}")
    
    page = KodillaStorePom(driver)

    assert len(page.search(search_phrase_1)) == len(page.search(search_phrase_2))

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

