# Exercise 6 - Weather Data Analysis using Hadoop Streaming

## Objective
Analyze weather data using Hadoop MapReduce and Python streaming scripts.

## Dataset Format
Date, City, Max Temperature, Min Temperature

## Files
- weather_data.txt - Original weather dataset
- weather_large.txt - Expanded dataset
- mapper_max_temp.py - Mapper for maximum temperature
- reducer_max_temp.py - Reducer to find hottest day
- mapper_min_temp.py - Mapper for minimum temperature
- reducer_min_temp.py - Reducer to find coldest day

## Output
- Hottest Day: 2024-06-15 with 45.5 C
- Coldest Day: 2024-01-15 with -2.0 C
