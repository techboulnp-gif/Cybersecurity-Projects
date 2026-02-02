# Portfolio Guide: Course 7 - Module 2: Writing Effective Code

## 1. Introduction

This guide covers Module 2 of Course 7, "Automate Cybersecurity Tasks with Python," focusing on how to write code that is not only functional but also clean, reusable, and maintainable. These are critical skills for building larger, more complex automation scripts that can be relied upon in a professional environment.

**Module Objectives:**
*   Learn to use built-in functions like `print()`, `type()`, `len()`, `max()`, and `min()`.
*   Define your own functions with `def`, pass in parameters, and use `return` to get the output.
*   Understand the difference between global and local variable scope.
*   Import modules and libraries from the Python Standard Library (e.g., `os`, `csv`, `re`).
*   Follow the PEP 8 style guide for indentation and comments to write clean, professional code.

## 2. Key Concepts & Syntax

### Functions

Functions are reusable blocks of code that perform a specific action. They help organize code, reduce repetition, and improve readability.

*   **Built-in Functions:** Python comes with many functions ready to use.
    *   `print(value)`: Prints a value to the console.
    *   `type(variable)`: Returns the data type of a variable.
    *   `len(sequence)`: Returns the length (number of items) of a sequence like a list or string.
    *   `max(sequence)` / `min(sequence)`: Returns the largest/smallest item in a sequence.

*   **User-Defined Functions:** You can create your own functions using the `def` keyword.
    ```python
    def function_name(parameter1, parameter2):
        """
        This is a docstring. It explains what the function does.
        """
        # Code to be executed
        result = parameter1 + parameter2
        return result
    ```
    *   **`def`**: Keyword to start a function definition.
    *   **`function_name`**: Name of your function (follows same rules as variables).
    *   **`parameters`**: Variables that the function accepts as input.
    *   **`docstring`**: A triple-quoted string that documents your function's purpose.
    *   **`return`**: Keyword to send a value back from the function. If omitted, the function returns `None`.

### Variable Scope

Scope determines the visibility of a variable within a program.

*   **Local Scope:** A variable created inside a function is only accessible within that function.
*   **Global Scope:** A variable created in the main body of a Python file is global and can be accessed throughout the file, both inside and outside of functions.

    ```python
    global_var = "I am global"

    def my_function():
        local_var = "I am local"
        print(global_var) # Can access global_var
        print(local_var)

    my_function()
    # print(local_var) # This would cause an error because local_var is not accessible here
    ```

### Modules & Libraries

Modules are Python files containing functions, classes, and variables that you can import into your script to use. A library is a collection of modules.

*   **`import`**: The keyword used to bring a module into your script.
    ```python
    import os # Imports the entire 'os' module
    import csv, re # Imports multiple modules

    # To use a function from an imported module:
    current_directory = os.getcwd()

    # You can also import specific functions or give a module an alias:
    from datetime import datetime # Imports just the datetime class
    import statistics as stats # Imports the statistics module and renames it to 'stats'
    ```
*   **Python Standard Library:** A huge collection of modules included with every Python installation. Essential for security tasks:
    *   `os`: Interact with the operating system (e.g., file paths, directories).
    *   `csv`: Read from and write to CSV files.
    *   `re`: Regular expressions for pattern matching.
    *   `datetime`: Work with dates and times.

### Code Style (PEP 8)

PEP 8 is the official style guide for Python code. Following it makes your code more readable and consistent with the wider Python community.

*   **Indentation:** Use **4 spaces** per indentation level. Do not mix tabs and spaces.
*   **Line Length:** Limit all lines to a maximum of 79 characters.
*   **Comments:**
    *   Use inline comments sparingly.
    *   Use block comments (`# comment`) to explain complex sections of code.
    *   Write comments that explain the *why*, not the *what*.
*   **Whitespace:** Use whitespace to improve readability (e.g., around operators, after commas).

## 3. Practical Exercise: Refactoring Your Security Script

Let's take the script from Module 1 and refactor it into a more professional, function-based structure.

**Objective:** Apply the principles of functions, scope, and code style to improve an existing script.

**Setup:**

1.  **Navigate to your scripts directory and activate your virtual environment:**
    ```bash
    cd ~/gemini_projects/cyber_soc_trainee/scripts
    source ~/.venv/bin/activate
    ```
2.  **Create a new Python script file:**
    ```bash
    nano refactored_security_check.py
    ```

3.  **Write the Refactored Python Code:**
    *   Inside the `nano` editor, type or paste the following code. Note how the logic is now encapsulated within functions.

    ```python
    # refactored_security_check.py
    # This script refactors the basic security check into a more modular,
    # function-based format, following PEP 8 style guidelines.

    # --- Global Data (Constants) ---
    # Using uppercase for constants is a common convention
    ALLOWED_USERS = ["admin_kali", "john_doe", "jane_smith"]
    USER_STATUS = {
        "admin_kali": True,
        "john_doe": True,
        "jane_smith": False,
        "guest_user": True
    }


    def check_user_access(username):
        """
        Checks if a user is on the allow list and if their account is active.

        Args:
            username (str): The username to check.

        Returns:
            str: A message indicating whether access is granted or denied,
                 and the reason.
        """
        print(f"Checking access for user: {username}")

        if username not in ALLOWED_USERS:
            return f"Access DENIED for '{username}'. User is not on the allow list."

        print(f"'{username}' is on the allow list. Checking status...")

        is_active = USER_STATUS.get(username)

        if is_active is True:
            return f"Access GRANTED for '{username}'. User is active."
        elif is_active is False:
            return f"Access DENIED for '{username}'. User account is disabled."
        else:
            return f"Access DENIED for '{username}'. User status is unknown."


    def main():
        """
        Main function to run the primary logic of the script.
        """
        # --- List of users to check ---
        login_attempts = ["jane_smith", "admin_kali", "guest_user", "unknown_hacker"]

        print("--- Running Security Checks ---")
        for user in login_attempts:
            # Call our function for each user and print the returned message
            message = check_user_access(user)
            print(message)
            print("-" * 20) # Separator for readability


    # This is a standard Python convention. The code inside this 'if' block
    # will only run when the script is executed directly.
    if __name__ == "__main__":
        main()

    ```

4.  **Save and Exit `nano`**.

**Tasks:**

1.  **Run the new script:**
    *   From your terminal, run the script:
        ```bash
        python3 refactored_security_check.py
        ```
    *   **Analyze the output:** Notice how the `for` loop in the `main` function now calls your `check_user_access` function for each user in the `login_attempts` list. The output is cleaner and the logic is reusable.

2.  **Understand the Structure:**
    *   **Functions:** How does `check_user_access` make the code cleaner? What is the purpose of the `main` function?
    *   **Scope:** `ALLOWED_USERS` and `USER_STATUS` are global. `username` and `message` are local to their respective functions. Why is this a good structure?
    *   `if __name__ == "__main__":`: This is a very common and important construct in Python. It allows a script to be both executable on its own *and* importable as a module into other scripts without automatically running the `main()` function.

3.  **Experiment (Optional):**
    *   Create a new function called `list_allowed_users()` that prints all the users in the `ALLOWED_USERS` list.
    *   Call your new function from within the `main()` function.

4.  **Deactivate the Virtual Environment:**
    *   When you are finished, type `deactivate`.

## 4. Reflection and Next Steps

*   **Self-Reflection:** How does organizing code into functions make it easier to read and debug? Why is the `if __name__ == "__main__"` block a professional standard?
*   **Next Module:** In the next module, we will dive into **Working with Data & Regular Expressions**, learning how to manipulate strings and search for complex patterns in text.

---
