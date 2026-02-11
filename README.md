🎂 Birthday Email Agent

An autonomous Python-based birthday notification agent that runs daily, identifies employees whose birthday is today, and sends personalized birthday emails.

The project is designed to be **safe by default**, **easy to use**, and **production-ready**, with real SMTP email support that can be enabled via configuration.

---

## ✅ What This Agent Does

* Runs once per day (manual or scheduler/cron)
* Reads employee data from CSV → SQLite
* Finds employees whose birthday is **today**
* Generates personalized birthday emails
* Supports:

  * **Console mode** (safe / dry run)
  * **SMTP mode** (real email sending via Gmail)

---

## 🧱 High-Level Design

The system is cleanly separated into layers:

* **Repository layer**
  Handles all database access (SQLite).

* **Business logic layer**
  Pure, testable functions for email content generation.

* **Delivery layer**
  Console output or real SMTP email sending.

* **Orchestration layer**
  Coordinates the daily agent run with logging and safety checks.

This makes the system easy to test, maintain, and extend.

---

## 📁 Project Structure

```
birthday-email-agent/
├── src/
│   ├── birthday_agent.py     # Main agent runner
│   ├── repository.py         # Database access
│   ├── email_sender.py       # SMTP email sender
│   ├── config.py             # Central configuration
│   └── __init__.py
│
├── data/
│   └── test_employees.csv    # Employee data
│
├── logs/
│   └── (created at runtime)  # Execution logs
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Usage

### 1️⃣ Prerequisites

* Python 3.9+
* Internet connection (only for SMTP mode)

---


# 🗄️ Database Configuration (Important)

This project uses a local **SQLite database** generated from a CSV file.

⚠️ The provided example database and CSV contain test data.
You should use your own employee dataset before enabling SMTP mode.

---

## How the Database Works

1. Employee data is stored in:

```
data/test_employees.csv
```

2. The database is generated from this CSV file:

```bash
python -m src.init_db
```

3. This creates a local SQLite database file (e.g., `employees.db`).

---

## ✅ Use Your Own Employee Data

Before running in SMTP mode:

1. Open:

```
data/test_employees.csv
```

2. Replace the example data with your own:

Required columns:

```
name,email,date_of_birth
```

Example:

```
Jane Doe,jane.doe@yourcompany.com,1992-04-15
John Smith,john.smith@yourcompany.com,1988-11-02
```

3. Rebuild the database:

```bash
python -m src.init_db
```

This ensures:

* The SQLite database reflects your employee list
* Emails are sent to your intended recipients
* No test emails are accidentally triggered

---

## 🔐 Important Safety Note

If you do not replace the sample data:

* The agent may send emails to example/test addresses
* This could result in unintended email delivery

Always verify your CSV before enabling:

```python
EMAIL_MODE = "smtp"
```

---

## 💡 Recommended Practice

* Use console mode first:

```python
EMAIL_MODE = "console"
```

* Verify correct recipients are printed
* Then switch to SMTP mode

---

# Optional Improvement (Highly Recommended)

You should **not commit `employees.db` to GitHub**.

Add this to your `.gitignore`:

```
*.db
```

That way:

* Each user generates their own database locally
* No personal data is stored in the repository
* The project looks more professional

---

# Even Better (If You Want It Cleaner)

Instead of shipping a real DB, you can:

* Delete `employees.db` from the repo
* Keep only:

  * `data/test_employees.csv`
* Add a note:

  > “Database file is generated locally and not included in version control.”

That’s how production tools handle this.

---




### 2️⃣ Prepare employee data

Edit:

```
data/test_employees.csv
```

Required columns:

* `name`
* `email`
* `date_of_birth` (YYYY-MM-DD)

---

### 3️⃣ Initialize database

From the project root:

```bash
python -m src.init_db
```

This creates a local SQLite database from the CSV.

---

## ▶️ Running the Agent (IMPORTANT)

### 🔹 Default Mode: Console (Safe)

By default, the agent runs in **console mode**.

In `src/config.py`:

```python
EMAIL_MODE = "console"
```

Run:

```bash
python -m src.birthday_agent
```

Result:

* Emails are **printed to the terminal**
* No real emails are sent
* Safe for testing and demos

---

## ✉️ Enabling Real Email Sending (SMTP)

SMTP is **already implemented and tested**, but disabled by default.



# ✉️ Enabling Real Email Sending (SMTP – Gmail)

SMTP support is fully implemented but disabled by default.

Follow these steps carefully.

---

## 1️⃣ Enable 2-Step Verification

1. Go to your Google Account → **Security**
2. Enable **2-Step Verification**

⚠️ Required before generating App Passwords.

---

## 2️⃣ Generate a Gmail App Password

1. Go to **Google Account → Security → App passwords**
2. Select:

   * **App:** Mail
   * **Device:** Windows Computer (or Other)
3. Click **Generate**
4. Google will display a 16-character password

Example:

```
abcd efgh ijkl mnop
```

Copy this password (Ctrl + C).
You will not see it again.

---

## 3️⃣ Open PowerShell in the Project Root Directory

Navigate to your project folder (the folder containing `src/`, `data/`, etc.).

Example structure:

```
birthday-email-agent/
├── src/
├── data/
├── logs/
```

### Option A (Recommended)

1. Open File Explorer
2. Go to the `birthday-email-agent` folder
3. Click the address bar
4. Type:

```
powershell
```

5. Press Enter

PowerShell will open **inside that directory**.

---

### Option B (Manual Navigation)

Open PowerShell normally, then run:

```powershell
cd path\to\birthday-email-agent
```

Example:

```powershell
cd C:\Users\YourName\Documents\birthday-email-agent
```

---

## 4️⃣ Set Environment Variables

In PowerShell (inside the project directory), run:

```powershell
setx SMTP_USERNAME "yourgmail@gmail.com"
```

Press Enter.

Then run:

```powershell
setx SMTP_PASSWORD "PASTE_YOUR_APP_PASSWORD_HERE"
```

Now:

* Delete `PASTE_YOUR_APP_PASSWORD_HERE`
* Press **Ctrl + V** to paste your copied App Password
* Press Enter

Example:

```powershell
setx SMTP_PASSWORD "abcdefghijklmnop"
```

You should see:

```
SUCCESS: Specified value was saved.
```

⚠️ Important:

* Use the App Password (NOT your real Gmail password)
* Do not add extra spaces
* Do not hardcode credentials in Python files

---

## 5️⃣ Restart PowerShell

Close PowerShell completely.
Open a new PowerShell window.

Environment variables will not load until restarted.

---

## 6️⃣ Enable SMTP Mode

Open:

```
src/config.py
```

Change:

```python
EMAIL_MODE = "console"
```

To:

```python
EMAIL_MODE = "smtp"
```

---

## 7️⃣ Run the Agent

From the project root directory:

```powershell
python -m src.birthday_agent
```

If configured correctly:

* Real birthday emails will be sent
* One email per matching employee
* Errors are logged in `logs/agent.log`

---



## 🛡️ Safety & Best Practices

* SMTP credentials are **never committed** to GitHub
* Console mode is the default
* Real emails are enabled only via config
* Recommended:

  * Test SMTP with your own email first
  * Use console mode when making changes

---

## 🧪 Logging & Error Handling

* All runs are logged to:

  ```
  logs/agent.log
  ```
* Failures are handled gracefully
* Safe to run via Task Scheduler / cron

---

## 🚀 Future Enhancements

* SMTP retry & alerting
* Email domain allow-list
* Dry-run + test override mode
* Scheduler integration
* Unit tests

---
