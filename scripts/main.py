import os

import pandas as pd

data = {
    "Invoice ID": [1, 2, 3, 4, 5],
    "Client Name": [
        "Ivan Petrov",
        "Maria Dimitrova",
        "Sofia Tech Ltd",
        "Georgi Ivanov",
        "Vasil Popov",
    ],
    "Issue Date": [
        "2025-01-01",
        "2025-01-05",
        "2025-01-10",
        "2025-01-12",
        "2025-01-15",
    ],
    "Due Date": ["2025-01-15", "2025-01-20", "2025-01-25", "2025-01-22", "2025-01-30"],
    "Amount (лв)": [500, 1200, 800, 300, 1500],
    "Payment Date": ["2025-01-14", "2025-01-25", None, "2025-01-21", None],
}

df = pd.DataFrame(data)

os.makedirs("data", exist_ok=True)

csv_path = os.path.join("data", "invoices.csv")
df.to_csv(csv_path, index=False)

print(f"CSV file saved at {csv_path}")
