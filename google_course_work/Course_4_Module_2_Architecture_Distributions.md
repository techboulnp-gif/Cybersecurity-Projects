# Portfolio Guide: Course 4 - Module 2: Linux Architecture & Distributions

## 1. Introduction

This guide covers Module 2 of Course 4, "Tools of the Trade—Linux and SQL," focusing on the fundamental architecture of Linux operating systems and the various distributions available. Understanding these concepts is essential for navigating, customizing, and securing Linux environments effectively.

**Module Objectives:**
*   Break down the Linux architecture: User, Applications, Shell, File System Hierarchy (FHS), Kernel, and Hardware.
*   Identify common Linux distributions like Kali Linux, Ubuntu, Parrot, and RHEL.
*   Master package managers to install and manage applications using `APT` (Debian/Ubuntu) or `YUM` (Red Hat).

## 2. Key Concepts & Definitions

### Linux Architecture Breakdown

Linux systems are structured in layers, each with specific responsibilities:

1.  **Hardware:** The physical components of the computer (CPU, RAM, storage, network card, etc.).
2.  **Kernel:** The core of the operating system. It manages the hardware, allocates resources, and provides essential services to other parts of the OS. It's the bridge between hardware and software.
3.  **Shell:** A command-line interpreter that acts as an interface between the user and the kernel. It takes commands from the user, executes them, and displays the output. (e.g., Bash, Zsh, Fish).
4.  **Applications:** Software programs that perform specific tasks for the user (e.g., web browsers, text editors, security tools like Wireshark or Nmap).
5.  **User:** You! The person interacting with the system.

### File System Hierarchy Standard (FHS)

The FHS defines the directory structure and content of Linux filesystems. It provides a standardized way to organize files, making it easier for users and applications to find what they need, regardless of the specific Linux distribution.

| Directory   | Purpose                                                                | Example Content                                         |
| :---------- | :--------------------------------------------------------------------- | :------------------------------------------------------ |
| `/`         | **Root Directory:** The top-level directory of the filesystem hierarchy. | All other directories reside under `/`                  |
| `/bin`      | **Binaries:** Essential user command binaries.                         | `ls`, `cp`, `mv`, `mkdir`, `rm`                         |
| `/sbin`     | **System Binaries:** Essential system binaries (for system administration). | `fdisk`, `ifconfig`, `mount`                            |
| `/etc`      | **Etc (Configuration):** Host-specific system-wide configuration files. | `/etc/passwd`, `/etc/resolv.conf`, `/etc/apt/sources.list` |
| `/home`     | **Home Directories:** User-specific configuration and data files.      | `/home/youruser/Documents`, `/home/youruser/.config`    |
| `/root`     | **Root's Home Directory:** The home directory for the root user.       |                                                         |
| `/usr`      | **Unix System Resources:** Secondary hierarchy for user programs and data. | `/usr/bin` (non-essential commands), `/usr/share` (docs)|
| `/var`      | **Variable Data:** Contains variable data files (e.g., logs, spool files). | `/var/log` (system logs), `/var/www` (web server files) |
| `/tmp`      | **Temporary Files:** Files that may be deleted between reboots.        |                                                         |
| `/opt`      | **Optional Software:** Add-on application software packages.           | Third-party applications                                |

### Common Linux Distributions

A "distribution" is a specific version of Linux that bundles the Linux kernel with other software (like a desktop environment, system utilities, and applications) into a complete operating system.

*   **Kali Linux:**
    *   **Focus:** Penetration testing and digital forensics.
    *   **Basis:** Debian.
    *   **Key Feature:** Comes pre-installed with hundreds of security tools. (This is what you're using!)
*   **Ubuntu:**
    *   **Focus:** Desktop, server, cloud, IoT. User-friendly.
    *   **Basis:** Debian.
    *   **Key Feature:** Widely popular, large community support, easy to use for beginners.
*   **Parrot OS:**
    *   **Focus:** Security (similar to Kali), privacy, and development.
    *   **Basis:** Debian.
    *   **Key Feature:** Lightweight, strong focus on anonymity tools.
*   **Red Hat Enterprise Linux (RHEL):**
    *   **Focus:** Enterprise-grade server and cloud environments.
    *   **Basis:** Red Hat (commercial).
    *   **Key Feature:** Commercial support, stability, and reliability for critical systems. (Often has free/community versions like Fedora or CentOS Stream).

### Package Managers

Package managers are tools that automate the process of installing, upgrading, configuring, and removing software packages from an operating system. They handle dependencies (other software a program needs to run).

*   **APT (Advanced Package Tool):**
    *   **Used by:** Debian, Ubuntu, Kali Linux, Parrot OS.
    *   **Commands:**
        *   `sudo apt update`: Updates the list of available packages from repositories.
        *   `sudo apt upgrade`: Upgrades all installed packages to their latest versions.
        *   `sudo apt install <package_name>`: Installs a new package.
        *   `sudo apt remove <package_name>`: Removes a package.
        *   `sudo apt search <keyword>`: Searches for packages.
*   **YUM (Yellowdog Updater, Modified) / DNF (Dandified YUM):**
    *   **Used by:** Red Hat, Fedora, CentOS. (DNF is the successor to YUM).
    *   **Commands:**
        *   `sudo dnf update`: Updates the list of available packages.
        *   `sudo dnf upgrade`: Upgrades all installed packages.
        *   `sudo dnf install <package_name>`: Installs a new package.
        *   `sudo dnf remove <package_name>`: Removes a package.

## 3. Practical Exercise: Exploring Your Linux Environment (Architecture & Packages)

Let's use the CLI to explore these concepts within your Kali Linux environment.

**Objective:** Understand your Kali's filesystem and how package management works.

**Steps:**

1.  **Explore the File System Hierarchy:**
    *   **Command:** `ls -F /`
    *   **Explanation:** List the contents of the root directory (`/`). You'll see directories like `bin/`, `etc/`, `home/`, `usr/`, `var/`, etc., confirming the FHS structure.
    *   **Command:** `ls -F /home/kali`
    *   **Explanation:** List the contents of your home directory. Notice directories like `Desktop/`, `Downloads/`, and your `.gemini/` and `gemini_projects/` folders.

2.  **Identify Your Current Shell:**
    *   **Command:** `echo $SHELL`
    *   **Explanation:** Displays the path to your current shell executable (e.g., `/usr/bin/zsh`). This confirms the shell is an application you interact with.

3.  **Use Your Package Manager (APT):**
    *   **Update Package Lists:**
        *   **Command:** `sudo apt update`
        *   **Explanation:** This command fetches the latest information about packages from the repositories. You might be prompted for your user password.
        *   **Task:** Observe the output. It shows APT connecting to various servers to get package lists.
    *   **Search for a Package (e.g., Nmap - a network scanner):**
        *   **Command:** `apt search nmap`
        *   **Explanation:** This will search for all packages whose names or descriptions contain "nmap".
        *   **Task:** Note how many results are returned. You'll likely see `nmap` itself, plus related tools.
    *   **(Optional - if you want to install something harmless and small):**
        *   **Command:** `sudo apt install htop` (htop is a process viewer, like a task manager for the terminal).
        *   **Explanation:** Installs `htop`. If it's already installed, APT will tell you. If not, it will ask for confirmation.
        *   **Task:** If installed, run `htop` and explore it (use `F10` or `q` to quit). Then, if you want to remove it: `sudo apt remove htop`.

## 4. Reflection and Next Steps

*   **Self-Reflection:** How does the FHS provide structure? How do package managers simplify software management?
*   **Next Module:** In the next module, we will dive deeper into **Command Line Mastery**, focusing on essential Linux commands for navigation, file manipulation, and basic text processing.

---
