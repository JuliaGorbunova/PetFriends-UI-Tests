from selenium import webdriver
driver = webdriver.Chrome()
import time
import pytest

# @pytest.fixture(autouse=True, scope="function")
def test_preparation(selenium):
    # заходим в свой аккаунт, проверяем что мы на странице, где все питомцы
    selenium.get('https://petfriends.skillfactory.ru/login')
    time.sleep(5)
    selenium.find_element_by_id('email').send_keys('svy-yuliana@yandex.ru')
    selenium.find_element_by_id('pass').send_keys('7Fevrala7')
    selenium.find_element_by_css_selector('button[type="submit"]').click()
    assert selenium.current_url == "https://petfriends.skillfactory.ru/all_pets"
    selenium.find_element_by_link_text('Мои питомцы').click()
    assert selenium.current_url == "https://petfriends.skillfactory.ru/my_pets"
    #получаем массив всех моих питомцев
    info_of_my_pets = selenium.find_elements_by_css_selector('div td')
    # формируем списки имен, типов и возрастов животных
    names = info_of_my_pets[::4]
    types = info_of_my_pets[1::4]
    ages = info_of_my_pets[2::4]
    #получаем кусок текста с логином, количеством питомцев, друзей и сообщений
    quantity_of_pets_full=selenium.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
    # получаем индекс символа буквы П слова "Питомцев"
    index_pets=quantity_of_pets_full.find('Питомцев')
    # получаем индекс символа буквы Д слова "Друзей"
    index_friends=quantity_of_pets_full.find('Друзей')
    # получаем срез строки от пробела после слова "Питомцев" до начала слова "Друзей"
    # (на всякий случай удаляем лишние пробелы, должно остаться только число)
    quantity_of_pets=quantity_of_pets_full[index_pets+10:index_friends].replace(' ','')
    # проверяем, соответствует ли количество питомцев по профилю реальному количеству имен питомцев
    assert int(quantity_of_pets)==len(names),"В таблице присутствуют не все питомцы"
    # получаем фото питомцев
    images = selenium.find_elements_by_css_selector('.table table-hover tbody tr th img')
    count=0
    # проходим циклом по массиву фотографий, считаем количество фото с атрибутом scr (значит фото есть)
    for i in range(len(images)):
        if (images[i].get_attribute('src')):
            count+=1
        if (len(images)//2)==0:
            assert count>=(len(images)/2), 'Фото присутствует менее чем у половины питомцев'
        else:
            assert count>=(len(images)/2+1), 'Фото присутствует менее чем у половины питомцев'
    # проверяем, что у всех питомцев есть имя
    assert '' not in names,'Не у всех питомцев есть имя'
    # проверяем, что у всех питомцев есть порода
    assert '' not in types,'Не у всех питомцев есть порода'
    # проверяем, что у всех питомцев есть возраст
    count_noage=0
    assert '' not in ages,'Не у всех питомцев есть возраст'
    # проверяем, что у всех питомцев разные имена
    assert len(names)==len(list(set(names))),'В списке есть питомцы с разным именем'
    # проверяем, что в списке нет повторяющихся питомцев, для этого сначала убедимся, что предыдущий тест не пройден и есть повтор имен
    if len(names)!=len(list(set(names))):
        # удаляем из списка элементы-крестики (удалить питомца)
        del info_of_my_pets[::4]
        # группируем каждые три элемента списка питомцев в кортеж (имя,порода,возраст)
        info_of_my_pets_tuple=[tuple(info_of_my_pets[i:i+3]) for i in range (0,len(info_of_my_pets),3)]
        # проверяем, есть ли в списке кортежей одинаковые элементы
        assert len(info_of_my_pets_tuple)==len(list(set(info_of_my_pets_tuple)))













