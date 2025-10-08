# to check if table exist in this below file
import sqlite3

# Open  simulation_results.db file
conn = sqlite3.connect("simulation_results.db")
cursor = conn.cursor()

# all tables list
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in DB:", cursor.fetchall())

conn.close()
