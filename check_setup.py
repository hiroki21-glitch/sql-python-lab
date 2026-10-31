import sys
import duckdb
import pandas as pd

print("Python      :", sys.version.split()[0])
print("Interpreter :", sys.executable)  # must point inside .venv
print("DuckDB      :", duckdb.__version__)
print("pandas      :", pd.__version__)

df = duckdb.sql("SELECT 'setup' AS step, 'ok' AS status").df()
print(df)
