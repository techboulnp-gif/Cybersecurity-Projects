# scripts/generate_soc_data.py

import os
import random
import datetime
import ipaddress
import csv

# --- Configuration ---
DATA_DIR = '../data_sources'
NUM_AUTH_LOG_ENTRIES = 500
NUM_ACCESS_LOG_ENTRIES = 1000
NUM_USERS = 50

AUTH_LOG_FILE = os.path.join(DATA_DIR, 'fake_auth.log')
ACCESS_LOG_FILE = os.path.join(DATA_DIR, 'fake_access.log')
USERS_CSV_FILE = os.path.join(DATA_DIR, 'fake_users.csv')

# Ensure the data_sources directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# --- Helper Functions ---
def random_ipv4():
    """Generates a random IPv4 address."""
    return str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))

def random_datetime(start_date, end_date):
    """Generates a random datetime between two dates."""
    time_delta = end_date - start_date
    random_seconds = random.randint(0, int(time_delta.total_seconds()))
    return start_date + datetime.timedelta(seconds=random_seconds)

def generate_auth_log_entry(start_time, end_time, usernames, ips):
    """Generates a single fake authentication log entry."""
    timestamp = random_datetime(start_time, end_time).strftime('%b %d %H:%M:%S')
    hostname = "kali-host"
    process = random.choice(["sshd", "sudo", "CRON"])
    pid = random.randint(1000, 9999)
    user = random.choice(usernames)
    ip = random.choice(ips)

    event_type = random.choices(
        ["Accepted password", "Failed password", "Invalid user", "session opened", "session closed"],
        weights=[0.6, 0.2, 0.1, 0.05, 0.05], k=1
    )[0]

    if "Accepted" in event_type or "Failed" in event_type:
        return f"{timestamp} {hostname} {process}[{pid}]: {event_type} for {user} from {ip} port {random.randint(1024, 65535)} ssh2"
    elif "Invalid user" in event_type:
        return f"{timestamp} {hostname} {process}[{pid}]: {event_type} {user} from {ip} port {random.randint(1024, 65535)}"
    else:
        return f"{timestamp} {hostname} {process}[{pid}]: {event_type} for user {user}"

def generate_access_log_entry(start_time, end_time, ips):
    """Generates a single fake web server access log entry."""
    timestamp = random_datetime(start_time, end_time).strftime('%d/%b/%Y:%H:%M:%S +0000')
    ip = random.choice(ips)
    method = random.choice(["GET", "POST", "HEAD"])
    path = random.choice(["/", "/index.html", "/login", "/admin", "/api/v1/data", "/images/logo.png"])
    protocol = "HTTP/1.1"
    status = random.choices([200, 404, 500, 301, 403], weights=[0.7, 0.15, 0.05, 0.05, 0.05], k=1)[0]
    size = random.randint(100, 5000)
    user_agent = random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
        "curl/7.68.0",
        "python-requests/2.25.1",
        "Go-http-client/1.1", # Common for bots/scanners
        "ZmEu", # Another common scanner user agent
    ])
    referrer = random.choice(["-", "https://google.com/", "https://bing.com/", "https://example.com/"])

    return f'{ip} - - [{timestamp}] "{method} {path} {protocol}" {status} {size} "{referrer}" "{user_agent}"'

def generate_users_csv(num_users):
    """Generates a CSV of fake users."""
    headers = ["user_id", "username", "email", "department", "is_admin", "last_login"]
    users = []
    first_names = ["alice", "bob", "charlie", "david", "eve", "frank", "grace", "heidi"]
    last_names = ["smith", "jones", "williams", "brown", "davis", "miller", "wilson", "moore"]
    departments = ["HR", "IT", "Sales", "Marketing", "Engineering", "Finance", "Security"]

    for i in range(1, num_users + 1):
        username = f"{random.choice(first_names)}_{random.choice(last_names)}_{i}"
        email = f"{username}@example.com"
        department = random.choice(departments)
        is_admin = random.choice([True, False, False, False]) # More non-admins
        last_login = random_datetime(datetime.datetime(2025, 1, 1), datetime.datetime(2026, 2, 2)).strftime('%Y-%m-%d %H:%M:%S')

        users.append({
            "user_id": i,
            "username": username,
            "email": email,
            "department": department,
            "is_admin": 1 if is_admin else 0,
            "last_login": last_login
        })
    return headers, users

# --- Main Generation Logic ---
def main():
    print(f"Generating fake SOC data into '{DATA_DIR}'...")

    start_date = datetime.datetime(2026, 1, 1)
    end_date = datetime.datetime(2026, 2, 2, 23, 59, 59)

    # Generate common data for logs
    usernames = [f"user_{i}" for i in range(1, NUM_USERS + 1)] + ["admin_kali", "root", "guest", "johndoe", "unknown_hacker"]
    ips = [str(ipaddress.IPv4Address('192.168.1.0') + i) for i in range(20)] + \
          [str(ipaddress.IPv4Address('10.0.0.0') + i) for i in range(10)] + \
          [str(ipaddress.IPv4Address('172.16.0.0') + i) for i in range(15)] + \
          ['203.0.113.1', '198.51.100.1', '198.51.100.2', '198.51.100.3'] # Malicious/external IPs

    # Generate Auth Logs
    with open(AUTH_LOG_FILE, 'w') as f:
        for _ in range(NUM_AUTH_LOG_ENTRIES):
            f.write(generate_auth_log_entry(start_date, end_date, usernames, ips) + '\n')
    print(f"Generated {NUM_AUTH_LOG_ENTRIES} auth log entries in '{AUTH_LOG_FILE}'")

    # Generate Access Logs
    with open(ACCESS_LOG_FILE, 'w') as f:
        for _ in range(NUM_ACCESS_LOG_ENTRIES):
            f.write(generate_access_log_entry(start_date, end_date, ips) + '\n')
    print(f"Generated {NUM_ACCESS_LOG_ENTRIES} access log entries in '{ACCESS_LOG_FILE}'")

    # Generate Users CSV
    headers, users_data = generate_users_csv(NUM_USERS)
    with open(USERS_CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(users_data)
    print(f"Generated {NUM_USERS} user entries in '{USERS_CSV_FILE}'")

    print("Data generation complete.")

if __name__ == "__main__":
    main()
