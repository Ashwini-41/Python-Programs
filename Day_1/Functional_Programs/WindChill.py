import math

t = float(input("Enter the temperature in Fahrenheit (t): "))
v = float(input("Enter the wind speed in miles per hour(v): "))

if abs(t) > 50 or v > 120 or v < 3 :
    print("The formula is not valid for the given input values.")
else:
    wind_chill = (
        35.74 + 0.6215 * t - 35.75 * math.pow(v,0.16) + 0.4275 * t * math.pow(v,0.16)
    )
    print(f"The wind chill for temperature {t}°F and wind speed {v} mph is: {wind_chill:.2f}°F")

