from logging.config import valid_ident
from tkinter import Button
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.action_chains import ActionChains

# Inicializar el navegador
inicio = webdriver.Firefox()
inicio.get("https://www.exito.com/")

# Esperar a que se cargue el elemento de publicidad y cerrarlo
time.sleep(25)
hidden_element = inicio.find_element(By.ID, "wps-overlay-close-button")
time.sleep(5)
hidden_element.click()
time.sleep(10)

# Seleccionar categoría
choose_category = inicio.find_element(By.ID, "Trazado_7822")
choose_category.click()
time.sleep(3)
select_category = inicio.find_element(By.ID, "undefined-nivel2-Dormitorio")
select_category.click()
time.sleep(5)
select_headboards = inicio.find_element(By.ID, "Categorías-nivel3-Cabeceros")
time.sleep(5)
select_headboards.click()
time.sleep(12)

# Desplazarse a la mitad de la página
scroll_height = inicio.execute_script("return document.body.scrollHeight")
inicio.execute_script("window.scrollTo(0, document.body.scrollHeight/2.7);") 
time.sleep(20)

# Realizar primera compra
first_buy = inicio.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[3]/div/div[9]/section/div[2]/div/div[3]/div/div[2]/div/div/div[5]/div/div/div/div[5]/section/a/article/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/span")
time.sleep(15)
# first_buy.click()  # Comentar o descomentar según se desee realizar la compra

# Realizar segunda compra
second_purchase = inicio.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[3]/div/div[9]/section/div[2]/div/div[3]/div/div[2]/div/div/div[5]/div/div/div/div[6]/section/a/article/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/span")
time.sleep(15)
second_purchase.click()
time.sleep(5)

# Continuar comprando
ventana = inicio.find_element(By.XPATH, "/html/body/div[17]/div[3]/div[2]/div/div/div[13]/div/div/div/div/div/div/div/div[2]/div[2]/button/div")
time.sleep(5)
ventana.click()
time.sleep(8)

# Generar compras adicionales
for _ in range(5):
   generate_purchase = inicio.find_element(By.CSS_SELECTOR, ".product-details-exito-vtex-components-buy-button-manager-more > svg:nth-child(1)")
   time.sleep(5)
   generate_purchase.click()

# Continuar comprando
continiue_shopping = inicio.find_element(By.XPATH, "/html/body/div[17]/div[3]/p")
continiue_shopping.click()
time.sleep(5)

# Realizar primera compra nuevamente
first_buy.click()
time.sleep(3)
Ventana_2 = inicio.find_element(By.CSS_SELECTOR, "div.border-box:nth-child(1)")
time.sleep(5)
Ventana_2.click()
time.sleep(4)

# Finalizar compra
end_of_purchase = inicio.find_element(By.XPATH, "/html/body/div[17]/div[3]/p")
time.sleep(4)
end_of_purchase.click()
time.sleep(5)

# Ingresar al carrito de compras
go_to_cart = inicio.find_element(By.CSS_SELECTOR, "svg.vtex-menu-2-x-header-link-icon:nth-child(2)")
time.sleep(5)
go_to_cart.click()
time.sleep(5)

# Ingresar email y continuar con el proceso de compra
email = inicio.find_element(By.NAME, "email")
time.sleep(5)
email.send_keys("amirchile@gmail.com")
time.sleep(5)
button_send = inicio.find_element(By.CSS_SELECTOR, ".exito-checkout-io-0-x-preLoginActiveButton")
time.sleep(10)
button_send.click()

# Realizar validaciones

# Cerrar el navegador
inicio.close()