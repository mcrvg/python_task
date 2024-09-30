# Git learning

**cd** -->open folders if there are space in the name folder we have to use "
**ls** -->list files 
**pwd** --> where are we right now?

# CORE COMMANDS 
git init: Initializes a new Git repository in the current directory.
git clone: Creates a local copy of a remote Git repository.
git add: Stages changes for inclusion in the next commit.
git commit: Creates a new commit with the staged changes.
git status: Shows the current status of the working directory and staging area.
git log: Displays the commit history of the repository.

# Steps GitHub
echo "# tech-264-git" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mcrvg/.....
git push -u origin main

# Branching and Merging:
git branch: Creates, lists, or deletes branches.
git checkout: Switches to a different branch.
git merge: Merges changes from one branch into another.

# Remote Repositories:
git remote: Manages remote repositories associated with the local repository.
git push: Pushes commits to a remote repository.
git pull: Fetches changes from a remote repository and merges them into the current branch.   

# Other Useful Commands:
git diff: Shows the differences between files or commits.
git reset: Undoes changes or commits.
git revert: Reverses the effect of a specific commit.
git tag: Creates tags to mark specific points in the repository's history.


# create new file named: .gitignore in pycharm
#We want to delete .idea/ folder from our remote repository (GitHub)
TERMINAL
--> git add .
--> git commit -m "Add .gitignore file"

### remove a file you don't want to commit

- .gitignore file = allows anything in the folder to be ignored during a git commit and push
EXAMPLES:
  - eg. sensitive information (personal files, credentials and passwords)
  - very large files or folders that don't need to be pushed
  - folders that build up (bin, out, etc)
  - hidden system files
 
-.idea (your pycharm settings) can be added to .gitignore
  - open a .gitignore repo and add: .idea/
TERMINAL:
--> git rm --cached .idea :Do not remove
-->git rm --cached -r .idea :Now everything inside the folder is deleted
-->git status: changes to be commit
-->git commit -m "Remove .idea folder recursively"
-->git push
##now is gone

Doing that avibe, the file is still available if the push is public as people can just go 
back to previous commit and see that file
# IF YOU PUSH PERSONAL CREDENTIALS ON A PUBLIC REPO TO GITHUB :
  - OPTION 1 "git reset", removes previous commit with that file DANGEROUS - CAN LOSE WORK
  - OPTION 2 
    - remove the GitHub repo IMMEDIATELY (you are now safe)
    - remove the sensitive information from your local repo
    - git remove the commit history, remove the .git folder, you will the latest files, but no history of past commits