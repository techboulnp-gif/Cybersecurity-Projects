# SOC Analyst Portfolio Project Instructions

This document is your comprehensive quick-start guide for navigating and utilizing your SOC Analyst Portfolio project.

---

## 1. Daily Workflow (Step-by-Step)

Follow these steps each time you want to work on your project:

1.  **Launch the Project Environment:**
    *   Open a new terminal and type the shortcut command:
        ```bash
        gemini-soc
        ```
    *   This will automatically take you to your project directory and launch this CLI.

2.  **Review Your Progress & Plan:**
    *   Check your master checklist to see what's next:
        *   Ask me: *"What's the next task on the TODO list?"*
        *   Or view the file yourself: `less TODO.md`
    *   (Optional) Refresh your memory on our last session by viewing the latest summary in the `SOC_Project_Info/Save_Chat` folder on your Desktop.

3.  **Start Working:**
    *   Tell me what you want to work on. You can be conversational!
        *   *"Let's start Advanced Scenario 1."*
        *   *"I need help with the Python script for the brute-force detector."*

4.  **Save Your Progress:**
    *   At the end of your session, or after a major task, use our command to create a session summary:
        ```
        save chat
        ```
    *   This will create a new, timestamped summary file in the `SOC_Project_Info/Save_Chat` folder on your Desktop.

---

## 2. Key Commands & Features

### `gemini-soc`
*   **What it does:** A permanent system shortcut that changes to your project directory (`/home/kali/gemini_projects/cyber_soc_trainee`) and launches the Gemini CLI.
*   **When to use it:** Always use this to start a new work session.

### `save chat`
*   **What it does:** Creates a date- and time-stamped summary of our session's accomplishments, decisions, and actions.
*   **Where it's saved:** `/home/kali/Desktop/SOC_Project_Info/Save_Chat/`
*   **Filename Format:** `Session_Summary_YYYY-MM-DD_hh-mmAMPM.md`
*   **Timezone:** Mountain Time (Utah time).

---

## 3. Tips, Tricks & Efficient Workflow

*   **Conversational References:** You **do not** need to type full file paths. I have the context of our project. Just refer to files or scenarios by name (e.g., "Advanced Scenario 2", "the `log_parser.py` script").
*   **Checking Your Work:** Ask me directly to review your work.
    *   *"Can you check my command for finding the top IP address?"*
    *   *"Is this Python code correct?"*
    *   *"Review my SQL query for finding stale admin accounts."*
*   **Documentation:** I will automatically ask you if we need to update our documentation (like the `REPLICATION_GUIDE.md`) after we make any significant changes to the project structure.
*   **Screenshot Prompts:** As we work through scenarios, I will prompt you when it's a good time to take a screenshot for your portfolio guides and suggest a descriptive filename (e.g., `s1_t1_output.png`).

---

## 4. Important Files & Folders

| File / Folder                                                               | Location                                    | Purpose                                                     |
| :-------------------------------------------------------------------------- | :------------------------------------------ | :---------------------------------------------------------- |
| **`TODO.md`**                                                               | Project Root                                | Your master checklist of all tasks and progress.            |
| **`Advanced_Scenarios.md`**                                                 | `advanced_practice/`                        | The guide for your advanced cybersecurity practice tasks.   |
| **`Save_Chat/`**                                                            | `Desktop/SOC_Project_Info/`                 | Contains all your session summary files.                    |
| **`google_course_work/`**                                                   | Project Root                                | Contains all portfolio guides from your course curriculum.  |
| **`scripts/`**                                                              | Project Root                                | Where you should save all your custom Python, SQL, and shell scripts. |
| **`data_sources/`**                                                         | Project Root                                | Contains the fake log and user data for your scenarios.     |
| **`GLOSSARY.md`**                                                           | Project Root                                | A quick reference for key terms, acronyms, and concepts.    |
| **`Backup_Instructions/`**                                                  | `Desktop/SOC_Project_Info/`                 | Contains the step-by-step guide for backing up to GitHub.   |

---

## 5. Project Structure Overview

*   `/home/kali/gemini_projects/cyber_soc_trainee` (Project Root)
    *   `.venv/`: Python virtual environment.
    *   `advanced_practice/`: Additional challenges and learning materials.
    *   `data_sources/`: Storage for fake logs, CSVs, and other data for analysis.
    *   `google_course_work/`: Files and exercises directly related to the Google Cybersecurity Course.
    *   `portfolio_guides/`: Markdown files documenting your step-by-step solutions for resume/GitHub.
    *   `scripts/`: Python, SQL, and shell scripts you develop.
    *   `README.md`: The main project overview for your GitHub repository.
    *   `TODO.md`: Your progress tracking checklist.
    *   `.gitignore`: Tells Git which files to ignore.