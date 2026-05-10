











import pandas as pd


# 1. Text file se data read karein
# Note: Hum calls.txt se data filter karke list mein dalte hain
data = []
try:
    with open('calls.txt', 'r') as f:
        for line in f:
            # Data parsing logic
            if "number=" in line:
                parts = line.split(',')
                entry = {}
                for p in parts:
                    if '=' in p:
                        key, val = p.strip().split('=', 1)
                        entry[key] = val
                data.append(entry)

    # 2. Pandas DataFrame banayein
    df = pd.DataFrame(data)

    # 3. Excel file mein save karein
    output_file = "Mobile_Evidence_Report.xlsx"
    df.to_excel(output_file, index=False)
    print(f"Success! Report saved as {output_file}")

except Exception as e:
    print(f"Error: {e}")
