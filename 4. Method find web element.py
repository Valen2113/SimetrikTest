from selenium import webdriver
from selenium.webdriver.common.by import By

def find_elements_within_element(element, locator):
    return element.find_elements(*locator)

driver = webdriver.Chrome()
driver.get("https://example.com")  # Reemplazar con tu URL

# Encontrar un elemento en la página principal
main_element = driver.find_element(By.ID, "main-element-id")

# Encontrar elementos dentro del elemento principal
sub_elements = find_elements_within_element(main_element, (By.TAG_NAME, "div"))

# Imprimir los elementos encontrados
for sub_element in sub_elements:
    print(sub_element.text)

# Cerrar Selenium WebDriver
driver.quit()
