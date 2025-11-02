# chunk_and_generate_copy_cmds.py

import csv
import os

# === CONFIG ===
CHUNK_SIZE = 500_000
INPUT_CSV_PATH = "data/data-cleaned/behavior-data/2019-Oct-cleaned.csv"
OUTPUT_DIR = "data/data-chunks/oct"
SUPABASE_TABLE = "user_behavior_oct"
CSV_FILENAME_PREFIX = "part_chunk_"

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def split_csv():
    print(f"Reading from: {INPUT_CSV_PATH}")
    columns = None
    rows_written = 0
    chunk_index = -1
    writer = None
    outfile = None

    with open(INPUT_CSV_PATH, newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        columns = next(reader)

        for row in reader:
            if rows_written % CHUNK_SIZE == 0:
                if outfile:
                    outfile.close()
                chunk_index += 1
                filename = f"{CSV_FILENAME_PREFIX}{chunk_index:03}.csv"
                path = os.path.join(OUTPUT_DIR, filename)
                outfile = open(path, "w", newline="", encoding="utf-8")
                writer = csv.writer(outfile)
                writer.writerow(columns)
                print(f"✅ Saved chunk: {path}")
            writer.writerow(row)
            rows_written += 1

    if outfile:
        outfile.close()

    return columns


def build_column_clause(columns):
    if not columns:
        raise ValueError("No columns were detected from the source CSV.")
    
    joined_columns = ", ".join(columns)
    return f"({joined_columns})"

def generate_copy_commands(columns):
    print("\n📋 COPY Commands for Supabase (run in psql):\n")
    abs_path = os.path.abspath(OUTPUT_DIR)
    column_clause = build_column_clause(columns)
    
    for file in sorted(os.listdir(OUTPUT_DIR)):
        if file.startswith(CSV_FILENAME_PREFIX) and file.endswith(".csv"):
            full_path = os.path.join(abs_path, file)
            print(f"\\COPY {SUPABASE_TABLE} {column_clause} FROM '{full_path}' WITH (FORMAT csv, HEADER true);")

def main():
    ensure_output_dir()
    columns = split_csv()
    generate_copy_commands(columns)
    print("\n✅ All done.")

if __name__ == "__main__":
    main()
