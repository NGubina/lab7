import time
import math
import os 

# webdriver - набор команд для управления браузером
from selenium import webdriver

#инициализация драйвера браузера, после выполнения которой пользователь видит новую страницу браузера
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

#  Метод get сообщает браузеру, что нужно открыть сайт по прописанной ссылке
driver.get("http://suninjuly.github.io/file_input.html")

# Поиск и заполнение полей FirstName, LastName, Email
textInputFirstName = driver.find_elements_by_css_selector("[name='firstname']")
textInputFirstName[0].send_keys("Nataly")

textInputLastName = driver.find_elements_by_css_selector("[name='lastname']")
textInputLastName[0].send_keys("Gubina")

textInputEmail = driver.find_elements_by_css_selector("[name='email']")
textInputEmail[0].send_keys("ntly.dutov@mail.ru")

time.sleep(1)

# Поиск кнопки "Выберите файл"
btnLoadFile = driver.find_elements_by_css_selector("[type='file']") 
# Получение пути к директории текущего исполняемого файла 
currentDir = os.path.abspath(os.path.dirname(__file__))
# Добавление к найденному пути имени файла 
filePath = os.path.join(currentDir, '1.txt')

btnLoadFile[0].send_keys(filePath)

# Поиск кнопки submit
btnSubmit = driver.find_element_by_css_selector(".btn") 
btnSubmit.click()

time.sleep(5)

# Закрытия окна браузера
driver.quit()