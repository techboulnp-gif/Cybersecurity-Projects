# Portfolio Guide: Course 7 - Module 3: Working with Data & Regular Expressions

## 1. Introduction

This guide covers Module 3 of Course 7, "Automate Cybersecurity Tasks with Python," focusing on manipulating data and using regular expressions (RegEx). These skills are fundamental for any security automation task, as they allow you to parse, search, and extract specific information from unstructured text like log files, configuration files, and command outputs.

**Module Objectives:**
*   Use indices, bracket notation, and slicing to manipulate strings.
*   Use common methods like `.upper()`, `.lower()`, and `.split()` on strings.
*   Use methods like `.insert()`, `.remove()`, and `.append()` to manage lists.
*   Use the `re` module to search for complex patterns (like IP addresses or email formats) in text.

## 2. Key Concepts & Syntax

### String Manipulation

Strings are sequences of characters, and you can access and manipulate them in various ways.

*   **Indexing:** Access a single character using its index in square brackets `[]`. Indexing starts at 0.
    *   `my_string = "Hello"`
    *   `print(my_string[0])`  # Output: 'H'
    *   `print(my_string[-1])` # Output: 'o' (negative indexing starts from the end)
*   **Slicing:** Extract a substring using a range `[start:stop:step]`.
    *   `my_string = "192.168.1.10"`
    *   `print(my_string[0:3])` # Output: '192' (from index 0 up to, but not including, index 3)
    *   `print(my_string[4:])`  # Output: '168.1.10' (from index 4 to the end)
    *   `print(my_string[:7])`  # Output: '192.168' (from the beginning up to index 7)
*   **Common String Methods:**
    *   `.upper()` / `.lower()`: Convert the string to uppercase or lowercase.
    *   `.strip()`: Remove whitespace from the beginning and end.
    *   `.startswith(substring)` / `.endswith(substring)`: Check if a string starts or ends with a specific substring.
    *   `.split(delimiter)`: Split a string into a list of substrings based on a delimiter.
        *   `log_entry = "INFO:User logged in"`
        *   `parts = log_entry.split(':')` # Result: ['INFO', 'User logged in']
    *   `.join(list)`: Joins the elements of a list into a single string.
        *   `my_list = ['a', 'b', 'c']`
        *   `result = '-'.join(my_list)` # Result: 'a-b-c'

### List Manipulation

Lists are ordered, mutable collections.

*   **Accessing/Modifying:** Use index `[]` to access or change an item.
    *   `my_list = [10, 20, 30]`
    *   `my_list[1] = 25` # my_list is now [10, 25, 30]
*   **Common List Methods:**
    *   `.append(item)`: Adds an item to the end of the list.
    *   `.insert(index, item)`: Inserts an item at a specific index.
    *   `.remove(item)`: Removes the first occurrence of an item.
    *   `.pop(index)`: Removes and returns the item at a specific index (or the last item if index is omitted).

### Regular Expressions (RegEx)

RegEx is a powerful mini-language for finding and extracting patterns in text. In Python, we use the `re` module.

*   **Importing:** `import re`
*   **Common `re` Functions:**
    *   `re.search(pattern, string)`: Scans through a string, looking for the *first* location where the pattern produces a match. Returns a match object if found, otherwise `None`.
    *   `re.findall(pattern, string)`: Finds *all* non-overlapping matches of the pattern in a string and returns them as a list of strings.
*   **Basic RegEx Patterns:**
    *   `.`: Matches any character except a newline.
    *   `*`: Matches the preceding character 0 or more times.
    *   `+`: Matches the preceding character 1 or more times.
    *   `?`: Matches the preceding character 0 or 1 time.
    *   `\d`: Matches any digit (0-9).
    *   `\w`: Matches any alphanumeric character (letters, numbers, and `_`).
    *   `\s`: Matches any whitespace character.
    *   `[...]`: Matches any character within the brackets (e.g., `[abc]`).
    *   `^`: Matches the start of the string.
    *   `$`: Matches the end of the string.

*   **Example: Finding an IP Address**
    *   An IP address is four groups of 1-3 digits, separated by dots.
    *   A simplified pattern: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`
    *   `{1,3}` means "match the preceding character (a digit `\d`) between 1 and 3 times".
    *   `\.`: means "match a literal dot `.`" (we have to "escape" the dot because `.` is a special character in RegEx).

## 3. Practical Exercise: Parsing Log Entries

Let's write a script to parse log entries to extract useful information like timestamps, log levels, and IP addresses.

**Objective:** Use string methods and regular expressions to parse structured and unstructured text.

**Setup:**

1.  **Navigate to your scripts directory and activate your virtual environment:**
    ```bash
    cd ~/gemini_projects/cyber_soc_trainee/scripts
    source ~/.venv/bin/activate
    ```
2.  **Create a new Python script file:**
    ```bash
    nano log_parser.py
    ```

3.  **Write the Python Code:**
    *   Inside `nano`, type or paste the following code.

    ```python
    # log_parser.py
    # A script to practice string manipulation and regular expressions
    # for parsing security log entries.

    import re

    def parse_log_entry_simple(log_entry):
        """
        Parses a log entry using the .split() method.
        Assumes a consistent format like "LEVEL: Message".
        """
        print(f"\n--- Parsing with .split() ---\nLog: '{log_entry}'")
        parts = log_entry.split(':')
        if len(parts) >= 2:
            log_level = parts[0]
            message = parts[1].strip() # Use .strip() to remove leading whitespace
            print(f"  Level: {log_level}")
            print(f"  Message: {message}")
        else:
            print("  Could not parse log entry.")

    def find_ip_address(log_entry):
        """
        Finds an IPv4 address in a log entry using regular expressions.
        """
        print(f"\n--- Finding IP with RegEx ---\nLog: '{log_entry}'")

        # RegEx pattern for an IPv4 address
        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

        # Use re.search to find the first match
        match = re.search(ip_pattern, log_entry)

        if match:
            # The matched string is retrieved with .group(0)
            ip_address = match.group(0)
            print(f"  IP Address Found: {ip_address}")
        else:
            print("  No IP Address found in this entry.")


    def main():
        """
        Main function to run the log parsing examples.
        """
        log1 = "INFO:User 'admin_kali' logged in successfully."
        log2 = "WARNING:Failed login attempt from IP 192.168.1.10 for user 'guest'."
        log3 = "ERROR:Service 'sshd' failed to start on port 22."
        log4 = "Firewall block from 10.25.30.100 to destination 8.8.8.8"

        # --- Practice with .split() ---
        parse_log_entry_simple(log1)
        parse_log_entry_simple(log2) # Notice this won't be perfect

        # --- Practice with Regular Expressions ---
        find_ip_address(log1)
        find_ip_address(log2)
        find_ip_address(log3)
        find_ip_address(log4)


    if __name__ == "__main__":
        main()

    ```

4.  **Save and Exit `nano`**.

**Tasks:**

1.  **Run the script:**
    *   From your terminal, run the script:
        ```bash
        python3 log_parser.py
        ```
    *   **Analyze the output:**
        *   How well did the `.split(':')` method work for `log1`?
        *   What was the problem when using `.split(':')` on `log2`? This shows the limitation of simple splitting when the format isn't perfectly consistent.
        *   Did the regular expression correctly find the IP addresses in `log2` and `log4`?
        *   Why didn't the RegEx find an IP in `log1` and `log3`?

2.  **Experiment with RegEx (Optional):**
    *   Modify the script to use `re.findall()` instead of `re.search()` on `log4`. What is the difference in the output?
    *   Can you write a RegEx pattern to extract the username from `log2` (the word in single quotes)? Hint: `'(\w+)'`. The parentheses create a "capturing group".

3.  **Deactivate the Virtual Environment:**
    *   When you are finished, type `deactivate`.

## 4. Reflection and Next Steps

*   **Self-Reflection:** When is a simple `.split()` good enough for parsing? When do you need the power of regular expressions? How could you combine these techniques to parse even more complex logs?
*   **Next Module:** In the final Python module, we will focus on **Python in Practice**, learning about file handling and building complete automation scripts.

---
