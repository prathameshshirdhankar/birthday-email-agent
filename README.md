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

### Step 1️⃣ Generate Gmail App Password

* Enable 2-Step Verification on your Google account
* Generate an **App Password** for Mail

---

### Step 2️⃣ Set environment variables (Windows PowerShell)

```powershell
setx SMTP_USERNAME "yourgmail@gmail.com"
setx SMTP_PASSWORD "your_app_password"
```

Restart the terminal after this.

---

### Step 3️⃣ Switch to SMTP mode

In `src/config.py`, change:

```python
EMAIL_MODE = "smtp"
```

⚠️ This is the **only change required** to enable real emails.

---

### Step 4️⃣ Run the agent

```bash
python -m src.birthday_agent
```

Result:

* Real birthday emails are sent via Gmail SMTP
* One email per user
* Failures are logged safely

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
