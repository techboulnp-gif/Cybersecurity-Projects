# Portfolio Guide: Course 4 - Module 4: SQL Fundamentals

## 1. Introduction

This guide covers Module 4 of Course 4, "Tools of the Trade—Linux and SQL," which introduces the fundamentals of Structured Query Language (SQL). SQL is essential for any cybersecurity professional to store, retrieve, manipulate, and analyze data, particularly in investigations involving logs, user databases, or application data. We will be using **SQLite3**, a lightweight, file-based database system, perfect for local practice.

**Module Objectives:**
*   Learn how to access SQL through the Linux terminal using `sqlite3`.
*   Master basic queries: `SELECT` and `FROM`.
*   Filter and sort results using the `WHERE` clause and `ORDER BY`.
*   Use wildcards (`%`, `_`) with the `LIKE` operator to find patterns.
*   Combine filters with `AND`, `OR`, and `NOT` logical operators.
*   Understand and perform `JOIN` operations to combine data from multiple tables.

## 2. Key Concepts & Commands (SQLite3)

### Accessing SQLite3

*   To start the SQLite3 prompt: `sqlite3`
*   To open a specific database file: `sqlite3 [database_file.db]`
*   SQLite3 commands (start with `.`) vs. SQL statements (end with `;`).
    *   `.quit`: Exit SQLite3.
    *   `.tables`: List tables in the current database.
    *   `.schema [table_name]`: Show the CREATE TABLE statement for a table.

### Basic Queries

*   **`SELECT`**: Specifies the columns you want to retrieve.
    *   `SELECT column1, column2 FROM table_name;`
    *   `SELECT * FROM table_name;` (retrieves all columns)
*   **`FROM`**: Specifies the table(s) from which to retrieve data.

### Filtering & Sorting

*   **`WHERE`**: Filters rows based on a specified condition.
    *   `SELECT column1 FROM table_name WHERE condition;`
    *   **Conditions:** `column = value`, `column > value`, `column < value`, `column >= value`, `column <= value`, `column <> value` (not equal).
*   **`ORDER BY`**: Sorts the result set.
    *   `SELECT column1 FROM table_name ORDER BY column_name ASC|DESC;` (ASC is ascending, DESC is descending).

### Wildcards & Pattern Matching (`LIKE`)

*   **`LIKE`**: Used in a `WHERE` clause to search for a specified pattern in a column.
*   **Wildcards:**
    *   `%`: Represents zero or more unknown characters.
    *   `_`: Represents a single unknown character.
    *   `SELECT column1 FROM table_name WHERE column_name LIKE 'pattern';`
    *   **Example:** `WHERE username LIKE 'joh%'` (starts with "joh"), `WHERE filename LIKE '%.log'` (ends with ".log").

### Logical Operators

*   **`AND`**: Combines two or more conditions. All conditions must be true.
    *   `WHERE condition1 AND condition2;`
*   **`OR`**: Combines two or more conditions. At least one condition must be true.
    *   `WHERE condition1 OR condition2;`
*   **`NOT`**: Negates a condition.
    *   `WHERE NOT condition;`

### Joins

*   **`JOIN` (or `INNER JOIN`)**: Returns rows when there is at least one match in both tables.
    *   `SELECT columns FROM table1 JOIN table2 ON table1.column = table2.column;`
*   **`LEFT JOIN`**: Returns all rows from the left table, and the matched rows from the right table. If no match, NULLs for right table columns.
    *   `SELECT columns FROM table1 LEFT JOIN table2 ON table1.column = table2.column;`

## 3. Practical Exercise: Building and Querying a User Database

Let's simulate a simple user database and practice SQL queries to extract information, similar to what a SOC analyst might do with a user management system or log data.

**Objective:** Create a SQLite database, populate it with data, and perform various queries including filtering, sorting, pattern matching, and joins.

**Setup:**

1.  **Navigate to your scripts directory and activate your virtual environment:**
    ```bash
    cd ~/gemini_projects/cyber_soc_trainee/scripts
    source ~/.venv/bin/activate
    ```
2.  **Create a new SQLite database file:**
    ```bash
    sqlite3 users.db
    ```
    This will open the SQLite prompt.

3.  **Create Tables:** At the SQLite prompt, enter the following SQL statements to create two tables: `users` and `roles`. Each statement must end with a semicolon `;`.

    ```sql
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        email TEXT UNIQUE,
        role_id INTEGER,
        last_login TEXT,
        is_active INTEGER,
        FOREIGN KEY (role_id) REFERENCES roles(role_id)
    );

    CREATE TABLE roles (
        role_id INTEGER PRIMARY KEY,
        role_name TEXT NOT NULL UNIQUE
    );
    ```
    *(Press Enter after the last semicolon for each `CREATE TABLE` statement.)*

4.  **Insert Data:** Now, insert some sample data into your tables:

    ```sql
    INSERT INTO roles (role_id, role_name) VALUES
    (1, 'Administrator'),
    (2, 'Analyst'),
    (3, 'User'),
    (4, 'Guest');

    INSERT INTO users (username, email, role_id, last_login, is_active) VALUES
    ('admin_kali', 'admin@example.com', 1, '2026-02-02 10:00:00', 1),
    ('john_doe', 'john.doe@example.com', 3, '2026-02-01 15:30:00', 1),
    ('jane_smith', 'jane.smith@example.com', 2, '2026-02-02 09:15:00', 1),
    ('guest_user', 'guest@example.com', 4, '2026-01-30 08:00:00', 0),
    ('bob_analyst', 'bob.analyst@example.com', 2, '2026-02-02 11:45:00', 1),
    ('inactive_user', 'inactive@example.com', 3, '2026-01-25 12:00:00', 0);
    ```
    *(Press Enter after the last semicolon for each `INSERT INTO` statement.)*

5.  **Verify Tables and Schema:**
    *   List tables: `.tables`
    *   Show schema for `users`: `.schema users`
    *   Show schema for `roles`: `.schema roles`

**Tasks:**

1.  **Retrieve All Users:**
    *   Select all columns and all rows from the `users` table.

2.  **Find Active Analysts:**
    *   Select the `username` and `email` of all users who are `is_active = 1` AND have a `role_id` corresponding to 'Analyst'. (You'll need a subquery or a join, but try to figure it out with just `WHERE` first based on `role_id`).

3.  **Users with Specific Last Login:**
    *   Select all users who last logged in on `2026-02-02`.

4.  **Users with 'admin' in Username:**
    *   Select the `username` of any user whose username contains the string 'admin' (case-insensitive if possible, but SQLite `LIKE` is case-insensitive for ASCII).

5.  **Sort Users by Last Login:**
    *   Select `username`, `email`, and `last_login` for all users, sorted by their `last_login` time in descending order.

6.  **Find Users Not Logged In Recently:**
    *   Select `username` and `last_login` for users whose `last_login` is BEFORE `2026-02-01`.

7.  **Combine User and Role Information (JOIN):**
    *   Select `username`, `email`, and `role_name` by joining the `users` and `roles` tables.

8.  **List All Roles and Associated Users (LEFT JOIN):**
    *   Show all `role_name`s, and the `username`s of users assigned to them. Include roles that currently have no users assigned (if any existed, like a 'Developer' role we didn't add users to).

9.  **Exit SQLite3:**
    *   Type `.quit`

10. **Deactivate Virtual Environment:**
    *   `deactivate`

## 4. Reflection and Next Steps

*   **Self-Reflection:** How does SQL provide structured access to data compared to plain text files? How could these queries be useful in a cybersecurity investigation (e.g., finding inactive administrator accounts, tracing user activity)?
*   **Next Module:** In the next phase, we will shift our focus to **Python Scripting**, starting with **Module 1: Python Core Foundations** from Course 7.

---
