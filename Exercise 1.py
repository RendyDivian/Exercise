def convert_to_days():
    hours = int(input("Enter number of hours:"))
    minutes = int(input("Enter number of minutes:"))
    seconds = int(input("Enter number of seconds:"))

    hours_to_days = 24/hours
    minutes_to_days = 1440/minutes
    seconds_to_days = 86400/seconds

    days = round(hours_to_days + minutes_to_days + seconds_to_days, 4)

    print(days)
    return hours_to_days, minutes_to_days, seconds_to_days


convert_to_days()
