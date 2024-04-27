import subprocess
import time
import pyautogui

# Open Command Prompt and run MySQL shell
subprocess.Popen('cmd /c mysql -u root -p', shell=True)
time.sleep(3)
pyautogui.write("root" + '\n', interval=0.1)
# Wait for the shell window to activate and root
time.sleep(5)

# Define SQL commands for table creation and CRUD operations
sql_commands = [
    "CREATE DATABASE IF NOT EXISTS test_db;",
    "USE test_db;",
    "CREATE TABLE IF NOT EXISTS authors (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));",
    "CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author_id INT, FOREIGN KEY (author_id) REFERENCES authors(id));",
    "INSERT INTO authors (name) VALUES ('George Orwell');",
    "INSERT INTO books (title, author_id) VALUES ('1984', 1);",
    "SELECT * FROM books;",
    "UPDATE authors SET name = 'George Orwell (Updated)' WHERE id = 1;",
    "SELECT * FROM books;",
    "DELETE FROM authors WHERE id = 1;",
    "SELECT * FROM books;"
]

# Perform each SQL command
for command in sql_commands:
    pyautogui.write(command + '\n', interval=0.05)  # Adjust the typing speed as needed
    pyautogui.press('enter')

    # Add a short delay to allow the operation to complete
    time.sleep(2)
