# GitHub Backup Steps for SOC Analyst Portfolio

This guide provides step-by-step instructions for backing up your local project changes to your remote GitHub repository. Regular backups are crucial for version control, collaboration, and data redundancy.

---

## Process Overview: Commit & Push

Backing up your changes to GitHub involves two main steps:

1.  **Commit:** Saving your changes to your local Git history. This creates a "snapshot" of your project at a specific point in time.
2.  **Push:** Sending those local commits from your machine to your remote GitHub repository.

---

## Step-by-Step Guide

### Prerequisite: Ensure you are in your project directory

*   **Open a terminal** and use your shortcut:
    ```bash
    gemini-soc
    ```
    (This will take you to `/home/kali/gemini_projects/cyber_soc_trainee/` and launch the CLI.)
*   **Alternatively,** manually navigate:
    ```bash
    cd /home/kali/gemini_projects/cyber_soc_trainee
    ```
    (You should see `(venv)` in your prompt, indicating you're in the right place with the virtual environment active.)

### 1. Stage Your Changes (Add Files to be Committed)

This command tells Git which of your modified or new files should be included in the next commit.

```bash
git add .
```
*   The `.` means "add all changes in the current directory and its subdirectories."

### 2. Commit Your Changes (Save Locally)

This command saves the staged changes to your local Git history. Always use a descriptive message so you know what changes were made in this commit.

```bash
git commit -m "Your descriptive commit message here"
```
*   **Replace `"Your descriptive commit message here"`** with a brief summary of what you did (e.g., "Added Glossary and updated all documentation").

### 3. Push Your Changes (Send to GitHub)

This command sends your local commits from your `master` branch to your remote GitHub repository.

```bash
git push -u origin master
```
*   **Authentication:** When you run this, you will be prompted for your GitHub credentials in your terminal:
    *   **`Username for 'https://github.com':`** - Enter your GitHub username (`techboulnp-gif`).
    *   **`Password for 'https://techboulnp.github.com/YourRepositoryName.git':`** - **Paste your Personal Access Token (PAT)** here. (Input will be hidden).

---

## Troubleshooting Authentication (If `git push` Fails)

If `git push` fails with "Password authentication is not supported...", you need to use a Personal Access Token (PAT).

1.  **Generate/Verify PAT:**
    *   Go to GitHub.com -> Profile Picture -> Settings -> Developer settings -> Personal access tokens -> Tokens (classic).
    *   Or, use the newer "Fine-grained personal access tokens" interface as previously discussed (check `SOC_Project_Info/INSTRUCTIONS.md` for detailed steps on PAT creation).
    *   Ensure your PAT has **`repo`** scope (classic token) or **`Contents: Read and write`** permission (fine-grained token).
2.  **Use PAT as Password:** When `git push` prompts for a password, paste your PAT.

---

## Next Steps After Backup

After a successful push, you can view your updated project on GitHub.com.

Remember to commit and push regularly, especially after completing tasks or making significant progress!
