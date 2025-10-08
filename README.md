# Python-Based Slot Machine Analytics

---
## Overview

This is a simulation-based project that integrates gameplay, database persistence, analytics, and automated reporting into a complete end-to-end pipeline. It’s about showcasing **how simulations can generate real-time data that is later stored, analyzed, visualized, and transformed into professional reports**. Here outcomes are logged into a database, analyzed with Python libraries, and finally converted into a polished PDF report with visual insights.

## Features
-  **Simulation Engine** – Runs slot machine spins with configurable symbols & payouts.  
-  **Persistent Storage (SQLite)** – Automatically logs every spin result for historical analysis.  
-  **Data Analytics (Pandas)** – Provides insights into wins/losses, trends, and cumulative performance.  
-  **Visualizations (Matplotlib)** – Graphs to illustrate session outcomes and long-term statistics.  
-  **Automated Reporting (FPDF)** – Generates polished PDF reports with stats and charts.  
-  **Optional GUI (Tkinter/PyQt)** – Interactive play mode (work in progress).  

---

## Tech Stack
- **Language**: Python 3  
- **Libraries**: `random`, `time`, `sqlite3`, `pandas`, `matplotlib`, `fpdf`, `colorama`, `json`, `tkinter/pyqt`  

---

## Project Structure
- ├── simulation_engine.py   # Slot machine simulation + DB logging
- ├── analytics_report.py    # Data analytics + PDF report generator
- ├── simulation_results.db  # SQLite database (auto-created)
- ├── simulation_report.pdf  # Generated PDF report
- └── README.md              # Project documentation

---

##  Workflow

1. **Run the simulation engine** (`simulation_engine.py`) → executes multiple runs and logs results into the database.  
2. **Generate analytics** using (`analytics_report.py`) → analyzes stored data, creates visualizations, and builds a PDF report.  
3. **Review results** → the generated PDF provides summarized performance trends and visual insights.  

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/via23-ma/Simulytics.git
cd Simulytics

# Run the simulation engine
python simulation_engine.py

# Generate analytics report
python analytics_report.py.
```
---

## Example Output

- Session results stored in **simulation_results.db**
- Trend graphs of winnings vs. losses
- Automated PDF reports summarizing performance

---

## Future Enhancements

 - Live dashboard with Streamlit/Flask.
 - Add ML models for prediction on outcomes.
 - Auto-generate report after each simulation run.

---

## Repository

 **https://github.com/via23-ma/Simulytics**

 







