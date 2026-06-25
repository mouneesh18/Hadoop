import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv(
    'city_sales_results.txt',
    sep='\t',
    header=None,
    names=['City', 'TotalSales', 'TransactionCount']
)

print("\n=== SALES BY CITY SUMMARY ===")
print(df)

df['AvgTransaction'] = df['TotalSales'] / df['TransactionCount']

print("\n=== AVERAGE TRANSACTION VALUE BY CITY ===")
print(df[['City', 'AvgTransaction']].sort_values('AvgTransaction', ascending=False))

top_cities = df.nlargest(10, 'TotalSales')

plt.figure(figsize=(12, 6))
plt.bar(top_cities['City'], top_cities['TotalSales'] / 1_000_000)
plt.title('Top Cities by Total Sales')
plt.xlabel('City')
plt.ylabel('Sales (Million Rs.)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_analysis.png')

print("\nVisualization saved as sales_analysis.png")
