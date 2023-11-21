import requests

# Endpoint para obtener todos los empleados
url_get_employees = "http://dummy.restapiexample.com/api/v1/employees"

# Endpoint para obtener un empleado específico
url_get_employee = "http://dummy.restapiexample.com/api/v1/employee/{id}"

# Endpoint para crear un nuevo empleado
url_create_employee = "http://dummy.restapiexample.com/api/v1/create"

# Endpoint para actualizar un empleado existente
url_update_employee = "http://dummy.restapiexample.com/api/v1/update/{id}"

# Endpoint para eliminar un empleado existente
url_delete_employee = "http://dummy.restapiexample.com/api/v1/delete/{id}"

# Método GET para obtener todos los empleados
response = requests.get(url_get_employees)
print(response.json(response))

# Método GET para obtener un empleado específico
employee_id = 1
response = requests.get(url_get_employee.format(id=employee_id))
print(response.json(response))

# Método POST para crear un nuevo empleado
new_employee = {
    "name": "John Doe",
    "salary": "5000",
    "age": "30"
}
response = requests.post(url_create_employee, json=new_employee)
print(response.json(response))

# Método PUT para actualizar un empleado existente
employee_id = 1
updated_employee = {
    "name": "Jane Doe",
    "salary": "6000",
    "age": "35"
}
response = requests.put(url_update_employee.format(id=employee_id), json=updated_employee)
print(response.json())

# Método DELETE para eliminar un empleado existente
employee_id = 1
response = requests.delete(url_delete_employee.format(id=employee_id))
print(response.json(response))
