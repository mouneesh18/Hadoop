#!/usr/bin/env python3
import sys

current_month = None
total_sales = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    month, amount = line.split('\t')
    amount = float(amount)

    if month == current_month:
        total_sales += amount
    else:
        if current_month is not None:
            print(f"{current_month}\t{total_sales:.2f}")

        current_month = month
        total_sales = amount

if current_month is not None:
    print(f"{current_month}\t{total_sales:.2f}")
