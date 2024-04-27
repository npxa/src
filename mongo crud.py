import subprocess
import time
import pyautogui

# Open Command Prompt and run mongosh
subprocess.Popen('cmd /c mongosh', shell=True)

# Wait for the shell window to activate and mongosh to start
time.sleep(5)

# Define some example CRUD operations
crud_operations = [
    "use mydatabase",
    "db.createCollection('users')",
    "db.users.insertOne({ 'username': 'john_doe', 'email': 'john@example.com', 'age': 30 })",
    "db.users.insertMany([{ 'username': 'jane_doe', 'email': 'jane@example.com', 'age': 28 },{ 'username': 'alice_smith', 'email': 'alice@example.com', 'age': 35 },{ 'username': 'bob_johnson', 'age': 25 },{ 'username': 'emma_jones', 'email': 'emma@example.com', 'age': 40 }])",
    "db.users.find({ 'age': { $gt: 30 } })",
    "db.users.find({ 'age': { $ne: 30 } })",
    "db.users.find({ 'username': { $nin: ['john_doe', 'jane_doe'] } })",
    "db.users.find({ 'email': { $exists: true } })",
    "db.users.updateOne({ 'username': 'john_doe' },{ $set: { 'age': 31 } })",
    "db.users.updateMany({ 'age': { $lt: 30 } },{ $inc: { 'age': 1 } })",
    "db.users.deleteOne({ 'username': 'jane_doe' })",
    "db.users.drop()"
]

# Perform each CRUD operation
for operation in crud_operations:
    pyautogui.write(operation + '\n', interval=0.1)  # Adjust the typing speed as needed
    # Add a short delay to allow the operation to complete
    time.sleep(2)
