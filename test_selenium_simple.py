from selenium import webdriver
driver = webdriver.Chrome()
import time
def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """
    #Открываем страницу гугла
    selenium.get('https://google.com')
    time.sleep(5)
    # Ищем поле ввода, очищаем его и вводим туда текст
    search_input=selenium.find_element_by_name('q')
    search_input.clear()
    search_input.send_keys('first test')
    time.sleep(5)
    # Ищем кнопку и нажимаем на нее
    search_button=selenium.find_element_by_name('btnK')
    search_button.click()
    time.sleep(10)
    selenium.save_screenshot('result.png')




