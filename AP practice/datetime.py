from datetime import datetime

# Given date
given_date = datetime(1978, 2, 2)  # Replace with your given date (year, month, day)

# Current date
current_date = datetime.now()

# Calculate the difference
date_difference = current_date - given_date

# Extract components
days_difference = date_difference.days #datetime.timedelta
seconds_difference = date_difference.seconds
years_difference = days_difference // 365.25
#since datetim.timedelta has no attribute called years,
#we divide the days with 365.25 to get the number of years
# Print the results
print(f"Difference in years: {years_disfference} years")
print(f"Difference in days: {days_difference} days")
print(f"Difference in seconds: {seconds_difference} seconds")
