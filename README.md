# TrimLine

TrimLine is a queue app for a walk-in barbershop with several barbers. Customers join the queue from their phone, see their ticket number and how many people are ahead, and the barber uses a staff dashboard to call the next customer and mark them as served or no-show. Built for CCC181 Week 3 with Flask, Jinja and Bootstrap.

## Screens

| URL | Used by | What it shows |
|---|---|---|
| `/` | Customer | Home page |
| `/join` | Customer | Join the queue form |
| `/queue/<ticket number>` | Customer | My place: ticket number, status and people ahead, refreshed every 10 seconds |
| `/staff` | Barber | Waiting list in order, with Call next, Call, Serve and No-show |

## How to run

Requires Python 3.11 or newer.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
flask --app app run --debug
```

Open http://127.0.0.1:5000.

## Notes

- The staff dashboard has no login yet. Login comes in a later week.
- Tickets are kept in a Python list in memory, so they reset when the server restarts. They move to PostgreSQL in Week 4.

## Documents

- Personas: [docs/week3/personas.md](docs/week3/personas.md)

## Other work in this repo

- Git Exercises: [activities/git-exercises](activities/git-exercises), described below.

---

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