<<<<<<< HEAD
# ClinicQ: Hello, Flask

Starter Flask app for **CCC181 Week 2: Git, GitHub & Flask Foundations**.
It shows the project structure, routes, templates and static files from the slides.

## Project structure

```
my-app/
├── app.py              # creates the app and defines routes
├── requirements.txt    # packages to rebuild the environment
├── .gitignore          # keeps .venv, caches and secrets out of Git
├── .venv/              # your virtual environment (not committed)
├── templates/          # Jinja2 HTML files for render_template()
│   ├── base.html       # shared layout
│   ├── index.html      # home page
│   └── ticket.html     # page for /queue/<ticket_id>
└── static/             # served at /static/...
    ├── css/style.css
    └── js/main.js
```

## Routes

| URL | View function | What you see |
|---|---|---|
| `/` | `index()` | "Hello, Ana!" and a list of tickets, rendered with `index.html` |
| `/queue/<int:ticket_id>` | `ticket()` | A page for that ticket, e.g. `/queue/12` |
| `/hello` | `hello()` | The plain text "Hello, CCC181!" |

Try `/queue/abc`: the `int` converter only accepts numbers, so Flask returns 404.

## 1. Set up the Python environment

```bash
# create (once per project)
python -m venv .venv

# activate (every new terminal)
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux

# install the packages
pip install -r requirements.txt
```

Your prompt shows `(.venv)` when the environment is active. Some systems use `python3` or `py` instead of `python`.
If PowerShell blocks the activate script, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, or use Command Prompt.

If you add more packages later, record them with:

```bash
pip freeze > requirements.txt
```

## 2. Run the app

```bash
flask --app app run --debug
```

Open http://127.0.0.1:5000. With `--debug`, the server reloads every time you save a file. Never use debug mode in production.

## 3. Put it on GitHub

### Once per computer

```bash
git config --global user.name "Your Name"
git config --global user.email you@g.msuiit.edu.ph   # same email as your GitHub account
git config --list
```

### Create the local repository and first commit

```bash
git init
git branch -M main
git status              # .venv should NOT appear, thanks to .gitignore
git add .
git commit -m "Add Flask starter app"
```

### Connect to GitHub and push

1. On GitHub, create a new **empty** repository (no README, no .gitignore).
2. Copy its URL, then:

```bash
git remote add origin <repo-url>
git push -u origin main
```

GitHub does not accept your account password for Git over HTTPS. Sign in through Git Credential Manager or the GitHub CLI, or use a personal access token or SSH key.

### Everyday loop

```bash
git pull origin main     # before you start working
git status
git add <file>
git commit -m "Add join-queue form"
git push origin main     # when you have commits to share
```

## 4. Lab: ship it through a pull request

1. On GitHub, open an issue: **"Set up Flask starter app"**.
2. Pull the latest `main`, then create a branch:
   ```bash
   git switch main
   git pull origin main
   git switch -c feature/flask-setup
   ```
3. Create `.venv`, install Flask, write `requirements.txt` and `.gitignore`.
4. Build `app.py` with a home route and one dynamic route, rendered with `base.html` and `index.html`.
5. Commit in small steps, then push the branch:
   ```bash
   git push -u origin feature/flask-setup
   ```
6. On GitHub, click **Compare & pull request** and write `Closes #N` in the description (N is your issue number). Merge it, then:
   ```bash
   git switch main
   git pull origin main
   ```

**Early finishers:** add another static CSS rule linked with `url_for`, or a third route based on one Must feature from your project milestone.

## Commit message tips

- Short summary in the imperative: "Add...", "Fix..."
- One logical change per commit
- Commit early and often
- Good: "Add join-queue form". Unhelpful: "update", "asdf", "final na talaga".
=======
# Git Exercises

**Course:** CCC181  
**Student Name:** Cosning, Raven  
**Student ID:** 20240598  

## Activity Description

This folder contains my screenshot submissions for the assigned Git Exercises activity.

The Git exercises were completed through: [Git Exercises](https://gitexercises.fracz.com/)

My Git configuration uses my student ID number without the hyphen, as instructed.

## Submitted Screenshots

| Exercise No. | Exercise Title | Screenshot File |
|---|---|---|
| 01 | master | `cosning_Raven_01.png` |
| 02 | commit-one-file | `cosning_Raven_02.png` |
| 03 | commit-one-file-staged | `cosning_Raven_03.png` |
| 04 | ignore-them | `cosning_Raven_04.png` |
| 05 | chase-branch | `cosning_Raven_05.png` |
| 06 | merge-conflict | `cosning_Raven_06.png` |
| 07 | save-your-work | `cosning_Raven_07.png` |
| 08 | change-branch-history | `cosning_Raven_08.png` |
| 09 | remove-ignored | `cosning_Raven_09.png` |
| 10 | case-sensitive-filename | `cosning_Raven_10.png` |
| 11 | fix-typo | `cosning_Raven_11.png` |
| 12 | forge-date | `cosning_Raven_12.png` |
| 13 | fix-old-typo | `cosning_Raven_13.png` |
| 14 | commit-lost | `cosning_Raven_14.png` |
| 15 | split-commit | `cosning_Raven_15.png` |
| 16 | too-many-commits | `cosning_Raven_16.jpg` |
| 17 | executable | `cosning_Raven_17.jpg` |
| 18 | commit-parts | `cosning_Raven_18.jpg` |
| 19 | pick-your-features | `cosning_Raven_19.jpg` |
| 20 | rebase-complex | `cosning_Raven_20.jpg` |
| 21 | invalid-order | `cosning_Raven_21.jpg` |
| 22 | find-swearwords | `cosning_Raven_22.jpg` |
| 23 | find-bug | `cosning_Raven_23.jpg` |

## Folder Contents

```text
activities/git-exercises/
├── README.md
├── cosning_Raven_01.png
├── cosning_Raven_02.png
├── cosning_Raven_03.png
├── cosning_Raven_04.png
├── cosning_Raven_05.png
├── cosning_Raven_06.png
├── cosning_Raven_07.png
├── cosning_Raven_08.png
├── cosning_Raven_09.png
├── cosning_Raven_10.png
├── cosning_Raven_11.png
├── cosning_Raven_12.png
├── cosning_Raven_13.png
├── cosning_Raven_14.png
├── cosning_Raven_15.png
├── cosning_Raven_16.jpg
├── cosning_Raven_17.jpg
├── cosning_Raven_18.jpg
├── cosning_Raven_19.jpg
├── cosning_Raven_20.jpg
├── cosning_Raven_21.jpg
├── cosning_Raven_22.jpg
└── cosning_Raven_23.jpg
```

## Declaration

I confirm that the screenshots in this folder show my own completion or progress for the required Git Exercises activity.
>>>>>>> origin/main
