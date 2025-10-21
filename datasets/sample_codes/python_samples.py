"""
Collection of Python code samples for testing and training
"""

# Good code examples
GOOD_CODE_1 = """
def calculate_average(numbers):
    \"\"\"Calculate the average of a list of numbers.\"\"\"
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
"""

GOOD_CODE_2 = """
class DataProcessor:
    \"\"\"Process data with proper error handling.\"\"\"
    
    def __init__(self, data_source):
        self.data_source = data_source
    
    def process_data(self):
        \"\"\"Process data from source.\"\"\"
        try:
            data = self.load_data()
            return self.clean_data(data)
        except Exception as e:
            print(f"Error processing data: {e}")
            return None
    
    def load_data(self):
        \"\"\"Load data from source.\"\"\"
        # Implementation here
        pass
"""

# Bad code examples (with issues)
BAD_CODE_1 = """
def calc(x,y):
    t=0
    for i in range(x):
        for j in range(y):
            t+=i*j
    return t
    # TODO: optimize this
"""

BAD_CODE_2 = """
def connect_db():
    password = "secret123"
    # Hardcoded password - security issue
    import sqlite3
    return sqlite3.connect('database.db')

def long_function():
    # This function is too long and complex
    result = 0
    for i in range(100):
        if i % 2 == 0:
            for j in range(50):
                if j % 3 == 0:
                    for k in range(25):
                        result += i * j * k
    return result
"""

SECURITY_VULNERABLE_CODE = """
import subprocess

def execute_user_input():
    user_input = input("Enter command: ")
    # Critical security vulnerability - command injection
    subprocess.call(user_input, shell=True)

def sql_query(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    # SQL injection vulnerability
    cursor.execute(query)
"""