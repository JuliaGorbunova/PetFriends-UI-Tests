from selenium import webdriver
driver = webdriver.Chrome()
import time
import pytest

def test_petfriends(web_browser):
    #заходим на сайт петфрендс
    web_browser.get("https://petfriends.skillfactory.ru/")
    time.sleep(5)
    #находим кнопку "зарегистрироваться" и кликаем на нее
    btn_new_user=web_browser.find_element_by_xpath('/html/body/div/div/div[2]/button')
    btn_new_user.click()
    #ищем кнопку о том, что аккаунт уже есть
    btn_exist_acc=web_browser.find_element_by_link_text(u'У меня уже есть аккаунт')
    btn_exist_acc.click()
    #вводим емэйл и пароль
    field_email=web_browser.find_element_by_id('email')
    field_email.clear()
    field_email.send_keys('svy-yuliana@yandex.ru')
    field_password = web_browser.find_element_by_id('pass')
    field_password.clear()
    field_password.send_keys('7Fevrala7')
    # ищем кнопку входа и нажимаем на нее
    btn_submit=web_browser.find_element_by_xpath('/html/body/div/div/form/div[3]/button')
    btn_submit.click()

    time.sleep(10)
    assert web_browser.current_url=='https://petfriends.skillfactory.ru/all_pets','login error'

@pytest.fixture(autouse=True)
def testing():
    driver = webdriver.Chrome(r'C:\Users\Юлия\PycharmProjects\Selenium\chromedriver.exe')
    driver.get=('http://petfriends.skillfactory.ru/login')

    yield

    driver.quit()

def test_show_my_pet():
    driver.find_element_by_id('email').send_keys('svy-yuliana@yandex.ru')
    # Вводим пароль
    driver.find_element_by_id('pass').send_keys('7Fevrala7')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element_by_tag_name('h1').text == "PetFriends"

def test_show_my_pets(selenium):
    selenium.get('https://petfriends.skillfactory.ru/login')
    # Вводим email
    selenium.find_element_by_id('email').send_keys('svy-yuliana@yandex.ru')
    # Вводим пароль
    selenium.find_element_by_id('pass').send_keys('7Fevrala7')
    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert selenium.find_element_by_tag_name('h1').text == "PetFriends"
    # получаем списки изображений, имен и описаний питомцев
    images = driver.find_elements_by_css_selector('.card-deck.card-img-top')
    names = driver.find_elements_by_css_selector('.card-deck.card-title')
    descriptions = driver.find_elements_by_css_selector('.card-deck.card-text')
    # перебираем элементы списка имен: для каждого делаем цикл
    for i in range (len(names)):
        assert images[i].get_attribute('src')!='' #проверяем, что у первого элемента из списка картинок есть атрибут, т.е. она не пуста
        assert names[i].text!=''
        assert descriptions[i].text!=''
        parts=descriptions[i].text.split(',')
        assert len(parts[0])>0
        assert len(parts[1]) > 0








