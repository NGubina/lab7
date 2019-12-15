import time
import math

# webdriver - набор команд для управления браузером
from selenium import webdriver

# инициализация драйвера браузера, после выполнения которой пользователь видит новую страницу браузера
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

# Метод get сообщает браузеру, что нужно открыть сайт по прописанной ссылке
driver.get("http://suninjuly.github.io/redirect_accept.html")
time.sleep(5)

# Поиск кнопки "I want to go on a magical journey!
btn = driver.find_elements_by_css_selector(".btn")
btn[0].click()

# Переход на вторую вкладку
driver.switch_to.window(driver.window_handles[1])

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Считывание значения х
x = driver.find_element_by_id("input_value").text
y = calc(x)

# Поиск поля ввода ответа
textInputAnswer = driver.find_element_by_id("answer")
textInputAnswer.send_keys(y)

# Поиск поля submit
btnSubmit = driver.find_element_by_css_selector(".btn") 
btnSubmit.click()

time.sleep(5)

# Закрытия окна браузера
driver.quit()