# Portfolio Guide: Data Generation for SOC Analysis Practice

## 1. Introduction

For effective cybersecurity training and building a robust portfolio, it's crucial to work with realistic data. This guide details the process of generating fake, yet representative, security logs (authentication and web access) and user data. This generated data will serve as the foundation for your advanced practice scenarios and the capstone project.

**Objective:** Understand the structure and content of the simulated data to be used in subsequent analysis tasks.

## 2. Data Generation Script (`generate_soc_data.py`)

The script located at `scripts/generate_soc_data.py` was used to create the following data files:
*   `data_sources/fake_auth.log`
*   `data_sources/fake_access.log`
*   `data_sources/fake_users.csv`

### How the Script Works:

The Python script leverages modules like `random`, `datetime`, `ipaddress`, and `csv` to produce varied and realistic log entries and user details. It simulates common events that a SOC analyst would encounter.

## 3. Description of Generated Data Files

### `fake_auth.log` (Authentication Log)

*   **Format:** Similar to a Linux `/var/log/auth.log` or `syslog` format.
*   **Content:** Records simulated authentication attempts and sessions for various users from different IP addresses.
*   **Example Entry (Accepted Password):**
    ```
    Feb 02 10:35:12 kali-host sshd[1234]: Accepted password for user_1 from 192.168.1.5 port 54321 ssh2
    ```
*   **Example Entry (Failed Password):**
    ```
    Feb 02 10:35:15 kali-host sshd[1235]: Failed password for user_5 from 203.0.113.1 port 12345 ssh2
    ```
*   **Example Entry (Invalid User):**
    ```
    Feb 02 10:35:20 kali-host sshd[1236]: Invalid user unknown_hacker from 198.51.100.2 port 8080
    ```
*   **Key Fields for Analysis:**
    *   **Timestamp:** Date and time of the event.
    *   **Hostname:** `kali-host` (static in this simulation).
    *   **Process:** `sshd`, `sudo`, `CRON`.
    *   **Event Type:** "Accepted password", "Failed password", "Invalid user", "session opened", "session closed".
    *   **Username:** User involved in the event.
    *   **Source IP:** IP address from which the attempt originated.

### `fake_access.log` (Web Server Access Log)

*   **Format:** Standard Apache Common Log Format (CLF) or similar.
*   **Content:** Records simulated HTTP requests made to a web server.
*   **Example Entry:**
    ```
    192.168.1.10 - - [02/Feb/2026:10:30:00 +0000] "GET /index.html HTTP/1.1" 200 1234 "https://google.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    ```
*   **Key Fields for Analysis:**
    *   **Source IP:** IP address of the client making the request.
    *   **Timestamp:** Date and time of the request.
    *   **HTTP Method:** GET, POST, HEAD.
    *   **Requested Path:** `/`, `/login`, `/admin`, etc.
    *   **HTTP Protocol:** HTTP/1.1.
    *   **Status Code:** 200 (OK), 404 (Not Found), 500 (Server Error), 403 (Forbidden), etc.
    *   **Response Size:** Size of the response in bytes.
    *   **Referrer:** Previous page visited.
    *   **User-Agent:** Browser/client making the request (e.g., `curl`, `python-requests`, common browser user agents, scanner user agents).

### `fake_users.csv` (User List CSV)

*   **Format:** Comma-Separated Values.
*   **Content:** A list of simulated user accounts with various attributes.
*   **Example Entry (Header Row):**
    ```
    user_id,username,email,department,is_admin,last_login
    ```
*   **Example Entry (Data Row):**
    ```
    1,alice_smith_1,alice_smith_1@example.com,IT,0,2026-01-15 10:30:00
    ```
*   **Key Fields for Analysis:**
    *   **`user_id`:** Unique identifier for the user.
    *   **`username`:** The user's account name.
    *   **`email`:** User's email address.
    *   **`department`:** The department the user belongs to.
    *   **`is_admin`:** Binary (0 or 1) indicating if the user has administrative privileges.
    *   **`last_login`:** Timestamp of the user's last login.

## 4. Next Steps

You now have realistic data in your `data_sources/` directory to practice your analysis skills. We will use these files in upcoming Advanced Practice Scenarios and the Capstone Project.

---
