import os
import argparse
import pandas as pd
import psycopg2
from pathlib import Path

# Argument parser
parser = argparse.ArgumentParser(description="Export SQL query results to CSV files.")
parser.add_argument('--analysis', action='store_true', help="Export analysis SQL files")
parser.add_argument('--kpis', action='store_true', help="Export KPI SQL files")
args = parser.parse_args()

# Default: if no flag is passed, run both
if not args.analysis and not args.kpis:
    args.analysis = args.kpis = True

# Database connection parameters
db_params = {
    "dbname": "ecommerce_behavior",
    "user": "postgres",
    "host": "localhost",
    "port": 5432
}

# Connect to database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Helper function
def export_sql_dir(sql_path, output_path):
    sql_dir = Path(sql_path)
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    for sql_file in sql_dir.glob("*.sql"):
        with open(sql_file, "r") as f:
            query = f.read()

        try:
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=columns)

            output_csv = output_dir / f"{sql_file.stem}.csv"
            df.to_csv(output_csv, index=False)
            print(f"✅ Exported: {output_csv}")

        except Exception as e:
            print(f"❌ Error in {sql_file.name}: {e}")

# Export logic
if args.analysis:
    export_sql_dir("sql/analysis", "exports/tableau/analysis")
if args.kpis:
    export_sql_dir("sql/kpis", "exports/tableau/kpis")

cursor.close()
conn.close()