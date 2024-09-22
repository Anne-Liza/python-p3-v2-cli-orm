from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name:")
    department = Department.find_by_name(name)
    print(department)if department else print(f'{name} Department not found')


def find_department_by_id():
    id_ = input("Enter the department's id:")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name:")
    location = input("Enter the department's location:")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department:", exc)


def update_department():
    def update_department():
        id_ = input("Enter the department's id: ")
        if department := Department.find_by_id(id_):
            try:
                name = input("Enter the department's new name: ")
                department.name = name
                location = input("Enter the department's new location: ")
                department.location = location

                department.update()
                print(f'Success: {department}')
            except Exception as exc:
                print("Error updating department: ", exc)
        else:
            print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id:")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_}deleted')
    else:
        print(print(f'Department {id_} not found'))
    


# You'll implement the employee functions in the lab

def list_employees():
    employees = employees.get_all()
    for employee in employees:
     print(employees)


def find_employee_by_name():
    name = input("Enter the employees' name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
     f'employees {name} not found')
    


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f'Employee {id_} not found')
    


def create_employee():
    name = input("Enter the department's name: ")
    job_title = input("Enter the job title: ")
    id = input("Enter the department's id: ")
    try:
        employee = Employee.create(name, job_title, id)
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    id_ = input("Enter the department's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employee's new name: ")
            employee.name = name
            id_ = input("Enter the employee's new id: ")
            employee.id = id_

            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {id_} not found')
    


def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')


def list_department_employees(department_id):
    employees = Employee.get_all()
    department_employees = [emp for emp in employees if emp.department_id == department_id]
    
    for emp in department_employees:
        print(emp)