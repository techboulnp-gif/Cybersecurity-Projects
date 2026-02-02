# Portfolio Guide: Course 7 - Module 4: Python in Practice

## 1. Introduction

This guide covers the final module of Course 7, "Automate Cybersecurity Tasks with Python," focusing on putting all your Python skills into practice. This involves reading from files, building complete automation scripts, and learning how to troubleshoot when things go wrong. These skills bridge the gap between knowing Python syntax and building functional tools for real-world security tasks.

**Module Objectives:**
*   Learn to `open()`, read, and parse files to extract data.
*   Build scripts that automate repetitive tasks like checking an allow list from a file.
*   Understand basic debugging techniques to troubleshoot your code.

## 2. Key Concepts & Syntax

### File Handling

Reading from and writing to files is a fundamental part of almost every automation script.

*   **Opening Files:** The `with open(...)` syntax is the recommended way to handle files. It ensures the file is automatically closed even if errors occur.
    ```python
    with open('filename.txt', 'r') as file_object:
        # Perform operations on the file here
        content = file_object.read()
    # The file is automatically closed when the 'with' block is exited.
    ```
*   **File Modes:**
    *   `'r'`: **Read** (default). Opens a file for reading. Throws an error if the file does not exist.
    *   `'w'`: **Write**. Opens a file for writing. **Creates the file if it does not exist; overwrites the entire file if it does exist.**
    *   `'a'`: **Append**. Opens a file for appending. **Creates the file if it does not exist; adds new content to the end of the file.**
*   **Reading from Files:**
    *   `file.read()`: Reads the entire content of the file into a single string.
    *   `file.readline()`: Reads a single line from the file.
    *   `file.readlines()`: Reads the entire content of the file into a list of strings, where each string is a line.
    *   **Iterating over a file (most common and memory-efficient):**
        ```python
        with open('filename.txt', 'r') as f:
            for line in f:
                # .strip() is often used to remove the trailing newline character
                print(line.strip())
        ```

### Structuring an Automation Algorithm

A typical automation script follows a simple, effective structure:

1.  **Imports:** Import all necessary modules at the top of the file (e.g., `import os`, `import re`).
2.  **Constants/Global Variables:** Define any global data, like file paths or fixed lists.
3.  **Function Definitions:** Encapsulate your logic into reusable functions. Have one primary function that controls the script's flow (often called `main()`).
4.  **Execution Block:** Use the `if __name__ == "__main__":` block to call your `main()` function.

This structure makes your scripts readable, maintainable, and reusable.

### Debugging

Debugging is the process of finding and fixing errors in your code.

*   **Read the Error Message (Traceback):** Python's error messages are very informative. Read them carefully from bottom to top.
    *   The **last line** tells you the type of error (e.g., `NameError`, `SyntaxError`, `FileNotFoundError`).
    *   The lines above show the "traceback"—the sequence of function calls that led to the error, including the file name and line number where the error occurred.
*   **Use `print()` Statements:** The simplest form of debugging. Strategically place `print()` statements in your code to check the values of variables at different points and understand the flow of execution.
    ```python
    print(f"DEBUG: The value of 'username' is: {username}")
    ```
*   **Isolate the Problem:** Comment out parts of your code to determine which section is causing the error.
*   **Check Your Assumptions:** Are your variables the data type you think they are? Is the file you're trying to open in the correct location?

## 3. Practical Exercise: Building an Allow List Checker

Let's build a practical script that reads a list of allowed usernames from one file and checks them against a list of login attempts from another file.

**Objective:** Combine file handling, data structures, and functions to build a complete, practical automation script.

**Setup:**

1.  **Navigate to your scripts directory and activate your virtual environment:**
    ```bash
    cd ~/gemini_projects/cyber_soc_trainee/scripts
    source ~/.venv/bin/activate
    ```
2.  **Create the necessary data files:**
    *   **Allowed Users File:**
        ```bash
        nano allowed_users.txt
        ```
        Inside `nano`, add these usernames, each on a new line:
        ```
        admin_kali
        john_doe
        jane_smith
        bob_analyst
        ```
        Save and exit.
    *   **Login Attempts File:**
        ```bash
        nano login_attempts.log
        ```
        Inside `nano`, add these usernames, each on a new line:
        ```
        jane_smith
        guest_user
        admin_kali
        unknown_hacker
        john_doe
        ```
        Save and exit.

3.  **Create your Python script:**
    ```bash
    nano allow_list_checker.py
    ```

4.  **Write the Python Code:**
    *   Inside `nano`, type or paste the following code.

    ```python
    # allow_list_checker.py
    # This script reads an allow list from a file and checks it against
    # a log of login attempts, flagging any unauthorized users.

    # --- Constants ---
    ALLOW_LIST_FILE = "allowed_users.txt"
    LOGIN_LOG_FILE = "login_attempts.log"

    def get_allowed_users(filepath):
        """
        Reads a file containing one username per line and returns a set of users.
        Using a set provides fast lookups.
        """
        allowed_users_set = set()
        try:
            with open(filepath, 'r') as f:
                for user in f:
                    # .strip() removes leading/trailing whitespace, including newlines
                    allowed_users_set.add(user.strip())
            return allowed_users_set
        except FileNotFoundError:
            print(f"Error: Allow list file not found at '{filepath}'.")
            # Return an empty set so the script doesn't crash
            return set()

    def check_login_attempts(log_filepath, allowed_users):
        """
        Reads a log of login attempts and checks each user against the
        allow list set.
        """
        print("\n--- Starting Login Attempt Check ---")
        unauthorized_attempts = []
        try:
            with open(log_filepath, 'r') as f:
                for user_attempt in f:
                    user = user_attempt.strip()
                    if user not in allowed_users:
                        print(f"ALERT: Unauthorized login attempt by '{user}'!")
                        unauthorized_attempts.append(user)
                    else:
                        print(f"Login by '{user}' is authorized.")
            return unauthorized_attempts
        except FileNotFoundError:
            print(f"Error: Login log file not found at '{log_filepath}'.")
            return []


    def main():
        """
        Main function to orchestrate the allow list check.
        """
        print("--- Security Automation: Allow List Checker ---")

        # 1. Get the set of allowed users from the file
        allowed_users = get_allowed_users(ALLOW_LIST_FILE)

        # 2. Check login attempts against the allowed users
        if allowed_users: # Only run if the allow list was successfully loaded
            unauthorized = check_login_attempts(LOGIN_LOG_FILE, allowed_users)

            # 3. Report summary
            print("\n--- Summary ---")
            if unauthorized:
                print("Unauthorized login attempts were detected for the following users:")
                for user in unauthorized:
                    print(f"- {user}")
            else:
                print("No unauthorized login attempts were detected.")
        else:
            print("Could not perform security check due to missing allow list.")


    if __name__ == "__main__":
        main()

    ```

5.  **Save and Exit `nano`**.

**Tasks:**

1.  **Run the script:**
    *   From your terminal, run the script:
        ```bash
        python3 allow_list_checker.py
        ```
    *   **Analyze the output:** Does the script correctly identify "guest_user" and "unknown_hacker" as unauthorized?

2.  **Practice Debugging:**
    *   Rename `allowed_users.txt` to something else, for example: `mv allowed_users.txt old_users.txt`.
    *   Run the script again: `python3 allow_list_checker.py`.
    *   What is the output now? Notice how the `try...except FileNotFoundError` block prevents the program from crashing and gives you a helpful error message.
    *   Rename the file back: `mv old_users.txt allowed_users.txt`.

3.  **Experiment (Optional):**
    *   Add a new function to write the list of `unauthorized` users to a new file called `unauthorized_logins.txt`.
    *   Call this new function from `main()`.

4.  **Deactivate the Virtual Environment:**
    *   When you are finished, type `deactivate`.

## 4. Reflection and Next Steps

*   **Self-Reflection:** How does reading from files make your scripts more flexible than hard-coding data? How do `try...except` blocks make your code more robust?
*   **Course Completion:** Congratulations! You have completed the guided learning portion for Python in this curriculum. You now have the foundational skills to start building more complex projects.
*   **Next Phase:** We will now move on to **Phase 3: Advanced Practice & Capstone Project**, where you will apply all your Linux, SQL, and Python skills to more challenging, real-world scenarios.

---
