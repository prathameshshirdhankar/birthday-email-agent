# Birthday Email Agent

An autonomous birthday notification agent that runs daily, identifies employees whose birthday is on the current date, and generates personalized birthday messages.

The project is intentionally designed to be **clean, portable, robust, and testable**, with email delivery simulated and abstracted for future production integration.

---

## Key Features

* Runs as a **daily autonomous agent**
* Fetches only employees whose birthday is **today**
* Generates **personalized, professional birthday messages**
* Designed with **clear separation of concerns**
* Robust error handling and structured logging
* OS-agnostic and portable (no hardcoded paths)
* Email delivery abstracted for easy future integration (SMTP / third-party services)

---

## Architecture Overview

The system is structured into clear layers:

* **Repository layer**
  Handles all data access (SQLite) and is isolated from business logic.

* **Business logic layer**
  Pure functions for message generation (fully testable, no side effects).

* **Orchestration layer**
  Coordinates execution, logging, and delivery.

This design allows easy extension, testing, and maintenance without changing core logic.

---

## 📁 Project Structure

```
birthday-email-agent/
├── src/
│   ├── birthday_agent.py     # Orchestration & delivery logic
│   ├── repository.py         # Data access layer
│   ├── config.py             # Centralized configuration & paths
│   └── __init__.py
│
├── data/
│   └── test_employees.csv    # Input employee data (CSV)
│
├── logs/
│   └── (created at runtime)  # Runtime logs (ignored by Git)
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuration

All paths and constants are centrally managed in:

```
src/config.py
```

This ensures:

* no hardcoded OS-specific paths
* easy portability across environments
* clean separation between configuration and logic

---

## ▶️ How to Run

### 1️⃣ Prerequisites

* Python 3.9+
* No external dependencies required

### 2️⃣ Prepare data

Update employee records in:

```
data/test_employees.csv
```

Required columns:

* `name`
* `email`
* `date_of_birth` (YYYY-MM-DD)

---

### 3️⃣ Initialize the database

From the project root:

```bash
python -m src.init_db
```

This creates a local SQLite database from the CSV.

---

### 4️⃣ Run the agent

```bash
python -m src.birthday_agent
```

Output:

* Birthday messages printed to console
* Execution details logged to `logs/agent.log`

---

## 🛡️ Robustness & Error Handling

The agent is designed to **fail gracefully**:

* Missing or empty CSV files are detected early
* Database errors are logged with stack traces
* The agent never crashes silently
* Safe to run via scheduler / cron jobs

---

## 📬 Email Delivery (Design Choice)

Actual email delivery is **intentionally simulated**.

Reason:

* Real email delivery introduces security, credentials, retries, and monitoring concerns.
* The system is architected so email delivery can be added later **without changing core logic**.

Supported future extensions:

* SMTP
* Company email services
* Third-party providers (e.g. SendGrid, SES)

---

## 🧪 Testability

* Business logic is implemented as **pure functions**
* Data access is isolated behind a repository layer
* Components can be unit tested independently without a real database or email service

---

Future Enhancements

* Add real email delivery via SMTP or third-party service
* Introduce unit tests for business logic
* Add retry and alerting mechanisms
* Package as a standalone executable

