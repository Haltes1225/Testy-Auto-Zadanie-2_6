import pytest
from pom import KodillaStorePom

@pytest.mark.parametrize("search_phrase, expected_amount", [
    ("NoteBook", 3),
    ("School", 1),
    ("Brand", 1),
    ("Business", 0),
    ("Gaming", 1),
    ("Powerful", 0),
])

def test_search_result_amount(driver, search_phrase, expected_amount):
    url = "https://kodilla.com/pl/test/store"
    driver.get(url)
    store_page = KodillaStorePom(driver)

    results = store_page.search(search_phrase)

    assert len(results) == expected_amount, \
        f"Search for '{search_phrase}' expected {expected_amount} results, but found {len(results)}"

@pytest.mark.parametrize("search_phrase_1, search_phrase_2", [
    ("Laptop", "laptopTTTT"),
    ("Laptop", "LAPTOP"),
    ("Laptop", "lApToP"),
    ("Laptop", "lAPTOP"),
    ("Laptop", "lapTOP"),
    ("Laptop", "laptoP"),
])

def test_search_result_case_sensitivity(driver,search_phrase_1,search_phrase_2):
    url = "https://kodilla.com/pl/test/store"
    driver.get(url)
    store_page = KodillaStorePom(driver)

    results1 = store_page.search(search_phrase_1)
    results2 = store_page.search(search_phrase_2)

    assert len(results1) == len(results2), \
        f"Search for '{search_phrase_1}' found different results than search for '{search_phrase_2}'"

