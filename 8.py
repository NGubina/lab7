import time
import math

# webdriver - набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# иинициализация драйвера браузера, после выполнения которой пользователь видит новую страницу браузера
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

# Метод get сообщает браузеру, что нужно открыть сайт по прописанной ссылке
driver.get("http://suninjuly.github.io/explicit_wait2.html")

# проверка Selenium в течение 12 секунд до тех пор, пока стоимость не станет = $100
waitPrice = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"), "$100")
    )

# Поиск кнопки "Book"
btnBook = driver.find_elements_by_id("book")
btnBook[0].click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Считывание значения х
x = driver.find_element_by_id("input_value").text
y = calc(x)

# Поиск поля ввода ответа
textInputAnswer = driver.find_element_by_id("answer")
textInputAnswer.send_keys(y)

# Поиск кнопки submit
btnSubmit = driver.find_element_by_id("solve") 
btnSubmit.click()

time.sleep(5)

# Закрытия окна браузера
driver.quit()