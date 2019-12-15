import time
import math

# webdriver - набор команд для управления браузером
from selenium import webdriver

# инициализация драйвера браузера, после выполнения которой пользователь видит новую страницу браузера
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

# Метод get сообщает браузеру, что нужно открыть сайт по прописанной ссылке
driver.get("http://suninjuly.github.io/get_attribute.html")
time.sleep(1)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Считывание значений х и у элемента img с атрибутом valuex
x = driver.find_element_by_id("treasure").get_attribute("valuex")
y = calc(x)

# Поиск поля ввода текста
textinput = driver.find_element_by_id("answer")
# Запись текста для поиска в найденное поле
textinput.send_keys(y)

time.sleep(1)

# Проставление checkbox "I'm the robot"
chkIRobot = driver.find_elements_by_id("robotCheckbox")
chkIRobot[0].click()

time.sleep(1)

# Выбор значения radiobutton "Robots rule!".
rbnRobotsRule = driver.find_elements_by_id("robotsRule")
rbnRobotsRule[0].click()

time.sleep(1)

# Поиск кнопки submit
btnSubmit = driver.find_element_by_css_selector(".btn") 
btnSubmit.click()

time.sleep(5)

# Закрытия окна браузера
driver.quit()