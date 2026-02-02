# Portfolio Guide: Course 7 - Module 1: Python Core Foundations

## 1. Introduction

This guide covers Module 1 of Course 7, "Automate Cybersecurity Tasks with Python," focusing on the core foundations of the Python 3 programming language. Python is the go-to language for automation in cybersecurity due to its simplicity, readability, and extensive libraries. Mastering these fundamentals is essential for writing scripts to automate security tasks.

**Module Objectives:**
*   Get to know Python 3 and why it’s the standard for automation in security.
*   Master data types: strings, integers, floats, and booleans.
*   Learn about data structures: lists, tuples, dictionaries, and sets.
*   Understand how to assign and reassign data to variables, following naming rules.
*   Use conditionals (`if`, `elif`, `else`) to make decisions in your code.
*   Use `for` loops to iterate through sequences and `while` loops to run as long as a condition is true.

## 2. Key Concepts & Syntax

### Why Python for Cybersecurity?
*   **Readability:** Python's clean syntax is easy to learn and read, making code easier to maintain and debug.
*   **Large Standard Library:** Comes with powerful modules for networking, file handling, regular expressions, and more.
*   **Extensive Third-Party Libraries:** A massive ecosystem of tools for security, data analysis, web development, etc. (e.g., `requests`, `pandas`, `scapy`).
*   **Cross-Platform:** Python scripts run on Windows, macOS, and Linux with minimal to no changes.
*   **"Glue Language":** Excellent for connecting different tools and systems together.

### Data Types
*   **Strings (`str`):** Textual data, enclosed in single `' '` or double `" "` quotes.
    *   `example = "Hello, World!"`
*   **Integers (`int`):** Whole numbers.
    *   `port = 443`
*   **Floats (`float`):** Numbers with decimal points.
    *   `version = 2.5`
*   **Booleans (`bool`):** Represents truth values, either `True` or `False`.
    *   `is_active = True`

### Data Structures
*   **Lists (`list`):** An ordered, changeable collection of items. Enclosed in `[ ]`.
    *   `allow_list_ips = ['192.168.1.1', '10.0.0.5']`
*   **Tuples (`tuple`):** An ordered, **unchangeable** collection of items. Enclosed in `( )`.
    *   `config = ('ssh', 22, 'enabled')`
*   **Dictionaries (`dict`):** An unordered collection of key-value pairs. Enclosed in `{ }`.
    *   `user_info = {'username': 'kali', 'user_id': 1000, 'shell': '/bin/zsh'}`
*   **Sets (`set`):** An unordered collection of **unique** items. Enclosed in `{ }`.
    *   `unique_ips = {'10.1.1.2', '10.1.1.3', '10.1.1.2'}` (will only store '10.1.1.2' once).

### Variables
*   A name that refers to a value.
*   **Assignment:** `variable_name = value`
*   **Naming Rules:** Must start with a letter or underscore `_`, can contain letters, numbers, and underscores. Cannot be a Python keyword (like `if`, `for`, `class`). By convention, variable names are `snake_case` (all lowercase with underscores).

### Conditionals
*   Used to execute code based on whether a condition is `True` or `False`.
    ```python
    if condition1:
        # code to run if condition1 is True
    elif condition2:
        # code to run if condition1 is False and condition2 is True
    else:
        # code to run if all previous conditions are False
    ```

### Loops
*   **`for` loops:** Iterate over a sequence (like a list, tuple, string, or dictionary).
    ```python
    my_list = ['a', 'b', 'c']
    for item in my_list:
        print(item)
    ```
*   **`while` loops:** Repeat as long as a condition is `True`.
    ```python
    count = 0
    while count < 5:
        print(count)
        count = count + 1 # Or count += 1
    ```

## 3. Practical Exercise: Your First Security Script

Let's write a simple Python script that mimics a basic security check: verifying if a user is on an allow list and if they are active.

**Objective:** Practice Python fundamentals by creating and running a simple script that uses variables, data structures, and conditionals.

**Setup:**

1.  **Navigate to your scripts directory and activate your virtual environment:**
    ```bash
    cd ~/gemini_projects/cyber_soc_trainee/scripts
    source ~/.venv/bin/activate
    ```
2.  **Create a new Python script file:**
    ```bash
    nano basic_security_check.py
    ```

3.  **Write the Python Code:**
    *   Inside the `nano` editor, type or paste the following Python code. Pay close attention to indentation (use 4 spaces).

    ```python
    # A simple script to practice Python fundamentals for security checks.

    # --- Data Structures ---
    # A list of usernames on an "allow list"
    allowed_users = ["admin_kali", "john_doe", "jane_smith"]

    # A dictionary mapping usernames to their active status
    user_status = {
        "admin_kali": True,
        "john_doe": True,
        "jane_smith": False,
        "guest_user": True
    }

    # --- Variables ---
    # The username we want to check
    login_attempt_user = "jane_smith"

    # --- Main Logic (Conditionals) ---
    print(f"Checking access for user: {login_attempt_user}")

    # Check if the user is in the allowed_users list
    if login_attempt_user in allowed_users:
        print(f"'{login_attempt_user}' is on the allow list. Checking status...")

        # Now, check if the user is active using the dictionary
        # The .get() method safely gets a value; if the user isn't in the dict, it returns None
        is_active = user_status.get(login_attempt_user)

        if is_active is True:
            print(f"Access GRANTED for '{login_attempt_user}'. User is active.")
        elif is_active is False:
            print(f"Access DENIED for '{login_attempt_user}'. User account is disabled.")
        else:
            print(f"Access DENIED for '{login_attempt_user}'. User status is unknown.")

    else:
        print(f"Access DENIED for '{login_attempt_user}'. User is not on the allow list.")


    # --- Looping Example ---
    # Print all users on the allow list
    print("\n--- Allowed Users ---")
    for user in allowed_users:
        print(user)
    ```

4.  **Save and Exit `nano`:**
    *   Press `Ctrl+X`.
    *   Press `Y` to confirm you want to save.
    *   Press `Enter` to confirm the filename.

**Tasks:**

1.  **Run the script:**
    *   From your terminal, run the script using the Python interpreter:
        ```bash
        python3 basic_security_check.py
        ```
    *   **Analyze the output:** Does the output match what you expect for the user "jane_smith"?

2.  **Modify and Re-run:**
    *   Open the script again with `nano basic_security_check.py`.
    *   Change the `login_attempt_user` variable to `"admin_kali"`.
    *   Save and run the script again. What is the output now?
    *   Change the `login_attempt_user` variable to `"guest_user"`.
    *   Save and run the script again. What is the output this time? Why?

3.  **Experiment (Optional):**
    *   Add a new user to the `allowed_users` list.
    *   Add a new user and their status to the `user_status` dictionary.
    *   Test your new user.

4.  **Deactivate the Virtual Environment:**
    *   When you are finished, type `deactivate`.

## 4. Reflection and Next Steps

*   **Self-Reflection:** How do data structures like lists and dictionaries help organize data? How do conditionals allow your script to make decisions? How could loops be used to check an entire list of login attempts?
*   **Next Module:** In the next module, we will explore **Writing Effective Code**, focusing on functions, modules, and code style.

---