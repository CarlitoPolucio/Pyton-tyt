years = int(input("Enter the year: "))

years_range = range(years - 2, 1900, -2)
for year in years_range:
    print(year)

print("that's it. 1900")