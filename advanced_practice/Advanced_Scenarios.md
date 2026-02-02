# Advanced Practice Scenarios for SOC Analysis

## Introduction

This guide presents a series of advanced practice scenarios designed to test and enhance your skills in Linux command-line analysis, Python scripting, and SQL querying. Each scenario simulates a real-world task that a Junior SOC Analyst might encounter. Use the provided data sources and the tools you've learned to investigate and answer the questions posed in each scenario.

## Scenario 1: Investigate a Potential Brute-Force Attack

**Objective:** Analyze authentication logs to identify and report on a suspected brute-force attack against the SSH service.

**Data Source:** `data_sources/fake_auth.log`

**Primary Tools:** Linux Command-Line (`grep`, `awk`, `sort`, `uniq`, `wc`), Python

### Tasks:

1.  **Initial Triage (Linux CLI):**
    *   Using `grep`, find all log entries related to "Failed password".
    *   From the "Failed password" entries, identify the IP address that has the most failed attempts. (Hint: Chain `grep`, `awk` to extract the IP, `sort`, `uniq -c` to count, and `sort -nr` to order).
    *   Identify all the usernames that were targeted by this top attacking IP address.
    *   Check if the top attacking IP ever had a successful login (i.e., an "Accepted password" entry).

2.  **Automated Analysis (Python):**
    *   Write a Python script in your `scripts/` directory named `brute_force_detector.py`.
    *   This script should read `data_sources/fake_auth.log` line by line.
    *   Use regular expressions (`re` module) to parse each line and extract the timestamp, source IP, and the result of the login attempt (e.g., "Failed password", "Accepted password").
    *   The script should count the number of failed login attempts per IP address.
    *   If any IP has more than a certain threshold of failed attempts (e.g., 10), the script should print a "Brute-Force Alert" including the IP address and the total number of failed attempts from that IP.

## Scenario 2: Web Server Log Anomaly Detection

**Objective:** Analyze web server access logs to identify suspicious or anomalous activity, such as web scanning or broken link discovery.

**Data Source:** `data_sources/fake_access.log`

**Primary Tools:** Linux Command-Line (`grep`, `awk`, `sort`, `uniq`), Python

### Tasks:

1.  **Initial Triage (Linux CLI):**
    *   Find the top 10 IP addresses that have accessed the server the most.
    *   Find all log entries that resulted in a "404 Not Found" status code. Which IP address is responsible for the most 404 errors? This could indicate a web directory scanner.
    *   Identify requests to sensitive paths like `/admin` or `/login`.
    *   Using `grep`, search for suspicious user agents like "curl", "python-requests", or "ZmEu".

2.  **Automated Analysis (Python):**
    *   Write a Python script in your `scripts/` directory named `access_log_analyzer.py`.
    *   The script should read `data_sources/fake_access.log` line by line.
    *   Use regular expressions to parse the log entries and extract the source IP, timestamp, requested path, and status code.
    *   The script should identify and report any IP address that generates more than a certain number of 404 errors (e.g., more than 5).
    *   The script should also list all unique "User-Agent" strings found in the log file, which can help in identifying bots or scanners.

## Scenario 3: Correlate User Data with SQL

**Objective:** Use SQL to analyze user data for potential security risks and policy violations.

**Data Source:** `data_sources/fake_users.csv`, `scripts/users.db` (from previous exercise)

**Primary Tools:** SQLite3, Python

### Tasks:

1.  **Data Import (Python & SQL):**
    *   Write a Python script in your `scripts/` directory named `import_users_csv.py`.
    *   This script should:
        1.  Connect to your `scripts/users.db` SQLite database.
        2.  Create a new table called `employees` with columns matching the `fake_users.csv` file (`user_id`, `username`, `email`, `department`, `is_admin`, `last_login`).
        3.  Read the `fake_users.csv` file (using the `csv` module).
        4.  Insert all the user data from the CSV into the `employees` table.
    *   Run this script to populate your database.

2.  **Database Interrogation (SQLite3):**
    *   Open your database: `sqlite3 users.db`
    *   **Find Privileged Accounts:** Write a query to select all users who are administrators (`is_admin = 1`).
    *   **Identify Stale Admin Accounts:** Write a query to find all administrators who have not logged in since a specific date (e.g., before '2025-06-01'). This is a major security risk.
    *   **Cross-Departmental Analysis:** Write a query to count the number of users in each `department`.
    *   **Search for Suspicious Usernames:** Write a query to find any usernames that seem generic or suspicious (e.g., containing "test", "temp", etc. - though none may exist in the fake data, this is for practice).
    *   **Correlate with Auth Logs (Conceptual):** How would you use this database to investigate a login attempt from your `fake_auth.log`? (e.g., if you see a login from `user_x`, how would you find their department and admin status?).

---

**Next Steps:** Work through these scenarios one by one. Create the Python scripts as instructed, and document your findings or create a new portfolio guide for each scenario you complete. This is excellent material for your GitHub repository.
