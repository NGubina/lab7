import time

# webdriver - набор команд для управления браузером
from selenium import webdriver

from selenium.webdriver.support.ui import Select

# инициализация драйвера браузера, после выполнения которой пользователь видит новую страницу браузера
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

# Метод get сообщает браузеру, что нужно открыть сайт по прописанной ссылке
driver.get("http://suninjuly.github.io/selects1.html")
time.sleep(1)

def sum(x1,x2):
  return str(int(x1)+int(x2))

# Считывание значений num1 и num2 и подсчитываем их сумму
num1 = driver.find_elements_by_id("num1")[0].text
num2 = driver.find_elements_by_id("num2")[0].text
y=sum(num1, num2)

# Выбор результата суммы из выпадающего списка 
select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value(y)

time.sleep(1)

# Поиск кнопки submit
btnSubmit = driver.find_element_by_css_selector(".btn") 
btnSubmit.click()

time.sleep(5)

#  Закрытия окна браузера
driver.quit()