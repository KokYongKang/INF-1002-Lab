import sys

start_year = sys.argv[1]
end_year = sys.argv[2]

if start_year.isdigit() or end_year.isdigit():
    start_years = int(start_year)
    end_years = int(end_year)

    leap_years = [year for year in range(
        start_years, end_years + 1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
    num_leap_years = len(leap_years)

    if num_leap_years > 0:
        leap_years_str = ', '.join(map(str, leap_years))
        print(
            f'The number of Leap Years is {num_leap_years}, the Leap Years are {leap_years_str}')


else:
    print("Your input is invalid!")
    sys.exit(1)
