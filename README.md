# PythonCodeCraftArena
Flask Challenge Hub

-Browse programming challenges

-Solve them in a browser

-Submit their code

-Get feedback or automated output

-Track progress

Think of it as your personal custom-built "LeetCode".

A Flask-powered web platform where users can browse, solve, and track Python programming challenges. Built to showcase practical Python skills for interviews and personal learning.

## Getting Started

```bash
git clone <your-repo-url>
cd your-project-folder

in project root open new folder named instance
in the folder instance open new file named config.py
in it paste the following code:
    SQLALCHEMY_DATABASE_URI = "sqlite:///arena.db"

    DEBUG = True
    SECRET_KEY = 'your-secret-key'

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

python run.py