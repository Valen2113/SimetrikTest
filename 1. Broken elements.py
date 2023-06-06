from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Configuración de Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://www.pixar.com/error404")

# Encontrar todos los enlaces en la página
links = driver.find_elements(By.TAG_NAME, "a")

# Verificación de cada enlace para determinar si está roto
for link in links:
    url = link.get_attribute("href")
    response = requests.head(url)
    if response.status_code >= 400:
        print(f"Enlace de PIXAR dañado: {url}")

# Cerrar Selenium WebDriver
driver.quit()