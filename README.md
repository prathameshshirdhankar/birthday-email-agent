# Birthday Email AI Agent

This project implements an autonomous AI agent that runs once per day to identify employees whose birthday is today and send them a personalized birthday email.

## Current Features
- Daily execution (once per day)
- Optimized SQLite query (no full table scans)
- Individual personalized emails
- Professional email template (TestOrg)
- Logging for traceability
- Email simulation for safe testing

## Architecture
The system uses:
- Python-based agent logic
- SQLite as a lightweight database
- OS-level scheduler for daily execution
- Modular email layer (simulated now, real SMTP later)

## Current Status
Email delivery is simulated for validation. The same logic can be integrated with a real company email service without changes to the core agent.

## Next Steps
- Integrate company SMTP / Outlook API
- Deploy as background service
- Enhance email personalization
