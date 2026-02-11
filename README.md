# 🎂 Birthday Email Agent

An autonomous Python-based birthday notification agent that runs daily, identifies employees whose birthday is today, and sends personalized birthday emails.

The project is designed to be **safe by default**, easy to use, and production-ready, with real SMTP email support that can be enabled via configuration.

---

## ✅ What This Agent Does

* Runs once per day (manual or via scheduler/cron)
* Reads employee data from CSV → SQLite
* Finds employees whose birthday is today
* Generates personalized birthday emails

Supports:

* **Console mode** (safe / dry run)
* **SMTP mode** (real email sending via Gmail)

---

## 🧱 High-Level Design

The system is cleanly separated into layers:

* **Repository layer** – Handles all database access (SQLite)
* **Business logic layer** – Pure, testable functions for email content generation
* **Delivery layer** – Console output or real SMTP email sending
* **Orchestration layer** – Coordinates the daily agent run with logging and safety checks

This design makes the system easy to test, maintain, and extend.

---

## 📁 Project Structure

```
birthday-email-agent/
├── src/
│   ├── birthday_agent.py     # Main agent runner
│   ├── repository.py         # Database access
│   ├── email_sender.py       # SMTP email sender
│   ├── config.py             # Central configuration
│   ├── init_db.py            # CSV → SQLite initializer
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

> Note: The SQLite database file is generated locally and should not be committed to version control.

---

# ⚙️ Setup & Usage

---

## 1️⃣ Prerequisites

* Python 3.9+
* Internet connection (only required for SMTP mode)

---

## 2️⃣ Prepare Employee Data

Edit:

```
data/test_employees.csv
```

Required columns:

* `name`
* `email`
* `date_of_birth` (format: `YYYY-MM-DD`)

Example:

```
name,email,date_of_birth
Jane Doe,jane.doe@company.com,1992-04-15
John Smith,john.smith@company.com,1988-11-02
```

⚠️ Replace sample data with your own before enabling SMTP mode.

---

## 3️⃣ Initialize Database

From the project root directory:

```bash
python -m src.init_db
```

This creates a local SQLite database from the CSV file.

Each user should generate their own database locally.

---

# ▶️ Running the Agent (IMPORTANT)

---

## 🔹 Default Mode: Console (Safe Mode)

By default, the agent runs in console mode.

In:

```
src/config.py
```

Ensure:

```python
EMAIL_MODE = "console"
```

Run:

```bash
python -m src.birthday_agent
```

Result:

* Emails are printed to the terminal
* No real emails are sent
* Safe for testing and development

---

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

Google will display a 16-character password:

```
abcd efgh ijkl mnop
```

Copy this password (Ctrl + C).
You will not see it again.

---

## 3️⃣ Open PowerShell in the Project Root Directory

Navigate to your project folder (the folder containing `src/`, `data/`, etc.).

### Option A (Recommended)

1. Open File Explorer
2. Go to the `birthday-email-agent` folder
3. Click the address bar
4. Type:

```
powershell
```

5. Press Enter

PowerShell will open inside that directory.

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

In PowerShell, run:

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
* Do not include extra spaces
* Do not hardcode credentials in Python files

---

## 5️⃣ Restart PowerShell

Close PowerShell completely.
Open a new terminal window.

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

```bash
python -m src.birthday_agent
```

If configured correctly:

* Real birthday emails will be sent
* One email per matching employee
* Errors are logged in `logs/agent.log`

---

# 🛡️ Safety & Best Practices

* SMTP credentials are never committed to GitHub
* Console mode is the default
* Real emails are enabled only via configuration
* Database files should not be committed to version control

Recommended workflow:

1. Develop and test in console mode
2. Verify correct recipients
3. Switch to SMTP mode only after validation

---

# 🧪 Logging & Error Handling

All runs are logged to:

```
logs/agent.log
```

* Failures are handled gracefully
* Safe to run via Task Scheduler or cron
* Suitable for daily automated execution

---

# 🚀 Future Enhancements

* SMTP retry & alerting
* Email domain allow-list
* Dry-run + test override mode
* Scheduler integration examples
* Unit tests

---
