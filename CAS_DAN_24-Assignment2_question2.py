import csv
import os

# Initialize dictionaries for storing temperature data by year and by station
temperature_by_year = {}
station_temperature_data = {}

# Loop over years (1987 to 2004) to process the data from each year's file
directory_path = "temperature_data"
for year in range(1987, 2005):
    file_path = os.path.join(directory_path, f"stations_group_{year}.csv")
    
    try:
        with open(file_path) as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            # Populate the dictionary with temperatures for each station
            temperature_by_year[year] = {row[0]: list(map(float, row[4:])) for row in reader}
    except FileNotFoundError:
        print(f"Could not find file: {file_path}. Skipping this year.")
    except Exception as error:
        print(f"Error processing {file_path}: {error}")

# Aggregate temperature data across all years by station
for year_data in temperature_by_year.values():
    for station, temperatures in year_data.items():
        if station not in station_temperature_data:
            station_temperature_data[station] = []  # Initialize station data if not already present
        station_temperature_data[station].extend(temperatures)

# Calculate the average temperature for each month across all stations
monthly_avg_temps = [0] * 12  # List to store average temperatures for 12 months
# Accumulate temperatures for each station for every month
for station_temps in station_temperature_data.values():
    for month_index in range(12):
        monthly_avg_temps[month_index] += station_temps[month_index]

# Calculate monthly averages by dividing the sum by the number of stations
monthly_avg_temps = [round(month_sum / len(station_temperature_data), 2) for month_sum in monthly_avg_temps]

# Define months corresponding to each season
seasons_mapping = {
    "Summer": [11, 0, 1],  # Dec, Jan, Feb
    "Autumn": [2, 3, 4],   # Mar, Apr, May
    "Winter": [5, 6, 7],   # Jun, Jul, Aug
    "Spring": [8, 9, 10]   # Sep, Oct, Nov
}

# Calculate the average temperature for each season
season_avg_temps = {
    season: round(sum(monthly_avg_temps[month] for month in months) / len(months), 2)
    for season, months in seasons_mapping.items()
}

# Write the seasonal averages to a file
with open('average_temp.txt', 'a') as output_file:
    output_file.write("\n\nSeasonal Average Temperatures:\n")
    for season, avg_temp in season_avg_temps.items():
        output_file.write(f"{season}: {avg_temp}°C\n")

# Identify the station with the largest temperature range (difference between max and min temperature)
station_with_largest_range = max(
    station_temperature_data.items(), 
    key=lambda item: max(item[1]) - min(item[1])  # Calculate range for each station
)
largest_range_value = round(max(station_with_largest_range[1]) - min(station_with_largest_range[1]), 2)

# Save the station with the largest temperature range to a text file
with open('largest_temp_range_station.txt', 'w') as output_file:
    output_file.write("Station with the Largest Temperature Range:\n")
    output_file.write(f"{station_with_largest_range[0]}: {largest_range_value}°C\n")

# Calculate the average temperature for each station
station_avg_temperatures = {
    station: sum(temps) / len(temps) for station, temps in station_temperature_data.items()
}

# Identify the warmest and coolest stations based on average temperature
warmest_station = max(station_avg_temperatures.items(), key=lambda item: item[1])  # Max temperature
coolest_station = min(station_avg_temperatures.items(), key=lambda item: item[1])  # Min temperature

# Save the warmest and coolest stations to a text file
with open('warmest_and_coolest_stations.txt', 'w') as output_file:
    output_file.write("Warmest Station:\n")
    output_file.write(f"{warmest_station[0]}: {round(warmest_station[1], 2)}°C\n\n")
    output_file.write("Coolest Station:\n")
    output_file.write(f"{coolest_station[0]}: {round(coolest_station[1], 2)}°C\n")
