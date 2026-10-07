# Git Crash Course

## What is Git and Github?

Git- Distributed Version Control System (VCS) that helps developers track their codebase, collaborate with others and manage multiple versions of a project.

Remote repositories: Github, Gitlab, bitbucket.

Github- Web-based platform designed for version control and collaboration. It hosts git/remote respositories and provides a GUI within browser to manaage code and do other things.

Git is the Version Control System while Github is the platform that hosts git repositories. Other platforms include Gitlab, bitbucket.

Use Git via Terminal or GUI.


## Git Workflow

Local Machine (LM) and Remote  Repository (RR).

Local Machine has 3 stages:

-Working Directory: On your local machine, where you make changes to your files.

-Staging Area: Where you prepare your files for a commit.

-Local Repository: Where git stores all the changes to your files, stored in a hidden folder called .git in your pproject directory.

Remote Repository: Stored remote via Github, Gitlab etc. where people can pull code from.

Working Directory:LM (git init)--> Staging Area: LM (git add)--> Local Repo: LM (git commit)--> Remote Repo: RR (git push)

git init: Initialize a new reporsitory in your project folder in your working directory. idden folder called .git.

git add: To add some files to the staging area. i.e. [git add .] with the period, means add all.

git commit: Commit your to your local repositoy on your machine + a comment explaining what that commit is. git commit -m 'Add your commit comment'.

git push: Push your changes to your remote repo.

git pull: Pull changes from your remote repo to your working directory.

git clone: Clone repo on your local machine.

git status: check the status of your files.

git branch -M main

.gitignore: For things you have in your project you don't want to push to github or remote repo e.g. .env files which may contain API keys.


### Branching & Merging


Branching- allows you to work on a new feature without affect main code base, create a branch and merge the change via pull request.

U- means untracked and you've not added them to staging area.

A- Added to staging arrea.


### Some Git Command Shortcuts

Add and commit in a single task: <mark>git commit -am 'Add your commit comment'</mark>

Add and commit in a single task: <span style="color: red;">git add filename && git commit -m 'Add comment'</span>


## Getting Code from Github

Downloading: You can download a zip of your repo, likely if you don't want to make code changes.

Clone: Get a copy of the full repo on your machine.

git pull: Get the latest changes from a repo and merge into local branch/current working directory i.e. git fetch + git merge/rebase.

git fetch: pulls the latest changes from the remote repo without merging.It doesn't affect the local repository/local working directory.

forking: Copying a repository from github unto github into your account

git merge vs git rebase: Similar.

git rebase: Combines changes from one branch into another by moving your commits to the tip of the target branch.

## Branching and Merging

git checkout -b feature/login: Create and check out new branch.

git branch: See which branch you're on.  

git push -u origin feature/login : Push changes to the login feature branch.

git branch -d feature/login: delete branch

git merge feature/branch

git checkout [branch_name]: switching branches

git checkout [commit] [filename] or git checkout [filename]: Restoring a different version of a file.

git pull origin main

Vercel.com for CI/CD Pipelines










