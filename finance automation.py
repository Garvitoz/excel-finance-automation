import pandas as pd

# This script automates a basic monthly finance report
# It reads data from an Excel file and creates a summary sheet

def generate_report(file_name):
    try:
        df = pd.read_excel(file_name)

        # Basic calculations
        df['Net'] = df['Revenue'] - df['Expenses']

        # Group by category to get total profit/loss
        summary = df.groupby('Category')['Net'].sum().reset_index()

        # Export summary to Excel
        output_file = "monthly_summary.xlsx"
        summary.to_excel(output_file, index=False)

        print(f"\n✅ Report created successfully: {output_file}")
        print("\n--- Preview ---")
        print(summary.head())

    except Exception as e:
        print("❌ Something went wrong:", e)


if __name__ == "__main__":
    print("📊 Excel Finance Automation")
    print("---------------------------")
    generate_report("sample_data.xlsx")
