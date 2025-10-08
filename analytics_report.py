
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime
import os

# Connect to SQLite database
conn = sqlite3.connect("simulation_results.db")   # use same DB as main.py
df = pd.read_sql("SELECT * FROM results", conn)

print("Data loaded from DB:\n", df)

if df.empty:
    print("\n⚠️ No data found. Play some games first in main.py!")
else:
    # ----- BASIC STATS -----
    total_games = len(df)
    total_profit = df["outcome"].sum()
    win_rate = (df["outcome"] > 0).mean() * 100
    best_win = df["outcome"].max()
    worst_loss = df["outcome"].min()

    print("\n=== Descriptive Statistics ===")
    print(df["outcome"].describe())
    print(f"\nTotal games played: {total_games}")
    print(f"Net profit/loss: {total_profit}")
    print(f"Win rate: {win_rate:.2f}%")
    print(f"Best win: {best_win}")
    print(f"Worst loss: {worst_loss}")

    # ----- VISUALIZATIONS -----
    plt.figure(figsize=(12,5))

    # 1. Outcome distribution
    plt.subplot(1,2,1)
    df["outcome"].hist(bins=10, color="skyblue", edgecolor="black")
    plt.title("Outcome Distribution")
    plt.xlabel("Outcome")
    plt.ylabel("Frequency")

    # 2. Cumulative profit trend
    plt.subplot(1,2,2)
    df["cumulative_profit"] = df["outcome"].cumsum()
    plt.plot(df["id"], df["cumulative_profit"], marker="o", color="green")
    plt.title("Cumulative Profit Over Time")
    plt.xlabel("Game ID")
    plt.ylabel("Cumulative Profit")

    plt.tight_layout()
    plt.savefig("analytics_plots.png")   # one combined image
    plt.close()

    # ----- CREATE POLISHED PDF REPORT -----
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Game Simulation & Analytics Report", ln=True, align="C")

    pdf.set_font("Arial", "I", 12)
    pdf.cell(0, 10, "Automated reporting using Python, SQLite, Pandas, Matplotlib", ln=True, align="C")

    pdf.ln(10)

    # KPIs Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Key Metrics:", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Total games played: {total_games}", ln=True)
    pdf.cell(0, 10, f"Net profit/loss: {total_profit}", ln=True)
    pdf.cell(0, 10, f"Win rate: {win_rate:.2f}%", ln=True)
    pdf.cell(0, 10, f"Best win: {best_win}", ln=True)
    pdf.cell(0, 10, f"Worst loss: {worst_loss}", ln=True)

    pdf.ln(10)

    # Insert plots
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Visualizations:", ln=True)

    pdf.image("analytics_plots.png", x=10, y=None, w=190)

    pdf.ln(85)

    # Footer
    pdf.set_font("Arial", "I", 10)
    pdf.cell(0, 10, f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
    pdf.cell(0, 10, "Generated automatically using Python (pandas, matplotlib, FPDF)", ln=True, align="C")

    report_filename = "simulation_report.pdf"
    pdf.output(report_filename)

    print(f"\n✅ Polished PDF report saved as '{report_filename}'")

# Cleanup
if os.path.exists("analytics_plots.png"):
    os.remove("analytics_plots.png")

conn.close()



# import sqlite3
# import pandas as pd
# import matplotlib.pyplot as plt

# # Connect to (or create) SQLite DB
# conn = sqlite3.connect("simulation_results.db")
# cursor = conn.cursor()

# # 1. Create table if not exists
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS results (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     run_id INTEGER,
#     bet INTEGER,
#     outcome INTEGER
# )
# """)

# # 2. Insert some demo data if table is empty
# cursor.execute("SELECT COUNT(*) FROM results")
# if cursor.fetchone()[0] == 0:
#     demo_data = [
#         (1, 10, 20),
#         (1, 15, -10),
#         (2, 20, 30),
#         (2, 10, 5),
#         (3, 5, -5)
#     ]
#     cursor.executemany("INSERT INTO results (run_id, bet, outcome) VALUES (?, ?, ?)", demo_data)
#     conn.commit()

# # 3. Load into pandas DataFrame
# df = pd.read_sql("SELECT * FROM results", conn)
# print("Data loaded from DB:\n", df)

# # 4. Basic stats
# print("\nDescriptive Statistics:")
# print(df["outcome"].describe())

# # 5. Visualization
# plt.figure(figsize=(6,4))
# df["outcome"].hist(bins=10)
# plt.title("Outcome Distribution")
# plt.xlabel("Outcome")
# plt.ylabel("Frequency")
# plt.show()

# conn.close()

# import pandas as pd
# import sqlite3
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import os

# # Connect to SQLite database
# conn = sqlite3.connect("simulation_results.db")

# # Load data
# df = pd.read_sql("SELECT * FROM results", conn)
# print("Data loaded from DB:\n", df)

# if df.empty:
#     print("\n⚠️ No data found. Play some games first in main.py!")
# else:
#     # ----- BASIC STATS -----
#     print("\n=== Descriptive Statistics ===")
#     print(df["outcome"].describe())

#     # Extra insights
#     total_games = len(df)
#     total_profit = df["outcome"].sum()
#     win_rate = (df["outcome"] > 0).mean() * 100
#     best_win = df["outcome"].max()
#     worst_loss = df["outcome"].min()

#     print(f"\nTotal games played: {total_games}")
#     print(f"Net profit/loss: {total_profit}")
#     print(f"Win rate: {win_rate:.2f}%")
#     print(f"Best win: {best_win}")
#     print(f"Worst loss: {worst_loss}")

#     # ----- VISUALIZATIONS -----
#     plt.figure(figsize=(12,5))

#     # 1. Outcome distribution
#     plt.subplot(1,2,1)
#     df["outcome"].hist(bins=10, color="skyblue", edgecolor="black")
#     plt.title("Outcome Distribution")
#     plt.xlabel("Outcome")
#     plt.ylabel("Frequency")
#     plt.tight_layout()
#     plt.savefig("outcome_distribution.png")

#     # 2. Cumulative profit trend
#     plt.subplot(1,2,2)
#     df["cumulative_profit"] = df["outcome"].cumsum()
#     plt.plot(df["id"], df["cumulative_profit"], marker="o", color="green")
#     plt.title("Cumulative Profit Over Time")
#     plt.xlabel("Game ID")
#     plt.ylabel("Cumulative Profit")
#     plt.tight_layout()
#     plt.savefig("cumulative_profit.png")

#     plt.show()

#     # ----- CREATE PDF REPORT -----
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Slot Machine Simulation Report", ln=True, align="C")

#     pdf.set_font("Arial", "", 12)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Total games played: {total_games}", ln=True)
#     pdf.cell(0, 10, f"Net profit/loss: {total_profit}", ln=True)
#     pdf.cell(0, 10, f"Win rate: {win_rate:.2f}%", ln=True)
#     pdf.cell(0, 10, f"Best win: {best_win}", ln=True)
#     pdf.cell(0, 10, f"Worst loss: {worst_loss}", ln=True)

#     pdf.ln(10)
#     pdf.cell(0, 10, "Graphs:", ln=True)

#     # Insert the saved plot images
#     pdf.image("outcome_distribution.png", x=10, y=80, w=90)
#     pdf.image("cumulative_profit.png", x=110, y=80, w=90)

#     report_filename = "slot_machine_report.pdf"
#     pdf.output(report_filename)
#     print(f"\n✅ PDF report saved as '{report_filename}'")

# # Cleanup plots
# if os.path.exists("outcome_distribution.png"):
#     os.remove("outcome_distribution.png")
# if os.path.exists("cumulative_profit.png"):
#     os.remove("cumulative_profit.png")

# conn.close()

# import pandas as pd
# import sqlite3
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import os

# # Connect to SQLite database
# conn = sqlite3.connect("simulation_results.db")

# # Load data
# df = pd.read_sql("SELECT * FROM results", conn)
# print("Data loaded from DB:\n", df)

# if df.empty:
#     print("\n⚠️ No data found. Play some games first in main.py!")
# else:
#     # ----- BASIC STATS -----
#     print("\n=== Descriptive Statistics ===")
#     print(df["outcome"].describe())

#     # Extra insights
#     total_games = len(df)
#     total_profit = df["outcome"].sum()
#     win_rate = (df["outcome"] > 0).mean() * 100
#     best_win = df["outcome"].max()
#     worst_loss = df["outcome"].min()

#     print(f"\nTotal games played: {total_games}")
#     print(f"Net profit/loss: {total_profit}")
#     print(f"Win rate: {win_rate:.2f}%")
#     print(f"Best win: {best_win}")
#     print(f"Worst loss: {worst_loss}")

#     # ----- VISUALIZATIONS (combined) -----
#     plt.figure(figsize=(12,5))

#     # 1. Outcome distribution
#     plt.subplot(1,2,1)
#     df["outcome"].hist(bins=10, color="skyblue", edgecolor="black")
#     plt.title("Outcome Distribution")
#     plt.xlabel("Outcome")
#     plt.ylabel("Frequency")

#     # 2. Cumulative profit trend
#     plt.subplot(1,2,2)
#     df["cumulative_profit"] = df["outcome"].cumsum()
#     plt.plot(df["id"], df["cumulative_profit"], marker="o", color="green")
#     plt.title("Cumulative Profit Over Time")
#     plt.xlabel("Game ID")
#     plt.ylabel("Cumulative Profit")

#     plt.tight_layout()
#     combined_plot = "combined_plots.png"
#     plt.savefig(combined_plot)
#     plt.show()

#     # ----- CREATE PDF REPORT -----
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Simulation Results Report", ln=True, align="C")

#     pdf.set_font("Arial", "", 12)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Total games played: {total_games}", ln=True)
#     pdf.cell(0, 10, f"Net profit/loss: {total_profit}", ln=True)
#     pdf.cell(0, 10, f"Win rate: {win_rate:.2f}%", ln=True)
#     pdf.cell(0, 10, f"Best win: {best_win}", ln=True)
#     pdf.cell(0, 10, f"Worst loss: {worst_loss}", ln=True)

#     pdf.ln(10)
#     pdf.cell(0, 10, "Graphs:", ln=True)

#     # Insert combined image
#     pdf.image(combined_plot, x=10, y=100, w=190)

#     report_filename = "simulation_report.pdf"
#     pdf.output(report_filename)
#     print(f"\n✅ PDF report saved as '{report_filename}'")

# # Cleanup plot
# if os.path.exists(combined_plot):
#     os.remove(combined_plot)

# conn.close()