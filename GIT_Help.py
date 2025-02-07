##############################################
#                Git Commands Tutorial       #
##############################################

# 🚀 Initialize a new Git repository
# -----------------------------------
# git init
# This command initializes a new Git repository in the current directory.

# 🔍 Check the status of the repository
# -------------------------------------
# git status
# Shows the current state of the working directory and staging area.

# 📂 Add files to the staging area
# --------------------------------
# git add <file_name>
# Stages a specific file.
# Example: git add main.py

# 🗂️ Add all files to the staging area
# ------------------------------------
# git add .
# Stages all modified and untracked files.

# ✅ Commit changes with a message
# --------------------------------
# git commit -m "Your commit message"
# Saves the staged changes with a description.

# 📜 View commit history
# ----------------------
# git log
# Displays commit history with details such as author, date, and commit message.

# 🔄 Push changes to a remote repository
# --------------------------------------
# git push origin <branch_name>
# Uploads the local commits to the specified remote branch.
# Example: git push origin main

# 🔄 Pull latest changes from a remote repository
# ----------------------------------------------
# git pull origin <branch_name>
# Fetches and merges changes from the remote repository.

# 📥 Clone a repository
# ---------------------
# git clone <repository_url>
# Copies a remote repository to the local machine.

# 🌿 Create a new branch
# ----------------------
# git branch <branch_name>
# Creates a new branch without switching to it.

# 🔀 Switch to another branch
# ---------------------------
# git checkout <branch_name>
# Switches to the specified branch.

# 🌱 Create and switch to a new branch
# ------------------------------------
# git checkout -b <branch_name>
# Creates a new branch and switches to it immediately.

# 🔗 Merge a branch into the current branch
# -----------------------------------------
# git merge <branch_name>
# Merges the specified branch into the current branch.

# 🗑️ Delete a branch
# ------------------
# git branch -d <branch_name>
# Deletes the specified branch.

# 📦 Stash changes
# ----------------
# git stash
# Temporarily saves uncommitted changes.

# 🎯 Apply stashed changes
# ------------------------
# git stash pop
# Restores the most recent stash and removes it from the stash list.

# 📜 View stashed changes
# ------------------------
# git stash list
# Displays a list of stashed changes.

# ❌ Remove a specific stash
# --------------------------
# git stash drop <stash_id>
# Removes a specific stash from the list.

# 🔄 Reset changes
# ----------------
# git reset --hard <commit_id>
# Resets the repository to a specific commit and removes all changes.

# 🔙 Revert a commit
# ------------------
# git revert <commit_id>
# Creates a new commit that undoes the changes of a specified commit.

# 🛠️ Configure Git User Info
# --------------------------
# git config --global user.name "Your Name"
# git config --global user.email "your.email@example.com"
# Sets your name and email for commits.

# 🔗 View Remote Repositories
# ---------------------------
# git remote -v
# Lists the remote repositories linked to the local repo.

# 🔄 Rename a Branch
# ------------------
# git branch -m old-branch new-branch
# Renames the branch from old-branch to new-branch.

# ❌ Delete a Remote Branch
# -------------------------
# git push origin --delete branch-name
# Deletes the specified branch from the remote repository.

# 🔍 Show Changes in a File
# -------------------------
# git diff file-name
# Shows differences between the working file and the last commit.

# 🛠️ Rebase a Branch
# ------------------
# git rebase branch-name
# Moves your branch's commits on top of another branch.

# ⏪ Undo Last Commit (Keep Changes)
# ----------------------------------
# git reset --soft HEAD~1
# Moves the last commit to the staging area but keeps the changes.

# 🛑 Undo Last Commit (Discard Changes)
# -------------------------------------
# git reset --hard HEAD~1
# Completely removes the last commit and its changes.

# 🏷️ Tagging a Commit
# --------------------
# git tag -a v1.0 -m "Version 1.0 release"
# Tags a commit with a version identifier.

# 🔍 Show Commit Details
# ----------------------
# git show commit-id
# Shows detailed information about a specific commit.

##############################################
#           End of Git Commands Guide       #
##############################################
