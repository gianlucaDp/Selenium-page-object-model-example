def test_add_then_remove(home):
    page = home.nav_to_add_remove_elements()
    page.add_element()
    page.add_element()
    page.add_element()
    num = page.count_elements()
    assert num == 3
    page.remove_element(2)
    num = page.count_elements()
    assert num == 2
