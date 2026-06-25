# Exercise 7 - Sales Analysis: Top Products

## Objective
Find the top products based on total sales using Hadoop Streaming and Python MapReduce.

## Dataset Format
Date, Product, Price, City

## Files
- sales_products.txt - Original sales dataset
- sales_products_large.txt - Dataset repeated 50 times
- mapper_top_products.py - Emits product and price
- reducer_top_products.py - Calculates total sales and finds top products

## Expected Output
TOP PRODUCTS BY SALES

1. Laptop: Rs.6,750,000.00
2. Monitor: Rs.2,500,000.00
3. Keyboard: Rs.350,000.00
4. Mouse: Rs.225,000.00
