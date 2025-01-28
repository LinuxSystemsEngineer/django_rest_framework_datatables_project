# Django REST Framework Datatables Project

## Overview
This free and open source project showcases the integration of Django REST Framework with Datatables. This project provides both read-only datatables and full CRUD (create, read, update, and delete) operations with the django admin web interface.

## Requirements
- python3
- pip3

## Ubuntu packages

1. **Install the required ubuntu packages:**

    ```bash
    sudo apt update && sudo apt install python3 python3-dev python3-venv -y
    ```

## Installation

1. **Use git to clone the repository into your current working directory**

    ```bash
    git clone https://github.com/LinuxSystemsEngineer/django_rest_framework_datatables_project.git
    ```
2. **Change directories to the newly cloned github repository you just cloned:**

    ```bash
    cd django_rest_framework_datatables_project
    ```

3. **Create an isolated Python virtual environment:**

    ```bash
    python3 -m venv .venv
    ```

4. **Activate the newly created Python virtual environment:**

    ```bash
    . .venv/bin/activate
    ```

5. **Install required packages from the `requirements.txt` file:**

    ```bash
    pip3 install -r requirements.txt
    ```

6. **Make the database migrations:**

    ```bash
    python3 manage.py makemigrations
    ```

7. **Actually migrate the database and create the `db.sqlite3`:**

    ```bash
    python3 manage.py migrate
    ```

8. **Create a python django admin account and password:**

    ```bash
    python3 manage.py createsuperuser
    ```

9. **Create obfuscated data for the vlans database:**

    ```bash
    python3 ./create_db_vlans_vlans.py 
    ```

10. **Create obfuscated data for the coresubnets database:**

    ```bash
    python3 ./create_db_coresubnets.py
    ```

11. **Run the Django web framework app on port 8007:**

    ```bash
    python3 manage.py runserver 0.0.0.0:8007
    ```

12. **Access the django web app through your web browser:**

    ```bash
    with web browser, navigate to 127.0.0.1:8007
    ```

## Usage

- **Read-only Datatables:**

    Access the read-only datatables at [http://hostserveripaddress:8007](http://hostserveripaddress:8007).

- **CRUD Operations:**

    For CRUD operations, go to [http://hostserveripaddress:8007/admin](http://hostserveripaddress:8007/admin) and log in with the username and password you created.

## Features

- Multi-column sorting
- Pagination
- Search functionality
- Export options (Excel, CSV, PDF, Print)
- Record mangement
- Mobile responsive design

## Programmer
 **Blake Jones** built this project. For any questions or further information, please contact me on linkedin.

* https://www.linkedin.com/in/blake-jones-linux/

## Contributions
Feel free to fork this project and submit pull requests. For significant changes, please open an issue first to discuss what you would like to change.

## Sources / References
This project was built using code from:

* https://django-rest-framework-datatables.readthedocs.io/en/latest/tutorial.html.

* https://datatables.net/

* https://www.w3schools.com/

* https://mimesis.name/master/

## Screenshots

- **Login Page:**
![001_login_screen.png](./img/001_login_screen.png)

- **Landing Page:**
![002_landing_page.png](./img/002_landing_page.png)

- **VLANs Datatables Page:**
![003_vlans_datatables.png](./img/003_vlans_datatables.png)

- **Mange Records / CRUD (create, read, update, delete) Page:**
![004_crud_operations.png](./img/004_crud_operations.png)

