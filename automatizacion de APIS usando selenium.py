from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar el driver de Selenium
driver = webdriver.Firefox()

# Definir la base URL de la API
base_url = "http://dummy.restapiexample.com/api/v1"

# Escenario para probar el método GET
def test_get_employee():
    # Navegar a la página de la API
    driver.get(f"{base_url}/employee/1")

  #  Verificar que la respuesta sea 200 OK
    assert driver.find_element(By.CSS_SELECTOR, "#json-tab").text == "200"

    # Verificar que los datos del empleado sean correctos
    assert driver.find_element(By.CSS_SELECTOR, "#\/data\/employee_name > td:nth-child(1) > span:nth-child(2)").text == "Jone Doe"
    assert driver.find_element(By.CSS_SELECTOR, "#\/data\/employee_age > td:nth-child(1) > span:nth-child(2)").text == "54"
    assert driver.find_element(By.CSS_SELECTOR, "#\/data\/employee_salary > td:nth-child(1) > span:nth-child(2)").text == "50000"

# Escenario para probar el método POST
def test_create_employee():
    # Navegar a la página de la API
    driver.get(f"{base_url}/create")

    # Ingresar los datos del nuevo empleado
    driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Jane Doe")
    driver.find_element(By.CSS_SELECTOR, "input[name='salary']").send_keys("60000")
    driver.find_element(By.CSS_SELECTOR, "input[name='age']").send_keys("25")

    # Enviar el formulario de creación de empleado
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Verificar que la respuesta sea 200 OK
    assert driver.find_element(By.CSS_SELECTOR, "span#status").text == "200"

    # Verificar que el empleado se haya creado correctamente
    assert driver.find_element(By.CSS_SELECTOR, "span#employee_name").text == "Jane Doe"
    assert driver.find_element(By.CSS_SELECTOR, "span#employee_age").text == "25"
    assert driver.find_element(By.CSS_SELECTOR, "span#employee_salary").text == "60000"

# Escenario para probar el método PUT
def test_update_employee():
    # Navegar a la página de la API
    driver.get(f"{base_url}/update/1")

    # Modificar los datos del empleado
    driver.find_element(By.CSS_SELECTOR, "input[name='name']").clear()
    driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("John Smith")
    driver.find_element(By.CSS_SELECTOR, "input[name='salary']").clear()
    driver.find_element(By.CSS_SELECTOR, "input[name='salary']").send_keys("55000")
    driver.find_element(By.CSS_SELECTOR, "input[name='age']").clear()
    driver.find_element(By.CSS_SELECTOR, "input[name='age']").send_keys("35")

    # Enviar el formulario de actualización de empleado
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Verificar que la respuesta sea 200 OK
    assert driver.find_element(By.CSS_SELECTOR, "span#status").text == "200"

    # Verificar que los datos del empleado se hayan actualizado correctamente
    assert driver.find_element(By.CSS_SELECTOR, "span#employee_name").text == "John Smith"
    assert driver.find_element(By.CSS_SELECTOR, "span#employee_age").text == "35"
    assert driver.find_element(By.CSS_SELECTOR, "span#employee_salary").text == "55000"

# Escenario para probar el método DELETE
def test_delete_employee():
    # Navegar a la página de la API
    driver.get(f"{base_url}/delete/1")

    # Verificar que la respuesta sea 200 OK
    assert driver.find_element(By.CSS_SELECTOR, "span#status").text == "200"

    # Verificar que el empleado haya sido eliminado
    assert driver.find_element(By.CSS_SELECTOR, "span#message").text == "Successfully! Record has been deleted"

# Ejecutar los escenarios de prueba
test_get_employee()
test_create_employee()
test_update_employee()
test_delete_employee()

# Cerrar el driver de Selenium
driver.quit()