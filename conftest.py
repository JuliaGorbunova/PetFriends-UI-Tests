import pytest
import uuid

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    #с помощью этой функции можно узнать, что тест упал и сообщить эту информацию после теста
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
#
@pytest.fixture
def web_browser(request,selenium):
    browser=selenium
    #устанавливаем размеры окна браузера
    browser.set_window_size(1400,1000)
    #продолжаем выполнение функции даже тогда, когда тест закончится
    yield browser
    #этот код будет выполняться после каждого теста
    if request.node.rep_call.failed:
        try:
            #делаем попытку изменить цвет браузера на белый
            browser.execute_script("document.body.bgColor='white';")
            #сделать скриншот
            browser.save_screencshot('screenshots/'+str(uuid.uuid4())+'.png')
            #для удачного случая получим текущий адрес в браузере и логи
            print('URL:',browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass

import pytest
@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.add_argument('--kiosk')
    return chrome_options