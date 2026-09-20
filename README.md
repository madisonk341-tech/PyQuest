# PyQuest

A Duolingo-style web app for learning Python, built around an intro engineering-programming
course. Login → **Learning** (module path with lessons, practice questions, and a quiz per
module) → **Practice** (custom quizzes, full practice exams, and a "weak areas" quiz built from
questions you've missed) → **Sandbox** (write and run real Python in the browser, no server
needed, via Pyodide).

Works on phone and laptop browsers — it's a website, not an installed app.

## Status

The framework (auth, progress tracking, quizzes, exams, sandbox) is fully built and wired up
end-to-end. **Modules 1–3** have complete lesson content (explanations, examples, practice
questions, quiz, and sandbox prompts) as a full vertical slice. **Modules 4–13** appear on the
map (per the course's 13-module syllabus) but are locked/"coming soon" until their content is
written — see `backend/content_data.py`, `MODULE_CONTENT` / `PRACTICE_POOLS` / `SANDBOX_PROMPTS`.

## Stack

- **Backend:** Flask + SQLAlchemy + SQLite. Session-cookie auth (passwords hashed with
  Werkzeug). Serves a JSON API under `/api/*`, and in production also serves the built React app.
- **Frontend:** React + TypeScript + Vite + Tailwind CSS v4.
- **Sandbox:** [Pyodide](https://pyodide.org) (real Python compiled to WebAssembly) runs
  entirely in the visitor's browser — no code is ever executed on the server.

## Local development

You need Node.js and Python 3 installed.

**1. Backend** (in one terminal):

```bash
cd backend
python -m venv venv
./venv/Scripts/pip install -r requirements.txt   # macOS/Linux: venv/bin/pip
./venv/Scripts/python app.py                     # macOS/Linux: venv/bin/python app.py
```

Runs on `http://127.0.0.1:5000`.

**2. Frontend** (in another terminal):

```bash
cd frontend
npm install     # also copies the Pyodide runtime into public/pyodide
npm run dev
```

Runs on `http://localhost:5173` and proxies `/api/*` to the Flask backend — open this URL.

## Production build (single deploy)

Flask serves the built frontend directly, so there's only one thing to host:

```bash
cd frontend
npm install
npm run build          # outputs frontend/dist
cd ../backend
./venv/Scripts/pip install -r requirements.txt
./venv/Scripts/python app.py   # or use a WSGI server (see below) pointing at wsgi:app
```

Visit `http://127.0.0.1:5000` — it now serves both the API and the app.

## Deploying for free (PythonAnywhere)

SQLite needs **persistent disk**, which most free hosts wipe on restart — PythonAnywhere's free
tier persists your files, so it's a good fit here.

1. Push this repo to GitHub (see below).
2. On PythonAnywhere: **Consoles → Bash**, then `git clone` your repo.
3. `cd PyQuest/frontend && npm install && npm run build` (PythonAnywhere consoles have Node
   available; if not, build locally and `git push` the `frontend/dist` folder instead — you'll
   need to remove `frontend/dist` from `.gitignore` if you go that route).
4. `cd ../backend && pip install --user -r requirements.txt`
5. **Web** tab → **Add a new web app** → Manual configuration → Python 3.10+.
6. Set the **Source code** directory to `.../PyQuest/backend` and edit the **WSGI configuration
   file** it gives you so it imports your app:
   ```python
   import sys
   path = '/home/yourusername/PyQuest/backend'
   if path not in sys.path:
       sys.path.append(path)
   from wsgi import app as application
   ```
7. Set `PYQUEST_SECRET_KEY` as an environment variable (Web tab → "Environment variables") to a
   random secret string instead of the `dev-secret-change-me` default.
8. Reload the web app. Your site is live at `yourusername.pythonanywhere.com`.

To ship updates later: `git pull` inside the PythonAnywhere console, rebuild the frontend if it
changed, then hit **Reload** on the Web tab.

## Pushing to GitHub

```bash
git init
git add .
git commit -m "Initial PyQuest scaffold"
gh repo create PyQuest --private --source=. --remote=origin
git push -u origin main
```

## Project layout

```
backend/
  app.py              Flask app factory
  models.py            SQLAlchemy models (User, progress, quiz results, attempts)
  auth.py               Register / login / logout / me
  routes_content.py     Module content, component/quiz completion, progress summary
  routes_practice.py    Custom quizzes, Exam 1 / Exam 2, weak-areas quiz, grading
  routes_sandbox.py     Sandbox coding-prompt search
  content_data.py       All course content lives here (edit this to add modules 4-13)
frontend/
  src/pages/            Login, Learning, ModuleDetail, Practice, Sandbox
  src/components/       PathMap, ModuleNode, CodeBlock, ChoiceList, nav
  src/lib/pyodideRunner.ts   In-browser Python execution
  src/context/AuthContext.tsx
  public/pyodide/       Pyodide WASM runtime (auto-copied by `npm install`, gitignored)
```

## Adding the remaining modules (4–13)

Everything is data-driven from `backend/content_data.py`:

1. Add the module's id to `MODULES_WITH_CONTENT`.
2. Add an entry to `MODULE_CONTENT[id]` with `components` (each with `explanation`, `examples`,
   `practice`) and a `quiz` list — follow the shape of modules `"1"`–`"3"`.
3. Add a larger, differently-worded question set to `PRACTICE_POOLS[id]` for the Practice tab.
4. Optionally add entries to `SANDBOX_PROMPTS` with that module's `module_id`.

No frontend changes are needed — the UI renders whatever content the API returns.
