# Portfolio Guide: Course 4 - Module 3: Command Line Mastery (The Linux)

## 1. Introduction

This guide covers Module 3 of Course 4, "Tools of the Trade—Linux and SQL," which is dedicated to mastering the Linux command line. Proficiency with the CLI is perhaps the most critical skill for any cybersecurity professional, enabling efficient system navigation, data analysis, and automation.

**Module Objectives:**
*   Master basic directory navigation commands (`pwd`, `ls`, `cd`).
*   Learn to read file content using `cat`, `head`, `tail`, and `less`.
*   Effectively filter output using `grep` and the pipe (`|`) operator.
*   Find files using the `find` command.
*   Manage files and directories (`mkdir`, `rm`, `mv`, `cp`) and edit text with `nano`.
*   Understand and manage file permissions (`chmod`) and user accounts (`sudo`, `useradd`, `userdel`), adhering to the Principle of Least Privilege.

## 2. Key Concepts & Commands

### Directory Navigation

*   `pwd` (Print Working Directory): Shows your current location in the filesystem.
    *   **Syntax:** `pwd`
*   `ls` (List Directory Contents): Shows files and directories in the current or specified location.
    *   **Syntax:** `ls [options] [directory]`
    *   **Common options:** `-l` (long listing), `-a` (all files, including hidden), `-h` (human-readable sizes).
*   `cd` (Change Directory): Moves you between directories.
    *   **Syntax:** `cd [directory]`
    *   **Examples:** `cd /var/log`, `cd ..` (go up one level), `cd ~` (go to home directory), `cd -` (go to previous directory).

### Reading Files

*   `cat` (Concatenate and Display Files): Displays the entire content of a file. Good for small files.
    *   **Syntax:** `cat [file]`
*   `head`: Displays the beginning (default 10 lines) of a file.
    *   **Syntax:** `head [options] [file]`
    *   **Option:** `-n [number]` (display specified number of lines).
*   `tail`: Displays the end (default 10 lines) of a file. Useful for logs that are actively being written to.
    *   **Syntax:** `tail [options] [file]`
    *   **Option:** `-n [number]`, `-f` (follow file as it grows).
*   `less`: Allows you to view file content page by page. Good for large files.
    *   **Syntax:** `less [file]`
    *   **Navigation:** `Spacebar` (page down), `b` (page up), `Arrow keys` (line by line), `/` (search), `n` (next search result), `q` (quit).

### Filtering & Finding

*   `grep` (Global Regular Expression Print): Searches for patterns in text files.
    *   **Syntax:** `grep [options] 'pattern' [file(s)]`
    *   **Common options:** `-i` (ignore case), `-v` (invert match), `-c` (count matches), `-n` (show line numbers).
*   `|` (Pipe): Sends the output of one command as the input to another command. Crucial for chaining commands.
    *   **Syntax:** `command1 | command2 | command3`
*   `find`: Searches for files and directories based on various criteria.
    *   **Syntax:** `find [path] [expression]`
    *   **Common expressions:** `-name 'pattern'`, `-type f` (file), `-type d` (directory), `-size +1M` (size greater than 1MB), `-mtime -7` (modified in last 7 days).

### Managing Files & Directories

*   `mkdir` (Make Directory): Creates new directories.
    *   **Syntax:** `mkdir [directory_name]`
    *   **Option:** `-p` (create parent directories if they don't exist).
*   `rm` (Remove): Deletes files or directories. **Use with extreme caution.**
    *   **Syntax:** `rm [options] [file/directory]`
    *   **Common options:** `-r` (recursive, for directories), `-f` (force, no prompt).
*   `mv` (Move): Renames or moves files/directories.
    *   **Syntax:** `mv [source] [destination]`
*   `cp` (Copy): Copies files or directories.
    *   **Syntax:** `cp [options] [source] [destination]`
    *   **Common option:** `-r` (recursive, for directories).
*   `nano`: A simple, user-friendly text editor in the terminal.
    *   **Syntax:** `nano [file]`
    *   **Usage:** Commands shown at the bottom (e.g., `^X` is `Ctrl+X` to Exit).

### Permissions & Users

*   **File Permissions (rwx):**
    *   `r` (read): Allows viewing file content or listing directory content.
    *   `w` (write): Allows modifying file content or creating/deleting files in a directory.
    *   `x` (execute): Allows running a file as a program or entering a directory.
    *   **Represented as:** `user` | `group` | `others` (e.g., `rwx r-x r--` or `754`).
*   `chmod` (Change Mode): Changes file permissions.
    *   **Syntax:** `chmod [permissions] [file]`
    *   **Examples:** `chmod 755 script.sh`, `chmod +x script.sh` (make executable).
*   `sudo` (SuperUser DO): Executes a command with elevated (root) privileges. **Use only when necessary.**
    *   **Syntax:** `sudo [command]`
*   `useradd`: Creates a new user account. (Requires `sudo`).
    *   **Syntax:** `sudo useradd [options] [username]`
*   `userdel`: Deletes a user account. (Requires `sudo`).
    *   **Syntax:** `sudo userdel [options] [username]`

## 3. Practical Exercise: Command Line Scavenger Hunt

Let's put your command line mastery to the test with a series of tasks within your Kali environment. You will be operating within your project directory for most tasks.

**Objective:** Practice core CLI commands for navigation, file manipulation, and basic analysis.

**Setup:**
First, ensure you are in your project's `scripts` directory and activate your virtual environment:
```bash
cd ~/gemini_projects/cyber_soc_trainee/scripts
source ~/.venv/bin/activate
```
*(You'll notice the `(.venv)` prefix in your terminal prompt, indicating the virtual environment is active.)*

**Tasks:**

1.  **Create a temporary working directory:**
    *   Create a directory named `temp_cli_work` inside your current `scripts` directory.
    *   Move into this new directory.
    *   Confirm your current location.

2.  **Create and edit a text file:**
    *   Create an empty file named `system_info.txt`.
    *   Open `system_info.txt` using `nano`.
    *   Type the following lines into the file (do not include the asterisks):
        ```
        *Operating System: Kali GNU/Linux*
        *Kernel Version: 6.x.x-kali*
        *Uptime: X days, Y hours*
        *Users logged in: Z*
        *Important Service: sshd*
        *Another Service: apache2*
        ```
    *   Save and exit `nano`.

3.  **Inspect file content:**
    *   Display the entire content of `system_info.txt`.
    *   Display only the first 2 lines of `system_info.txt`.
    *   Display only the last line of `system_info.txt`.

4.  **Search and Filter:**
    *   Find all lines in `system_info.txt` that contain the word "Service" (case-sensitive).
    *   Find all lines in `system_info.txt` that contain the word "version" (case-insensitive).
    *   Count how many times the word "Service" appears in `system_info.txt`.
    *   List all files in `/etc/` that contain "kali" in their name. (Hint: Use `grep` with `ls` or `find`).

5.  **Copy, Rename, and Move:**
    *   Copy `system_info.txt` to a new file named `backup_info.txt` within the same `temp_cli_work` directory.
    *   Rename `backup_info.txt` to `old_system_info.txt`.
    *   Move `old_system_info.txt` to the parent directory (your `scripts` directory).
    *   Confirm that `old_system_info.txt` is no longer in `temp_cli_work` but is now in `scripts`.

6.  **Manage Permissions:**
    *   Inside `temp_cli_work`, create an empty executable script file: `touch my_script.sh`
    *   Verify its initial permissions (using `ls -l`).
    *   Make `my_script.sh` executable only by the owner (you). Use the numeric `chmod` value.
    *   Verify the updated permissions.

7.  **Clean Up:**
    *   Go up one directory level (back to `scripts`).
    *   Remove the `temp_cli_work` directory and its contents **without being prompted for confirmation**. **Be extremely careful with this command in real environments.**
    *   Remove `old_system_info.txt` from the `scripts` directory.
    *   Deactivate your virtual environment: `deactivate`

## 4. Reflection and Next Steps

*   **Self-Reflection:** Which commands felt most powerful? What are the potential dangers of commands like `rm -rf` or `sudo`?
*   **Next Module:** In the next module, we will shift our focus to **SQL Fundamentals** from Course 4.

---
