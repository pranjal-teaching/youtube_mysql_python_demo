from mysql.connector import connect

hostname = "localhost"
user_name = "root"
pwd = "password"


def execute_and_commit_query(query):
    # Step 1: Create connection object
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        # Step 2: Create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 4: Execute the statement
            mysql_cursor.execute(query)
            # Step 5: Commit Change
            mysql_connection_object.commit()


def add_job(job_class: str, charge_hour: float):
    add_job_insert_statement = f"""INSERT INTO company.job (job_class, chg_hour) 
                                   values ('{job_class}', {charge_hour});"""
    execute_and_commit_query(add_job_insert_statement)


def add_employee(emp_name, job_class):
    try:
        add_employee_insert_statement = f"""INSERT INTO company.employee (emp_name, job_class) value('{emp_name}', '{job_class}');"""
        execute_and_commit_query(add_employee_insert_statement)
    except Exception as e:
        return str(e)  # not ideal
    else:
        return 0


def add_project(project_name):
    add_project_insert_statement = f"""INSERT INTO company.project (project_name) value('{project_name}');"""
    execute_and_commit_query(add_project_insert_statement)


def assign_employee_to_project(employee_num: int, project_num: int, assignment_hours: float):
    assign_employee_to_project_statement = f"""INSERT INTO company.assignment (project_num, emp_num, assign_hours) 
                                                            value({project_num}, {employee_num}, {assignment_hours});"""
    # print(assign_employee_to_project_statement)
    execute_and_commit_query(assign_employee_to_project_statement)


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


def remove_employee(emp_num):
    # DELETE FROM company.assignment WHERE emp_num = 1;
    # DELETE FROM company.employee WHERE emp_num = 1;
    delete_employee_assignments_command = f"DELETE FROM company.assignment WHERE emp_num = {emp_num};"
    delete_employee_command = f"DELETE FROM company.employee WHERE emp_num = {emp_num};"
    execute_and_commit_query(delete_employee_assignments_command)
    execute_and_commit_query(delete_employee_command)


def remove_project(project_id):
    """
    Remove project by its ID
    DELETE FROM company.assignment WHERE project_num = 1;
    DELETE FROM company.project WHERE project_num = 1;
    :param project_id: indicates project to be deleted
    :return: None
    """
    del_assignments = f"DELETE FROM company.assignment WHERE project_num = {project_id};"
    del_project = f"DELETE FROM company.project WHERE project_num = {project_id};"
    execute_and_commit_query(del_assignments)
    execute_and_commit_query(del_project)


def remove_employee_from_project(employee_id, project_id):
    """DELETE FROM company.assignment WHERE project_num = 2 and emp_num = 3;"""
    remove_employee_from_project_query = f"DELETE FROM company.assignment WHERE project_num = {project_id} and emp_num = {employee_id};"
    execute_and_commit_query(remove_employee_from_project_query)


def update_project_name(current_name, new_name):
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 4: Execute the statement
            query = f'UPDATE company.project SET project_name = "{new_name}" WHERE project_name = "{current_name}";'
            mysql_cursor.execute(query)
            if mysql_cursor.rowcount == 0:
                raise ValueError(f"{current_name} does not exist")
            # Step 5: Commit Change
            mysql_connection_object.commit()



def testing():
    update_project_name("abc", "def")
    # add_job(job_class="J002", charge_hour=62.75)
    # add_employee(emp_name='Ron', job_class='J001')
    # add_project('funny_memes')
    # assign_employee_to_project(project_num=2, employee_num=3, assignment_hours=5)
    # print(get_employee_list_for_project('funny_memes'))
    # remove_employee(emp_num=4)
    # print(get_employee_list_for_project('funny_memes'))
    # remove_project(project_id=1)
    # remove_employee_from_project(project_id=2, employee_id=3)



if __name__ == '__main__':
    testing()
