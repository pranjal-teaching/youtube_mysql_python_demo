from mysql.connector import connect

hostname = "localhost"
user_name = "root"
pwd = "password"


def add_job(job_class: str, charge_hour: float):
    # Step 1: Create connection object
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        # Step 2: Create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Build sql statment
            add_job_insert_statement = f"""INSERT INTO company.job (job_class, chg_hour) values ('{job_class}', {charge_hour});"""
            # Step 4: Execute the statement
            mysql_cursor.execute(add_job_insert_statement)
            # Step 5: Commit Change
            mysql_connection_object.commit()


def add_employee(emp_name, job_class):
    # Step 1: Create connection object
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        # Step 2: Create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Build sql statment
            add_employee_insert_statement = f"""INSERT INTO company.employee (emp_name, job_class) value('{emp_name}', '{job_class}');"""
            # Step 4: Execute the statement
            mysql_cursor.execute(add_employee_insert_statement)
            # Step 5: Commit Change
            mysql_connection_object.commit()


def add_project(project_name):
    # Step 1: Create connection object
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        # Step 2: Create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Build sql statment
            add_project_insert_statement = f"""INSERT INTO company.project (project_name) value('{project_name}');"""
            # Step 4: Execute the statement
            mysql_cursor.execute(add_project_insert_statement)
            # Step 5: Commit Change
            mysql_connection_object.commit()


def assign_employee_to_project(employee_num: int, project_num: int, assignment_hours: float):
    # Step 1: Create connection object
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        # Step 2: Create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Build sql statment
            assign_employee_to_project_statement = f"""INSERT INTO company.assignment (project_num, emp_num, assign_hours) 
                                                        value({employee_num}, {project_num}, {assignment_hours});"""
            # Step 4: Execute the statement
            mysql_cursor.execute(assign_employee_to_project_statement)
            # Step 5: Commit Change
            mysql_connection_object.commit()


def get_employee_list_for_project(project_name):
    # Step 1: Create connection object
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        # Step 2: Create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Build sql statment
            get_employee_list_statement = f"""SELECT 
                                                            e.emp_name
                                                        FROM
                                                            company.assignment a
                                                                INNER JOIN
                                                            company.employee e ON a.emp_num = e.emp_num
                                                                INNER JOIN
                                                            company.project p ON a.project_num = p.project_num
                                                        WHERE
                                                            p.project_name = '{project_name}'"""
            # Step 4: Execute the statement
            mysql_cursor.execute(get_employee_list_statement)
            # Step 5: Retrieve Data
            employee_names = []
            for employee in mysql_cursor:
                employee_names.append(employee[0])
    return employee_names


def testing():
    # add_job(job_class="J002", charge_hour=62.75)
    # add_employee(emp_name='Ron', job_class='J001')
    # add_project('funny_memes')
    # assign_employee_to_project(1, 1, 2)
    print(get_employee_list_for_project('funny_memes'))
    pass


if __name__ == '__main__':
    testing()
