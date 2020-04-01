import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_add_button(browser):
    browser.get(link)
    add_button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(3)
    
    assert add_button, 'Add button is not found'